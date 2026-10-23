"""
Converts an N64 Ocarina of Time sequence (.seq) to the 3DS sequence text format (.cseq) that bcseq.py assembles into a
.bcseq.

It runs the sequence the way the N64 game's sequence player does, following AudioSeq_SequencePlayerProcessSequence,
AudioSeq_SequenceChannelProcessScript and AudioSeq_SeqLayerProcessScript in the OoT decomp
(src/audio/internal/seqplayer.c), and writes what it plays.

The loop, instrument and drum steps in convert_to_3d.py read this layout:
- one track per N64 channel, with track 0 also holding the tempo changes
- notewait_off, so notes do not delay the commands after them
- notes as "<note> <velocity>, <length>", with N64 note N written as key N + 21
- channel instrument (prg), volume and pan, and sequence tempo
- the N64 instrument numbers in prg, which convert_to_3d.py changes to the 3DS ones

Ticks are N64 sequence ticks (48 per quarter note), which is also the .cseq resolution.
"""

import struct


# Argument sizes in bytes (1 = u8, 2 = s16) for channel commands 0xB0 - 0xFF, from sSeqInstructionArgsTable
channel_argument_sizes = {
    0xB0: [ 2 ], 0xB1: [], 0xB2: [ 2 ], 0xB3: [ 1 ], 0xB4: [], 0xB5: [], 0xB6: [], 0xB7: [ 2 ], 0xB8: [ 1 ],
    0xB9: [ 1 ], 0xBA: [ 1 ], 0xBB: [ 1, 2 ], 0xBC: [ 2 ], 0xBD: [ 2, 2 ], 0xBE: [], 0xBF: [], 0xC0: [], 0xC1: [ 1 ],
    0xC2: [ 2 ], 0xC3: [], 0xC4: [], 0xC5: [], 0xC6: [ 1 ], 0xC7: [ 1, 2 ], 0xC8: [ 1 ], 0xC9: [ 1 ], 0xCA: [ 1 ],
    0xCB: [ 2 ], 0xCC: [ 1 ], 0xCD: [ 1 ], 0xCE: [ 2 ], 0xCF: [ 2 ], 0xD0: [ 1 ], 0xD1: [ 1 ], 0xD2: [ 1 ],
    0xD3: [ 1 ], 0xD4: [ 1 ], 0xD5: [ 1 ], 0xD6: [ 1 ], 0xD7: [ 1 ], 0xD8: [ 1 ], 0xD9: [ 1 ], 0xDA: [ 2 ],
    0xDB: [ 1 ], 0xDC: [ 1 ], 0xDD: [ 1 ], 0xDE: [ 2 ], 0xDF: [ 1 ], 0xE0: [ 1 ], 0xE1: [ 1, 1, 1 ],
    0xE2: [ 1, 1, 1 ], 0xE3: [ 1 ], 0xE4: [], 0xE5: [ 1 ], 0xE6: [ 1 ], 0xE7: [ 2 ], 0xE8: [ 1, 1, 1 ], 0xE9: [ 1 ],
    0xEA: [], 0xEB: [ 1, 1 ], 0xEC: [], 0xED: [ 1 ], 0xEE: [ 1 ], 0xEF: [ 2, 1 ], 0xF0: [], 0xF1: [ 1 ],
}

# Argument sizes for the flow control commands 0xF2 - 0xFF, which the header, channels and layers share
flow_argument_sizes = {
    0xF2: [ 1 ], 0xF3: [ 1 ], 0xF4: [ 1 ], 0xF5: [ 2 ], 0xF6: [], 0xF7: [], 0xF8: [ 1 ], 0xF9: [ 2 ], 0xFA: [ 2 ],
    0xFB: [ 2 ], 0xFC: [ 2 ], 0xFD: [], 0xFE: [], 0xFF: [],
}

# Argument sizes for sequence header commands 0xC0 - 0xF1, from AudioSeq_SequencePlayerProcessSequence
header_argument_sizes = {
    0xC2: [], 0xC3: [], 0xC4: [ 1, 1 ], 0xC5: [ 2 ], 0xC6: [], 0xC7: [ 1, 2 ], 0xC8: [ 1 ], 0xC9: [ 1 ], 0xCC: [ 1 ],
    0xCD: [ 2 ], 0xCE: [ 1 ], 0xD0: [ 1 ], 0xD1: [ 2 ], 0xD2: [ 2 ], 0xD3: [ 1 ], 0xD4: [], 0xD5: [ 1 ], 0xD6: [ 2 ],
    0xD7: [ 2 ], 0xD9: [ 1 ], 0xDA: [ 1, 2 ], 0xDB: [ 1 ], 0xDC: [ 1 ], 0xDD: [ 1 ], 0xDE: [ 1 ], 0xDF: [ 1 ],
    0xEF: [ 2, 1 ], 0xF0: [], 0xF1: [ 1 ],
}

# A sequence that runs this long without ending or looping is refused, so that one that never ends cannot run forever
MAX_TICKS = 500000

"""
Constants that time a note with a delay of 0, which plays its whole sample (AudioSeq_SeqLayerProcessScriptStep4).
They come from AudioHeap_Init in src/audio/internal/heap.c for NTSC (refresh rate 60) and the 32000 Hz audio specs:
- samplesPerFrameTarget = ALIGN16( 32000 / 60 ) = 544
- ticksPerUpdate = ( 544 + 0x10 ) / 0xD0 + 1 = 3
- aiSamplingFrequency = osAiSetFrequency( 32000 ) = VI_NTSC_CLOCK / dacRate = 48681812 / 1521 = 32006
- maxTempoTvTypeFactors = 1000 * REFRESH_RATE_DEVIATION_NTSC / REFRESH_RATE_NTSC = 1000 * 1.00278 / 60
- maxTempo = ticksPerUpdate * ( 60 * 1000 * 48 ) / 48 / maxTempoTvTypeFactors = 10770 ticks per minute
- unk_2870 = refreshRate * ticksPerUpdate / aiSamplingFrequency / maxTempo
The N64 game computes these in 32-bit floats, so f32() rounds every step the same way.
"""
REFRESH_RATE = 60
TICKS_PER_UPDATE = 3
AI_SAMPLING_FREQUENCY = 32006
SEQTICKS_PER_BEAT = 48


def f32( value ):
    return struct.unpack( '<f', struct.pack( '<f', value ) )[0]


MAX_TEMPO_TV_TYPE_FACTORS = f32( f32( 1000 * f32( 1.00278 ) ) / 60 )
MAX_TEMPO = int( f32( f32( TICKS_PER_UPDATE * f32( 60 * 1000 * SEQTICKS_PER_BEAT ) ) / SEQTICKS_PER_BEAT ) / MAX_TEMPO_TV_TYPE_FACTORS )
UNK_2870 = f32( f32( f32( f32( REFRESH_RATE ) * TICKS_PER_UPDATE ) / AI_SAMPLING_FREQUENCY ) / MAX_TEMPO )

# gPitchFrequencies in src/audio/internal/data.c, the playback rate of each semitone (39 is middle C)
PITCH_FREQUENCIES = [
    0.105112, 0.111362, 0.117984, 0.125, 0.132433, 0.140308, 0.148651, 0.15749,
    0.166855, 0.176777, 0.187288, 0.198425, 0.210224, 0.222725, 0.235969, 0.25,
    0.264866, 0.280616, 0.297302, 0.31498, 0.33371, 0.353553, 0.374577, 0.39685,
    0.420448, 0.445449, 0.471937, 0.5, 0.529732, 0.561231, 0.594604, 0.629961,
    0.66742, 0.707107, 0.749154, 0.793701, 0.840897, 0.890899, 0.943875, 1.0,
    1.059463, 1.122462, 1.189207, 1.259921, 1.33484, 1.414214, 1.498307, 1.587401,
    1.681793, 1.781798, 1.887749, 2.0, 2.118926, 2.244924, 2.378414, 2.519842,
    2.66968, 2.828428, 2.996615, 3.174803, 3.363586, 3.563596, 3.775498, 4.0,
    4.237853, 4.489849, 4.756829, 5.039685, 5.33936, 5.656855, 5.993229, 6.349606,
    6.727173, 7.127192, 7.550996, 8.0, 8.475705, 8.979697, 9.513658, 10.07937,
    10.6787205, 11.31371, 11.986459, 12.699211, 13.454346, 14.254383, 15.101993, 16.0,
    16.95141, 17.959395, 19.027315, 20.15874, 21.35744, 22.62742, 23.972918, 25.398422,
    26.908691, 28.508766, 30.203985, 32.0, 33.90282, 35.91879, 38.05463, 40.31748,
    42.71488, 45.25484, 47.945835, 50.796845, 53.817383, 57.017532, 60.40797, 64.0,
    67.80564, 71.83758, 76.10926, 80.63496, 85.42976, 0.055681, 0.058992, 0.0625,
    0.066216, 0.070154, 0.074325, 0.078745, 0.083427, 0.088388, 0.093644, 0.099213,
]

# gDefaultShortNoteVelocityTable and gDefaultShortNoteGateTimeTable in src/audio/internal/data.c
DEFAULT_SHORT_NOTE_VELOCITIES = [ 12, 25, 38, 51, 57, 64, 71, 76, 83, 89, 96, 102, 109, 115, 121, 127 ]
DEFAULT_SHORT_NOTE_GATE_TIMES = [ 229, 203, 177, 151, 139, 126, 113, 100, 87, 74, 61, 48, 36, 23, 10, 0 ]

NOTE_NAMES = [ 'cn', 'cs', 'dn', 'ds', 'en', 'fn', 'fs', 'gn', 'gs', 'an', 'as', 'bn' ]


class UnsupportedSequence( Exception ):
    """
    The sequence uses something this converter cannot reproduce. The message says what.
    """


def signed_byte( value ):
    value &= 0xFF
    return value - 256 if value > 127 else value


def signed_short( value ):
    value &= 0xFFFF
    return value - 65536 if value > 32767 else value


class Script:
    """
    The state of one sequence script (the header, a channel or a note layer), like SeqScriptState in the decomp.
    """

    def __init__( self, pc ):
        self.pc = pc
        self.stack = [] # [ return or loop position, remaining loop iterations ]
        self.value = 0
        self.wake = 0


class Note:

    def __init__( self, tick, key, velocity, length ):
        self.tick = tick
        self.key = key
        self.velocity = velocity
        self.length = length

    def cut( self, tick ):
        """
        Ends the note early, as AudioSeq_SeqLayerNoteDecay does when a layer stops or restarts.
        """
        if self.tick + self.length > tick:
            self.length = max( tick - self.tick, 0 )


class Layer:

    def __init__( self, pc, tick ):
        self.script = Script( pc )
        self.script.wake = tick
        self.transposition = 0
        self.gate_time = 0x80
        self.last_delay = 0
        # AudioSeq_SeqChannelSetLayer does not reset these, so a layer that uses them before setting them plays
        # whatever an earlier layer left there
        self.velocity = None
        self.short_default_delay = None
        self.finished = False
        self.note = None

    def stop( self, tick ):
        if self.note is not None:
            self.note.cut( tick )
            self.note = None
        self.finished = True


class Channel:

    def __init__( self, index ):
        self.index = index
        self.enabled = False
        self.script = None
        self.layers = [ None, None, None, None ]
        self.transposition = 0
        self.large_notes = False
        self.instrument = None
        self.io = [ -1 ] * 8
        # I/O values that a sample load started by ldsample writes when it finishes, at a time this cannot know
        self.pending_io = set()
        self.dyn_table = None

    def stop_layers( self, tick ):
        for index, layer in enumerate( self.layers ):
            if layer is not None:
                layer.stop( tick )
                self.layers[ index ] = None


class Sequence:

    def __init__( self, data, samples=None ):
        self.data = bytearray( data )
        # sample_lookup for this sequence's instrument set, used to time notes with a delay of 0
        self.samples = samples
        # Ticks per minute, AudioSeq_ResetSequencePlayer starts at 120 BPM
        self.tempo = 120 * SEQTICKS_PER_BEAT
        self.header = Script( 0 )
        self.header_stopped = False
        self.header_io = [ -1 ] * 8
        self.transposition = 0
        self.channels = [ Channel( index ) for index in range( 16 ) ]
        self.tick = 0
        self.ended = False
        self.loop = None
        # Every instrument a channel selects while the sequence plays (instr and fontinstr)
        self.instruments = set()
        self.header_positions = {}
        # Addresses of the short note tables set by ldshortvelarr and ldshortgatearr, or None for the defaults.
        # The N64 game keeps a pointer into the sequence data and reads an entry when a note uses it.
        self.short_velocity_table = None
        self.short_gate_time_table = None
        # Events per track: track number -> [ ( tick, order, event ) ], where event is a Note or a command string
        self.events = { index: [] for index in range( 16 ) }
        self.order = 0

    # Reading

    def u8( self, script ):
        if script.pc >= len( self.data ):
            raise UnsupportedSequence( 'a script reads past the end of the sequence' )
        value = self.data[ script.pc ]
        script.pc += 1
        return value

    def s16( self, script ):
        return signed_short( self.u8( script ) << 8 | self.u8( script ) )

    def compressed_u16( self, script ):
        """
        AudioSeq_ScriptReadCompressedU16: one byte, or two when the first has its 0x80 bit set
        """
        value = self.u8( script )
        if value & 0x80:
            value = ( value & 0x7F ) << 8 | self.u8( script )
        return value

    def read_arguments( self, script, sizes ):
        return [ self.u8( script ) if size == 1 else self.s16( script ) for size in sizes ]

    # Output

    def emit( self, track, event ):
        self.events[ track ].append( ( self.tick, self.order, event ) )
        self.order += 1

    # Flow control, shared by every script type (AudioSeq_HandleScriptFlowControl)

    def flow_control( self, script, command, argument ):
        """
        Returns the delay to wait, 0 to keep reading, or None when the script ends.
        """

        # At the fifth call level, the loop commands would use the loop counters that hold the return position
        if len( script.stack ) == 5 and command in ( 0xF8, 0xF7, 0xF6 ):
            raise UnsupportedSequence( 'a loop runs inside a fifth nested call' )

        if command == 0xFF: # end
            if not script.stack:
                return None
            script.pc = script.stack.pop()[0]
        elif command == 0xFD: # delay
            return self.compressed_u16( script )
        elif command == 0xFE: # delay1
            return 1
        elif command == 0xFC: # call
            if len( script.stack ) == 4:
                """
                The N64 game does not check the depth here, so a fifth call writes its return position to stack[4], which
                in SeqScriptState is remLoopIters[0 - 3]. That still returns to the right place, as long as no outer
                level is a loop (its iteration count would be overwritten) and the fifth level does not call or loop.
                """
                if any( iterations for position, iterations in script.stack ):
                    raise UnsupportedSequence( 'a fifth nested call overwrites the iteration count of a loop' )
            elif len( script.stack ) > 4:
                raise UnsupportedSequence( 'calls nest deeper than the N64 game allows' )
            script.stack.append( [ script.pc, 0 ] )
            script.pc = argument & 0xFFFF
        elif command == 0xF8: # loop, where 0 iterations means 256
            script.stack.append( [ script.pc, argument or 256 ] )
        elif command == 0xF7: # loopend
            if not script.stack:
                """
                Some sequences have a loopend with no loop before it. The N64 game then uses index -1 of its stack arrays:
                in SeqScriptState, stack[-1] is pc itself and remLoopIters[-1] is the last byte of stack[3], so the
                script continues from where it is unless that byte is 1.
                """
                return 0
            script.stack[-1][1] -= 1
            if script.stack[-1][1] > 0:
                script.pc = script.stack[-1][0]
            else:
                script.stack.pop()
        elif command == 0xF6: # break
            if script.stack:
                script.stack.pop()
        elif command in ( 0xF5, 0xF9, 0xFA, 0xFB ):
            taken = {
                0xF5: script.value >= 0,
                0xF9: script.value < 0,
                0xFA: script.value == 0,
                0xFB: True,
            }[ command ]
            if taken:
                return self.jump( script, argument & 0xFFFF )
        elif command in ( 0xF2, 0xF3, 0xF4 ):
            taken = {
                0xF2: script.value < 0,
                0xF3: script.value == 0,
                0xF4: True,
            }[ command ]
            if taken:
                return self.jump( script, script.pc + signed_byte( argument ) )

        return 0

    def jump( self, script, target ):

        # A jump back in the sequence header, outside of a call, to a position already played is the song's loop
        if script is self.header and not script.stack and target in self.header_positions:
            self.loop = ( self.header_positions[ target ], self.tick )
            self.ended = True
            return None

        script.pc = target
        return 0

    # The sequence header (AudioSeq_SequencePlayerProcessSequence)

    def run_header( self ):

        script = self.header

        while True:

            if not script.stack:
                self.header_positions.setdefault( script.pc, self.tick )

            command = self.u8( script )

            if command >= 0xF2:
                delay = self.flow_control( script, command, self.read_flow_argument( script, command ) )
                if delay is None:
                    # The header ended (or looped), which stops the whole sequence
                    self.ended = True
                    return
                if delay:
                    script.wake = self.tick + delay
                    return
                continue

            if command >= 0xC0:

                if command not in header_argument_sizes:
                    raise UnsupportedSequence( 'unknown sequence header command ' + hex( command ) )

                arguments = self.read_arguments( script, header_argument_sizes[ command ] )

                if command == 0xDD: # tempo, which the N64 game caps at maxTempo
                    self.tempo = max( min( arguments[0] * SEQTICKS_PER_BEAT, MAX_TEMPO ), 1 )
                    self.emit( 0, 'tempo ' + str( max( self.tempo // SEQTICKS_PER_BEAT, 1 ) ) )
                elif command == 0xDF: # transpose
                    self.transposition = signed_byte( arguments[0] )
                elif command == 0xDE: # rtranspose
                    self.transposition += signed_byte( arguments[0] )
                elif command == 0xCC: # ldi
                    script.value = signed_byte( arguments[0] )
                elif command == 0xC8: # sub
                    script.value = signed_byte( script.value - arguments[0] )
                elif command == 0xC9: # and
                    script.value = signed_byte( script.value & arguments[0] )
                elif command == 0xC7: # stseq
                    self.data[ arguments[1] & 0xFFFF ] = ( script.value + arguments[0] ) & 0xFF
                elif command == 0xC6: # stop: the header stops, but the channels keep playing
                    self.header_stopped = True
                    return
                elif command == 0xCD: # dyncall
                    if script.value != -1 and len( script.stack ) < 3:
                        address = ( arguments[0] & 0xFFFF ) + ( script.value << 1 )
                        script.stack.append( [ script.pc, 0 ] )
                        script.pc = self.data[ address ] << 8 | self.data[ address + 1 ]
                elif command == 0xD1: # ldshortgatearr
                    self.short_gate_time_table = arguments[0] & 0xFFFF
                elif command == 0xD2: # ldshortvelarr
                    self.short_velocity_table = arguments[0] & 0xFFFF
                elif command == 0xCE:
                    raise UnsupportedSequence( 'the sequence header uses random values (rand)' )
                elif command == 0xD4:
                    raise UnsupportedSequence( 'the sequence header mutes the sequence (mute)' )
                elif command == 0xC4:
                    raise UnsupportedSequence( 'the sequence header starts another sequence (runseq)' )

                continue

            low = command & 0x0F

            if command < 0x40: # testchan
                script.value = 0 if self.channels[ low ].enabled else 1
            elif command < 0x50: # stopchan
                self.disable_channel( self.channels[ low ] )
            elif command < 0x60: # subio
                script.value = signed_byte( script.value - self.header_io[ low & 7 ] )
            elif command < 0x70: # ldres
                self.read_arguments( script, [ 1, 1 ] )
            elif command < 0x80: # stio
                self.header_io[ low & 7 ] = script.value
            elif command < 0x90: # ldio
                script.value = self.header_io[ low & 7 ]
                if low < 2:
                    self.header_io[ low ] = -1
            elif command < 0xA0: # ldchan
                self.enable_channel( low, self.s16( script ) & 0xFFFF )
            elif command < 0xB0: # rldchan
                offset = self.s16( script )
                self.enable_channel( low, script.pc + offset )
            else: # ldseq
                self.read_arguments( script, [ 1, 2 ] )

    def short_note_table( self, address, defaults, index ):
        return defaults[ index ] if address is None else self.data[ ( address + index ) & 0xFFFF ]

    def read_flow_argument( self, script, command ):
        sizes = flow_argument_sizes[ command ]
        return self.read_arguments( script, sizes )[0] if sizes else 0

    def enable_channel( self, index, pc ):
        """
        AudioSeq_SequenceChannelEnable: replaces the channel's script and frees its layers
        """
        channel = self.channels[ index ]
        channel.stop_layers( self.tick )
        channel.enabled = True
        channel.script = Script( pc )
        # A channel processed earlier in this tick than the one starting it runs from the next tick
        channel.script.wake = self.tick + ( 1 if index < getattr( self, 'current_channel', -1 ) else 0 )

    def disable_channel( self, channel ):
        channel.stop_layers( self.tick )
        channel.enabled = False

    # Channels (AudioSeq_SequenceChannelProcessScript)

    def run_channel( self, channel ):

        script = channel.script

        while True:

            command = self.u8( script )

            if command >= 0xB0:

                if command >= 0xF2:
                    delay = self.flow_control( script, command, self.read_flow_argument( script, command ) )
                    if delay is None:
                        self.disable_channel( channel )
                        return
                    if delay:
                        script.wake = self.tick + delay
                        return
                    continue

                arguments = self.read_arguments( script, channel_argument_sizes[ command ] )

                if command == 0xC6 or command == 0xEB: # font, fontinstr
                    """
                    The argument is an index into the sequence's soundfont list, counted from its end
                    (AudioSeq_SequenceChannelProcessScript), and a converted song has only its own instrument set, which
                    is index 0. Index 0 keeps the channel on that set.
                    """
                    if arguments[0] & 0xFF:
                        raise UnsupportedSequence( 'a channel switches to soundfont ' + str( arguments[0] & 0xFF ) + ' of the sequence, and a converted song has only its own instrument set' )

                if command == 0xC1 or command == 0xEB: # instr, fontinstr
                    channel.instrument = arguments[-1] & 0xFF
                    self.instruments.add( channel.instrument )
                    self.emit( channel.index, 'prg ' + str( channel.instrument ) )
                elif command == 0xC3: # short
                    channel.large_notes = False
                elif command == 0xC4: # noshort
                    channel.large_notes = True
                elif command == 0xDF: # vol
                    self.emit( channel.index, 'volume ' + str( min( arguments[0] & 0xFF, 127 ) ) )
                elif command == 0xDD: # pan
                    self.emit( channel.index, 'pan ' + str( min( arguments[0] & 0xFF, 127 ) ) )
                elif command == 0xDB: # transpose
                    channel.transposition = signed_byte( arguments[0] )
                elif command == 0xE8: # params
                    channel.transposition = signed_byte( self.u8( script ) )
                    self.emit( channel.index, 'pan ' + str( min( self.u8( script ), 127 ) ) )
                    self.read_arguments( script, [ 1, 1, 1 ] )
                elif command == 0xE7: # ldparams
                    address = arguments[0] & 0xFFFF
                    channel.transposition = signed_byte( self.data[ address + 3 ] )
                    self.emit( channel.index, 'pan ' + str( min( self.data[ address + 4 ], 127 ) ) )
                elif command == 0xEA: # stop: the channel script stops, but its layers keep playing
                    script.wake = MAX_TICKS
                    return
                elif command == 0xCC: # ldi
                    script.value = signed_byte( arguments[0] )
                elif command == 0xC8: # sub
                    script.value = signed_byte( script.value - arguments[0] )
                elif command == 0xC9: # and
                    script.value = signed_byte( script.value & arguments[0] )
                elif command == 0xC7: # stseq
                    self.data[ arguments[1] & 0xFFFF ] = ( script.value + arguments[0] ) & 0xFF
                elif command == 0xCB: # ldseq
                    script.value = signed_byte( self.data[ ( ( arguments[0] & 0xFFFF ) + script.value ) & 0xFFFF ] )
                elif command == 0xCD: # stopchan
                    self.disable_channel( self.channels[ arguments[0] & 0x0F ] )
                elif command == 0xC2: # dyntbl
                    channel.dyn_table = arguments[0] & 0xFFFF
                elif command == 0xE4: # dyncall
                    if script.value != -1:
                        address = self.dyn_entry( channel, script.value )
                        script.stack.append( [ script.pc, 0 ] )
                        script.pc = address
                elif command == 0xC5: # dyntbllookup
                    if script.value != -1:
                        channel.dyn_table = self.dyn_entry( channel, script.value )
                elif command in ( 0xB8, 0xB7, 0xBD, 0xB9, 0xBA ):
                    raise UnsupportedSequence( 'a channel uses random values (command ' + hex( command ) + ')' )
                elif command in ( 0xB2, 0xB4, 0xB5, 0xB6, 0xBC, 0xCE, 0xCF ):
                    raise UnsupportedSequence( 'a channel uses its pointer register (command ' + hex( command ) + ')' )

                continue

            if command >= 0x70:

                low = command & 0x07
                kind = command & 0xF8

                if kind != 0x70 and low >= 4:
                    low = 0

                if kind == 0x70: # stio
                    channel.io[ low ] = script.value
                elif kind == 0x78: # rldlayer
                    offset = self.s16( script )
                    self.start_layer( channel, low, script.pc + offset )
                elif kind == 0x80: # testlayer
                    layer = channel.layers[ low ]
                    script.value = ( 1 if layer.finished else 0 ) if layer is not None else -1
                elif kind == 0x88: # ldlayer
                    self.start_layer( channel, low, self.s16( script ) & 0xFFFF )
                elif kind == 0x90: # dellayer
                    if channel.layers[ low ] is not None:
                        channel.layers[ low ].stop( self.tick )
                        channel.layers[ low ] = None
                elif kind == 0x98: # dynldlayer
                    if script.value != -1:
                        self.start_layer( channel, low, self.dyn_entry( channel, script.value ) )
                else:
                    raise UnsupportedSequence( 'unknown channel command ' + hex( command ) )

                continue

            low = command & 0x0F
            kind = command & 0xF0

            if kind == 0x00: # cdelay
                script.wake = self.tick + max( low, 1 )
                return
            elif kind == 0x10: # ldsample
                """
                Starts loading a sample and sets an I/O value to SEQ_IO_VAL_NONE until the load finishes. The load
                has no effect on what plays, but the time it writes the I/O value is unknown.
                """
                index = low if low < 8 else low - 8
                channel.io[ index ] = -1
                channel.pending_io.add( index )
            elif kind == 0x20: # ldchan
                self.enable_channel( low, self.s16( script ) & 0xFFFF )
            elif kind == 0x30: # stcio
                self.channels[ low ].io[ self.u8( script ) & 7 ] = script.value
            elif kind == 0x40: # ldcio
                script.value = self.channels[ low ].io[ self.u8( script ) & 7 ]
            elif kind == 0x50: # subio
                if ( low & 7 ) in channel.pending_io:
                    raise UnsupportedSequence( 'a channel reads an I/O value that a sample load (ldsample) writes at an unknown time' )
                script.value = signed_byte( script.value - channel.io[ low & 7 ] )
            elif kind == 0x60: # ldio
                if ( low & 7 ) in channel.pending_io:
                    raise UnsupportedSequence( 'a channel reads an I/O value that a sample load (ldsample) writes at an unknown time' )
                script.value = channel.io[ low & 7 ]
                if low < 2:
                    channel.io[ low ] = -1

    def dyn_entry( self, channel, index ):
        if channel.dyn_table is None:
            raise UnsupportedSequence( 'a channel reads a dynamic table before setting one' )
        address = channel.dyn_table + index * 2
        return self.data[ address ] << 8 | self.data[ address + 1 ]

    def start_layer( self, channel, index, pc ):
        """
        AudioSeq_SeqChannelSetLayer: a layer that is already playing has its note cut and its script replaced
        """
        if channel.layers[ index ] is not None and channel.layers[ index ].note is not None:
            channel.layers[ index ].note.cut( self.tick )
        channel.layers[ index ] = Layer( pc, self.tick )

    # Note layers (AudioSeq_SeqLayerProcessScript)

    def run_layer( self, channel, layer ):

        script = layer.script

        while True:

            command = self.u8( script )

            if command <= 0xC0:
                break

            if command >= 0xF2:
                delay = self.flow_control( script, command, self.read_flow_argument( script, command ) )
                if delay is None:
                    layer.stop( self.tick )
                    channel.layers[ channel.layers.index( layer ) ] = None
                    return
                if delay:
                    # A delay command in a layer is read like a note delay, and the layer waits for it
                    script.wake = self.tick + delay
                    return
                continue

            if command in ( 0xC1, 0xCA, 0xC9, 0xCD, 0xCE, 0xCF, 0xC6 ):
                argument = self.u8( script )
                if command == 0xC9: # shortgate
                    layer.gate_time = argument
                elif command == 0xC1: # shortvel
                    layer.velocity = argument
                elif command == 0xC6:
                    # Checked by find_unmappable_instruments before converting
                    raise UnsupportedSequence( 'a note layer sets its own instrument (linst)' )
            elif command == 0xC2: # transpose
                layer.transposition = signed_byte( self.u8( script ) )
            elif command == 0xC3: # shortdelay
                layer.short_default_delay = self.compressed_u16( script )
            elif command == 0xC7: # portamento: the 3DS has no portamento, so the notes play without the slide
                mode = self.u8( script )
                self.u8( script )
                if mode & 0x80:
                    self.u8( script )
                else:
                    self.compressed_u16( script )
            elif command == 0xCB: # env, then the release rate
                self.read_arguments( script, [ 2, 1 ] )
            elif 0xD0 <= command <= 0xDF: # ldshortvel
                layer.velocity = self.short_note_table( self.short_velocity_table, DEFAULT_SHORT_NOTE_VELOCITIES, command & 0x0F )
            elif 0xE0 <= command <= 0xEF: # ldshortgate
                layer.gate_time = self.short_note_table( self.short_gate_time_table, DEFAULT_SHORT_NOTE_GATE_TIMES, command & 0x0F )
            elif command in ( 0xC4, 0xC5, 0xC8, 0xCC, 0xF0, 0xF1 ):
                pass
            else:
                raise UnsupportedSequence( 'unknown note layer command ' + hex( command ) )

        # AudioSeq_SeqLayerProcessScriptStep3 and Step4: a note or a rest

        if layer.note is not None:
            layer.note.cut( self.tick )
            layer.note = None

        if command == 0xC0: # ldelay
            script.wake = self.tick + max( self.compressed_u16( script ), 1 )
            return

        kind = command & 0xC0

        if channel.large_notes:

            if kind == 0x00: # notedvg
                delay = self.compressed_u16( script )
                velocity = self.u8( script )
                layer.gate_time = self.u8( script )
                layer.last_delay = delay
            elif kind == 0x40: # notedv
                delay = self.compressed_u16( script )
                velocity = self.u8( script )
                layer.gate_time = 0
                layer.last_delay = delay
            else: # notevg
                delay = layer.last_delay
                velocity = self.u8( script )
                layer.gate_time = self.u8( script )

            layer.velocity = velocity

        else:

            # Short notes take their velocity and gate from the layer, set by shortvel, shortgate and the tables
            if kind == 0x00: # snoted
                delay = self.compressed_u16( script )
                layer.last_delay = delay
            elif kind == 0x40: # snotedef
                if layer.short_default_delay is None:
                    raise UnsupportedSequence( 'a short note uses the default delay before shortdelay sets it' )
                delay = layer.short_default_delay
            else: # snotelast
                delay = layer.last_delay

            if layer.velocity is None:
                raise UnsupportedSequence( 'a short note plays before its layer sets a velocity' )

            velocity = layer.velocity

        if velocity > 0x7F:
            velocity = 0x7F

        semitone = command - kind

        if channel.instrument is None:
            # AudioSeq_SeqLayerProcessScriptStep4 ends before setting a delay, so the layer runs again next tick
            script.wake = self.tick + max( delay, 1 )
            return

        # Drums ignore the sequence transposition (AudioSeq_SeqLayerProcessScriptStep4)
        if channel.instrument == 0x7F:
            semitone += channel.transposition + layer.transposition
        else:
            semitone += self.transposition + channel.transposition + layer.transposition

        # The N64 game mutes notes outside of the instrument range, before setting a delay of 0 from the sample
        if not 0 <= semitone < 0x80 or semitone + 21 > 127:
            script.wake = self.tick + max( delay, 1 )
            return

        if delay == 0:
            delay = self.whole_sample_delay( channel.instrument, semitone )
            gate_delay = 0
        else:
            gate_delay = ( layer.gate_time * delay ) >> 8

        script.wake = self.tick + delay

        length = delay - gate_delay

        if length <= 0:
            return

        layer.note = Note( self.tick, semitone + 21, velocity, length )
        self.emit( channel.index, layer.note )

    def whole_sample_delay( self, instrument, semitone ):
        """
        The delay of a note with a delay of 0, which waits for its whole sample (AudioSeq_SeqLayerProcessScriptStep4):
        time = loop end * tempo * unk_2870 / freqScale, limited to 0x7FFE, and the delay is time + 1.
        """

        if self.samples is None:
            raise UnsupportedSequence( 'a note has no delay, and there is no sample table for its instrument set' )

        if instrument == 0x7F:
            sample = self.samples[ 'drums' ].get( semitone )
            if sample is None:
                raise UnsupportedSequence( 'a note with no delay plays drum ' + str( semitone ) + ', which has no sample' )
            loop_end, tuning = sample
            frequency_scale = f32( tuning )
        elif instrument < 0x7E:
            entry = self.samples[ 'instruments' ].get( instrument )
            if entry is None:
                raise UnsupportedSequence( 'a note with no delay plays instrument ' + str( instrument ) + ', which is empty' )
            range_low, range_high, low, normal, high = entry
            # Audio_GetInstrumentTunedSample
            sample = low if semitone < range_low else normal if semitone <= range_high else high
            if sample is None:
                raise UnsupportedSequence( 'a note with no delay plays instrument ' + str( instrument ) + ' outside its samples' )
            loop_end, tuning = sample
            frequency_scale = f32( f32( PITCH_FREQUENCIES[ semitone ] ) * f32( tuning ) )
        else:
            # Synthetic waves and sound effects (the song is skipped before converting)
            return 1

        time = f32( loop_end )
        time = f32( time * self.tempo )
        time = f32( time * UNK_2870 )
        time = f32( time / frequency_scale )

        if time > 0x7FFE:
            time = 0x7FFE

        return int( time ) + 1

    # Running

    def run( self ):

        while not self.ended:

            if self.tick > MAX_TICKS:
                raise UnsupportedSequence( 'the sequence neither ends nor loops' )

            if not self.header_stopped and self.header.wake <= self.tick:
                self.run_header()
                if self.ended:
                    break

            any_enabled = False

            for channel in self.channels:

                self.current_channel = channel.index

                if not channel.enabled:
                    continue

                any_enabled = True

                if channel.script.wake <= self.tick:
                    self.run_channel( channel )

                for layer in list( channel.layers ):
                    if layer is not None and layer in channel.layers and layer.script.wake <= self.tick:
                        self.run_layer( channel, layer )

            self.current_channel = -1

            if self.header_stopped and not any_enabled:
                break

            self.tick += 1

        # The sequence stops here, so every note still playing is cut
        for channel in self.channels:
            for layer in channel.layers:
                if layer is not None and layer.note is not None:
                    layer.note.cut( self.tick )

    # Writing

    def write_cseq( self, path ):

        tracks = [ index for index in range( 16 ) if self.events[ index ] or index == 0 ]

        lines = [ ';', '; Converted from an N64 sequence by n64_to_cseq.py', ';', '' ]
        mask = sum( 1 << index for index in tracks )
        lines.append( '\talloctrack ' + str( mask ) )

        for index in tracks[ 1: ]:
            lines.append( '\topentrack ' + str( index ) + ', _track_' + str( index ) )

        for index in tracks:

            if index != 0:
                lines.append( '' )
                lines.append( '_track_' + str( index ) + ':' )

            lines.append( '\tnotewait_off' )
            tick = 0

            for event_tick, order, event in sorted( self.events[ index ], key=lambda item: ( item[0], item[1] ) ):

                if isinstance( event, Note ) and event.length <= 0:
                    continue

                if event_tick > tick:
                    lines.append( '\twait ' + str( event_tick - tick ) )
                    tick = event_tick

                if isinstance( event, Note ):
                    lines.append( '\t' + note_name( event.key ) + ' ' + str( event.velocity ) + ', ' + str( event.length ) )
                else:
                    lines.append( '\t' + event )

            lines.append( '\tfin' )

        with open( path, 'w', encoding='utf-8' ) as file:
            file.write( '\n'.join( lines ) + '\n' )


def note_name( key ):
    octave = key // 12 - 1
    return NOTE_NAMES[ key % 12 ] + ( str( octave ) if octave >= 0 else 'm' + str( -octave ) )


def convert( seq_path, cseq_path, samples=None ):
    """
    Converts seq_path to cseq_path. samples is the sample_lookup entry for the sequence's instrument set.

    Returns ( loop, None, instruments ), where loop is ( loop start tick, loop end tick ) or None for a song that ends
    and instruments is every instrument a channel selected while playing, or ( None, reason, None ) when the sequence
    cannot be converted.
    """

    with open( seq_path, 'rb' ) as file:
        sequence = Sequence( file.read(), samples )

    try:
        sequence.run()
    except UnsupportedSequence as error:
        return None, str( error ), None

    sequence.write_cseq( cseq_path )

    return sequence.loop, None, sequence.instruments

"""
Generates drum_note_lookup and sample_lookup for Convert to 3D.py.

drum_note_lookup: On the N64, each drum note plays one sample at a fixed pitch. On the 3DS, the drum kit is the last
instrument in each bank, and each key plays a sample at a pitch that depends on the key. The 3DS kits put the drums on
different keys, often in reverse order, so each N64 drum is matched to the 3DS key that plays the same sample at the same
pitch.

sample_lookup: The loop end and tuning of every N64 instrument and drum sample. A note with a delay of 0 plays its whole
sample, and its layer waits for the sample to end, so n64_to_cseq.py needs the sample length to time it.

Requires:
- The OoT MQ debug ROM (the version the 3DS banks match), uncompressed, as used by Ship of Harkinian
- The 3DS sound archive, QueenSound.bcsar, from the OoT3D romfs/sound folder

Usage: python "Generate Lookup Tables.py" <MQ debug ROM> <QueenSound.bcsar>
"""

import math
import struct
import sys

import bcsar

# From the decomp: baseroms/gc-eu-mq-dbg/config.yml and segments.csv
MQ_DEBUG_DMADATA = 0x12F70
MQ_DEBUG_CODE_VRAM = 0x8001CE60
MQ_DEBUG_SOUNDFONT_TABLE = 0x801550D0
MQ_DEBUG_AUDIOBANK_SEGMENT = 3
MQ_DEBUG_CODE_SEGMENT = 28

# 3DS bank names by bank ID, from the string table in QueenSound.bcsar
bank_names = [
    'BANK_PLAYER', 'BANK_ITEM', 'BANK_ENVIROMENT', 'BANK_ENEMY', 'BANK_SYSTEM', 'BANK_OCARINA', 'BANK_VOICE',
    'BANK_ORCHE', 'BANK_YOUSEI', 'BANK_MARKET', 'BANK_TITLE', 'BANK_JAB', 'BANK_FOLK', 'BANK_MEGAMI', 'BANK_HONOO',
    'BANK_DUNGEONBANK', 'BANK_MORI', 'BANK_RONRON', 'BANK_GORON', 'BANK_KOKIRI', 'BANK_TAMASHII', 'BANK_UMA', 'BANK_OK',
    'BANK_DENSETU', 'BANK_MATOATE', 'BANK_ZORA', 'BANK_OMISE', 'BANK_KOORI', 'BANK_YAMI', 'BANK_MIZU', 'BANK_SARIA',
    'BANK_GERUDO', 'BANK_KUSURI', 'BANK_KOTAKE', 'BANK_GANONJYO', 'BANK_CHIKA', 'BANK_VSGANON', 'BANK_STAFF',
    'BANK_STAFF2', 'BANK_FANFARE', 'BANK_FUKUROU', 'BANK_SE_ITEM', 'BANK_NATURE',
]

# Two samples are treated as the same sample when their lengths differ by at most this fraction
LENGTH_TOLERANCE = 0.03

"""
A drum may play up to this many semitones away from its N64 pitch. A song with a drum note that has no 3DS key within
this distance is skipped by Convert to 3D.py.

Many N64 drum pitches do not exist in the 3DS kits. In BANK_ORCHE, N64 drums 16 - 20 use one sample at rising pitches,
but the 3DS keys for that sample (28 - 32) play falling pitches instead, so only drum 16 has an exact key. The 3DS game's
own sequences use the nearest pitch for these drums, 1 - 3 semitones away (NA_BGM_EVENT_CLEAR plays N64 drum 17 on key
28, one semitone low).

On the songs in data/Music, counting channels that only play drums, exact pitch only would skip 474 of the 534 songs
with drums, and 3 semitones skips 79.
"""
PITCH_TOLERANCE = 3.05


def find_font( rom, font_index ):
    """
    Returns ( ROM offset of the soundfont, instrument count, drum count )
    """

    def segment( index ):
        return struct.unpack_from( '>IIII', rom, MQ_DEBUG_DMADATA + index * 16 )

    audiobank = segment( MQ_DEBUG_AUDIOBANK_SEGMENT )[0]
    code = segment( MQ_DEBUG_CODE_SEGMENT )[0]

    table = code + ( MQ_DEBUG_SOUNDFONT_TABLE - MQ_DEBUG_CODE_VRAM )
    entry = table + 16 + font_index * 16
    font_offset = struct.unpack_from( '>I', rom, entry )[0]

    return audiobank + font_offset, rom[ entry + 12 ], rom[ entry + 13 ]


def read_tuned_sample( rom, base, offset ):
    """
    Returns ( loop end, tuning ) of the TunedSample at base + offset, or None if it has no sample
    """

    sample_offset, tuning = struct.unpack_from( '>If', rom, base + offset )

    if sample_offset == 0:
        return None

    loop_offset = struct.unpack_from( '>I', rom, base + sample_offset + 8 )[0]
    loop_end = struct.unpack_from( '>I', rom, base + loop_offset + 4 )[0]

    return ( loop_end, tuning )


def read_n64_samples( rom, font_index ):
    """
    Returns { 'instruments': { slot: ( normal range low, normal range high, low, normal, high ) },
    'drums': { drum index: ( loop end, tuning ) } }, where low, normal and high are ( loop end, tuning ) or None
    """

    base, instrument_count, drum_count = find_font( rom, font_index )
    instruments = {}
    drums = {}

    for slot in range( instrument_count ):

        offset = struct.unpack_from( '>I', rom, base + 8 + slot * 4 )[0]

        if offset == 0:
            continue

        range_low, range_high = rom[ base + offset + 1 ], rom[ base + offset + 2 ]
        tuned_samples = [ read_tuned_sample( rom, base, offset + 8 + index * 8 ) for index in range( 3 ) ]
        instruments[ slot ] = ( range_low, range_high, *tuned_samples )

    drum_list = struct.unpack_from( '>I', rom, base )[0]

    for index in range( drum_count ):

        offset = struct.unpack_from( '>I', rom, base + drum_list + index * 4 )[0]

        if offset != 0:
            drums[ index ] = read_tuned_sample( rom, base, offset + 4 )

    return { 'instruments': instruments, 'drums': drums }


def read_n64_drums( rom, font_index ):
    """
    Returns { drum index: ( sample length in frames, pitch in semitones ) }
    """

    base, instrument_count, drum_count = find_font( rom, font_index )
    drum_list = struct.unpack_from( '>I', rom, base )[0]
    drums = {}

    for index in range( drum_count ):

        offset = struct.unpack_from( '>I', rom, base + drum_list + index * 4 )[0]

        if offset == 0:
            continue

        sample_offset, tuning = struct.unpack_from( '>If', rom, base + offset + 4 )
        bits = struct.unpack_from( '>I', rom, base + sample_offset )[0]
        codec = bits >> 28
        size = bits & 0xFFFFFF
        # ADPCM stores 16 samples in 9 bytes, or in 5 bytes for the small variant
        frames = size // 9 * 16 if codec == 0 else size // 5 * 16

        drums[ index ] = ( frames, math.log2( tuning * 32000 ) * 12 )

    return drums


def match_drums( n64_drums, keys ):
    """
    Returns { N64 drum index: 3DS key or None }. A drum matches the keys that use the sample closest to its length,
    and among those, the key with the nearest pitch, if it is within PITCH_TOLERANCE. When two keys are equally near,
    the lower key wins.
    """

    lengths = sorted( { length for length, pitch in keys.values() } )
    result = {}

    for drum, ( frames, pitch ) in sorted( n64_drums.items() ):

        closest = min( lengths, key=lambda length: abs( length - frames ) ) if lengths else None

        if closest is None or abs( closest - frames ) / frames > LENGTH_TOLERANCE:
            result[ drum ] = None
            continue

        candidates = sorted( ( round( abs( key_pitch - pitch ), 3 ), key ) for key, ( length, key_pitch ) in keys.items() if length == closest )
        result[ drum ] = candidates[0][1] if candidates and candidates[0][0] <= PITCH_TOLERANCE else None

    return result


def main():

    if len( sys.argv ) != 3:
        print( __doc__ )
        return

    rom = open( sys.argv[1], 'rb' ).read()
    archive = bcsar.SoundArchive( sys.argv[2] )

    # Imported here so that this script can be run from any folder
    sys.path.insert( 0, '.' )
    import importlib.util
    spec = importlib.util.spec_from_file_location( 'convert', './Convert to 3D.py' )
    convert = importlib.util.module_from_spec( spec )
    spec.loader.exec_module( convert )

    print( 'drum_note_lookup = {' )

    for instrument_set, bank in sorted( convert.instrument_set_lookup.items() ):

        if instrument_set not in convert.instrument_list_lookup:
            continue

        n64_drums = read_n64_drums( rom, int( instrument_set, 16 ) )

        if not n64_drums:
            continue

        kit_index, keys = bcsar.drum_keys( archive, bank )

        print( "    # " + bank_names[ bank ] + ( '' if kit_index is not None else ' has no drum kit' ) )
        print( "    '" + instrument_set + "': {" )
        print( "        'program': " + str( kit_index ) + "," )
        print( "        'notes': {" )

        matches = match_drums( n64_drums, keys )
        items = [ str( drum ) + ': ' + str( key ) for drum, key in matches.items() ]

        for start in range( 0, len( items ), 8 ):
            print( '            ' + ', '.join( items[ start:start + 8 ] ) + ',' )

        print( '        },' )
        print( '    },' )

    print( '}' )
    print()

    # Tunings are 32-bit floats in the ROM. repr() of the unpacked value converts back to the same 32-bit float.
    def sample_text( sample ):
        return 'None' if sample is None else '( ' + str( sample[0] ) + ', ' + repr( sample[1] ) + ' )'

    print( 'sample_lookup = {' )

    for instrument_set in sorted( convert.instrument_list_lookup ):

        samples = read_n64_samples( rom, int( instrument_set, 16 ) )

        print( "    '" + instrument_set + "': {" )
        print( "        'instruments': {" )

        for slot, ( range_low, range_high, low, normal, high ) in sorted( samples[ 'instruments' ].items() ):
            print( '            ' + str( slot ) + ': ( ' + str( range_low ) + ', ' + str( range_high ) + ', '
                   + ', '.join( sample_text( sample ) for sample in ( low, normal, high ) ) + ' ),' )

        print( '        },' )
        print( "        'drums': {" )

        items = [ str( drum ) + ': ' + sample_text( sample ) for drum, sample in sorted( samples[ 'drums' ].items() ) ]

        for start in range( 0, len( items ), 4 ):
            print( '            ' + ', '.join( items[ start:start + 4 ] ) + ',' )

        print( '        },' )
        print( '    },' )

    print( '}' )


if __name__ == '__main__':
    main()

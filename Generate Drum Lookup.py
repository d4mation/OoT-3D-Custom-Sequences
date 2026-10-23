"""
Generates drum_note_lookup for Convert to 3D.py.

On the N64, each drum note plays one sample at a fixed pitch. On the 3DS, the drum kit is the last instrument in each
bank, and each key plays a sample at a pitch that depends on the key. The 3DS kits put the drums on different keys, often
in reverse order, so each N64 drum is matched to the 3DS key that plays the same sample at the same pitch.

Requires:
- The OoT MQ debug ROM (the version the 3DS banks match), uncompressed, as used by Ship of Harkinian
- The .sf2 files that caesar (https://github.com/kr3nshaw/caesar) exports from the 3DS QueenSound.bcsar, one per bank,
  in <folder>/<BANK_NAME>/<BANK_NAME>.sf2

Usage: python "Generate Drum Lookup.py" <MQ debug ROM> <caesar output folder>
"""

import math
import struct
import sys

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


def read_n64_drums( rom, font_index ):
    """
    Returns { drum index: ( sample length in frames, pitch in semitones ) }
    """

    def segment( index ):
        return struct.unpack_from( '>IIII', rom, MQ_DEBUG_DMADATA + index * 16 )

    audiobank = segment( MQ_DEBUG_AUDIOBANK_SEGMENT )[0]
    code = segment( MQ_DEBUG_CODE_SEGMENT )[0]

    table = code + ( MQ_DEBUG_SOUNDFONT_TABLE - MQ_DEBUG_CODE_VRAM )
    entry = table + 16 + font_index * 16
    font_offset = struct.unpack_from( '>I', rom, entry )[0]
    drum_count = rom[ entry + 13 ]

    base = audiobank + font_offset
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


def read_sf2_drum_keys( path ):
    """
    Returns ( drum kit index, { key: ( sample length, pitch in semitones ) } ), or ( None, {} ) if the bank has no drum kit
    """

    data = open( path, 'rb' ).read()
    chunks = {}

    def walk( start, end ):
        position = start
        while position + 8 <= end:
            chunk_id, size = struct.unpack_from( '<4sI', data, position )
            if chunk_id == b'LIST':
                walk( position + 12, position + 8 + size )
            else:
                chunks[ chunk_id ] = data[ position + 8:position + 8 + size ]
            position += 8 + size + ( size & 1 )

    walk( 12, len( data ) )

    def records( name, layout ):
        size = struct.calcsize( layout )
        return [ struct.unpack_from( layout, chunks[ name ], i * size ) for i in range( len( chunks[ name ] ) // size ) ]

    presets = records( b'phdr', '<20sHHHIII' )
    preset_bags = records( b'pbag', '<HH' )
    preset_generators = records( b'pgen', '<HH' )
    instruments = records( b'inst', '<20sH' )
    instrument_bags = records( b'ibag', '<HH' )
    instrument_generators = records( b'igen', '<HH' )
    samples = records( b'shdr', '<20sIIIIIbbHH' )

    def zones( bags, generators, first, last ):
        for bag in range( first, last ):
            yield dict( generators[ bags[ bag ][0]:bags[ bag + 1 ][0] ] )

    def signed( value ):
        return value - 0x10000 if value >= 0x8000 else value

    # The last record in phdr is the terminal record
    for preset_index in range( len( presets ) - 1 ):

        bank = presets[ preset_index ][2]

        # Bank 128 is the percussion bank
        if bank != 128:
            continue

        keys = {}

        for preset_zone in zones( preset_bags, preset_generators, presets[ preset_index ][3], presets[ preset_index + 1 ][3] ):

            # Generator 41 is the instrument
            if 41 not in preset_zone:
                continue

            instrument = preset_zone[ 41 ]

            for zone in zones( instrument_bags, instrument_generators, instruments[ instrument ][1], instruments[ instrument + 1 ][1] ):

                # Generator 53 is the sample, 43 the key range, 58 the root key, 51 coarse tune and 52 fine tune
                if 53 not in zone:
                    continue

                sample = samples[ zone[ 53 ] ]
                start, end, rate, original_pitch, correction = sample[1], sample[2], sample[5], sample[6], sample[7]
                key_range = zone.get( 43, 0x7F00 )
                root = zone.get( 58, original_pitch )
                coarse = signed( zone.get( 51, 0 ) )
                fine = signed( zone.get( 52, 0 ) ) + correction

                for key in range( key_range & 0xFF, ( key_range >> 8 ) + 1 ):
                    pitch = math.log2( rate ) * 12 + ( key - root + coarse ) + fine / 100
                    keys[ key ] = ( end - start, pitch )

        return preset_index, keys

    return None, {}


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
    folder = sys.argv[2]

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

        kit_index, keys = read_sf2_drum_keys( folder + '/' + bank_names[ bank ] + '/' + bank_names[ bank ] + '.sf2' )

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


if __name__ == '__main__':
    main()

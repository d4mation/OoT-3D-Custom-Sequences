"""
Reads the instrument banks and wave lengths from a 3DS sound archive (.bcsar), such as OoT3D's QueenSound.bcsar from the
game's romfs/sound folder.

Layout, as used here (all values little endian, references are a u16 type, 2 bytes of padding and a u32 offset):
- CSAR header: section references to STRG (0x2000), INFO (0x2001) and FILE (0x2002)
- INFO: references to the bank table (0x2101), wave archive table (0x2103) and file table (0x2106), each a u32 count
  followed by references to entries, relative to the start of the table
- A bank entry starts with its file ID and a reference to a table of wave archive item IDs
- A file entry references an internal location: offset and size of the file in the FILE section's body
- CBNK (bank): INFO holds a wave ID table (wave archive item ID, wave index) and an instrument table. An instrument
  references its key regions directly (0x6000), through a key range table (0x6001) or through a per-key index table
  (0x6002). Key regions reference velocity regions the same way. A velocity region holds an index into the wave ID
  table, a bitfield of the parameters that follow, and the parameters: original key, volume, pan, pitch ratio, ...
- CWAR (wave archive): INFO lists the waves as offsets into its FILE section's body
- CWAV (wave): INFO holds the encoding, the loop flag, the sample rate, the loop start and the loop end (sample count)
"""

import math
import struct

DIRECT = 0x6000
RANGE_TABLE = 0x6001
INDEX_TABLE = 0x6002
NULL_OFFSET = 0xFFFFFFFF


def u32( data, offset ):
    return struct.unpack_from( '<I', data, offset )[0]


def reference( data, offset ):
    """
    Returns ( type, offset ) of the reference at offset
    """
    return struct.unpack_from( '<HxxI', data, offset )


def reference_table( data, offset ):
    """
    Returns [ ( type, offset relative to the table ) ] for the reference table at offset
    """
    return [ reference( data, offset + 4 + index * 8 ) for index in range( u32( data, offset ) ) ]


def block( data, header_offset ):
    """
    Returns the offset of the body of the block whose header offset is at header_offset
    """
    return u32( data, header_offset ) + 8


class SoundArchive:

    def __init__( self, path ):

        self.data = open( path, 'rb' ).read()

        if self.data[:4] != b'CSAR':
            raise ValueError( path + ' is not a 3DS sound archive (CSAR)' )

        sections = {}
        for index in range( struct.unpack_from( '<H', self.data, 0x10 )[0] ):
            section_type, offset, size = struct.unpack_from( '<HxxII', self.data, 0x14 + index * 12 )
            sections[ section_type ] = offset

        self.info = sections[ 0x2001 ] + 8
        self.file_body = sections[ 0x2002 ] + 8

        tables = { section_type: self.info + offset for section_type, offset in reference_table_header( self.data, self.info ) }
        self.bank_table = tables[ 0x2101 ]
        self.wave_archive_table = tables[ 0x2103 ]
        self.file_table = tables[ 0x2106 ]
        self.wave_archives = {}

    def file( self, file_id ):
        """
        Returns the bytes of an internal file
        """
        entry_type, entry_offset = reference_table( self.data, self.file_table )[ file_id ]
        entry = self.file_table + entry_offset
        location_type, location_offset = reference( self.data, entry )
        if location_type != 0x220C:
            raise ValueError( 'file ' + str( file_id ) + ' is not stored in the archive' )
        location = entry + location_offset
        offset, size = struct.unpack_from( '<II', self.data, location + 4 )
        return self.data[ self.file_body + offset:self.file_body + offset + size ]

    def bank( self, bank_id ):
        """
        Returns the Bank with this bank ID (the number convert_to_3d.py writes to .cmeta)
        """
        entry_type, entry_offset = reference_table( self.data, self.bank_table )[ bank_id ]
        file_id = u32( self.data, self.bank_table + entry_offset )
        return Bank( self, self.file( file_id ) )

    def wave( self, wave_archive_item_id, wave_index ):
        """
        Returns ( sample rate, loop end ) of a wave in a wave archive
        """
        archive_index = wave_archive_item_id & 0xFFFFFF

        if archive_index not in self.wave_archives:
            entry_type, entry_offset = reference_table( self.data, self.wave_archive_table )[ archive_index ]
            self.wave_archives[ archive_index ] = self.file( u32( self.data, self.wave_archive_table + entry_offset ) )

        archive = self.wave_archives[ archive_index ]
        info = block( archive, 0x18 )
        file_body = block( archive, 0x24 )
        count = u32( archive, info )
        if wave_index >= count:
            raise ValueError( 'wave ' + str( wave_index ) + ' is not in wave archive ' + str( archive_index ) )
        wave_offset = u32( archive, info + 4 + wave_index * 12 + 4 )
        wave = archive[ file_body + wave_offset: ]

        wave_info = block( wave, 0x18 )
        sample_rate, loop_start, loop_end = struct.unpack_from( '<III', wave, wave_info + 4 )
        return sample_rate, loop_end


def reference_table_header( data, info ):
    """
    The INFO section body starts with 8 references (sound, sound group, bank, player, wave archive, group, file and
    project tables), not a counted reference table
    """
    return [ reference( data, info + index * 8 ) for index in range( 8 ) ]


class Bank:

    def __init__( self, archive, data ):

        if data[:4] != b'CBNK':
            raise ValueError( 'not a 3DS bank (CBNK)' )

        self.archive = archive
        self.data = data
        info = block( data, 0x18 )

        wave_table_type, wave_table_offset = reference( data, info )
        instrument_table_type, instrument_table_offset = reference( data, info + 8 )

        wave_table = info + wave_table_offset
        self.waves = [ struct.unpack_from( '<II', data, wave_table + 4 + index * 8 ) for index in range( u32( data, wave_table ) ) ]
        self.instrument_table = info + instrument_table_offset

    def instruments( self ):
        """
        Returns [ ( key table type, { key: velocity region } ) ] per instrument index, where a velocity region is a dict
        with wave_index, original_key, pitch (a frequency ratio), sample_rate and length. Keys without a region are
        left out.
        """
        result = []
        for entry_type, entry_offset in reference_table( self.data, self.instrument_table ):
            if entry_offset == NULL_OFFSET:
                result.append( ( None, {} ) )
                continue
            instrument = self.instrument_table + entry_offset
            table_type = reference( self.data, instrument )[0]
            result.append( ( table_type, self.regions_by_key( instrument, self.key_region ) ) )
        return result

    def regions_by_key( self, offset, read_child ):
        """
        Follows a direct (0x6000), range table (0x6001) or index table (0x6002) reference at offset, and returns
        { key or velocity: read_child( child offset ) } for every value from 0 to 127 that has a child
        """
        table_type, table_offset = reference( self.data, offset )
        table = offset + table_offset
        result = {}

        if table_type == DIRECT:
            child_type, child_offset = reference( self.data, table )
            child = read_child( table + child_offset )
            return { key: child for key in range( 128 ) }

        if table_type == RANGE_TABLE:
            count = u32( self.data, table )
            # The upper keys are u8s, padded to 4 bytes
            upper_keys = list( self.data[ table + 4:table + 4 + count ] )
            references_start = table + 4 + ( ( count + 3 ) & ~3 )
            low = 0
            for index, upper in enumerate( upper_keys ):
                child_type, child_offset = reference( self.data, references_start + index * 8 )
                if child_offset != NULL_OFFSET:
                    child = read_child( table + child_offset )
                    for key in range( low, upper + 1 ):
                        result[ key ] = child
                low = upper + 1
            return result

        if table_type == INDEX_TABLE:
            minimum, maximum = self.data[ table ], self.data[ table + 1 ]
            for index, key in enumerate( range( minimum, maximum + 1 ) ):
                child_type, child_offset = reference( self.data, table + 4 + index * 8 )
                if child_offset != NULL_OFFSET:
                    result[ key ] = read_child( table + child_offset )
            return result

        raise ValueError( 'unknown region table type ' + hex( table_type ) )

    def key_region( self, offset ):
        """
        A key region holds velocity regions. Returns the velocity region for the highest velocity.
        """
        velocities = self.regions_by_key( offset, self.velocity_region )
        return velocities[ max( velocities ) ]

    def velocity_region( self, offset ):
        wave_index, flags = struct.unpack_from( '<II', self.data, offset )
        position = offset + 8
        original_key = 60
        pitch = 1.0
        # Parameters follow in bit order, 4 bytes each for these first four: original key, volume, pan, pitch
        for bit in range( 4 ):
            if flags & ( 1 << bit ):
                if bit == 0:
                    original_key = self.data[ position ]
                elif bit == 3:
                    pitch = struct.unpack_from( '<f', self.data, position )[0]
                position += 4
        sample_rate, length = self.archive.wave( *self.waves[ wave_index ] )
        return {
            'wave_index': wave_index,
            'original_key': original_key,
            'pitch': pitch,
            'sample_rate': sample_rate,
            'length': length,
        }


def drum_keys( archive, bank_id ):
    """
    Returns ( drum kit index, { key: ( sample length, pitch in semitones ) } ) for the bank's drum kit, or ( None, {} )
    if the bank has none. The drum kit is the last instrument, and it gives each key its own region through an index
    table (0x6002), where melodic instruments use a direct reference or a key range table.
    """
    instruments = archive.bank( bank_id ).instruments()

    if not instruments or instruments[-1][0] != INDEX_TABLE:
        return None, {}

    kit_index = len( instruments ) - 1
    regions = instruments[ kit_index ][1]

    keys = {}
    for key, region in regions.items():
        pitch = math.log2( region[ 'sample_rate' ] ) * 12 + ( key - region[ 'original_key' ] ) + math.log2( region[ 'pitch' ] ) * 12
        keys[ key ] = ( region[ 'length' ], pitch )

    return kit_index, keys

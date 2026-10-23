"""
Assembles the .cseq text that n64_to_cseq.py and Convert to 3D.py write into a 3DS binary sequence (.bcseq).

Only the commands those scripts write are supported. Commands are big endian, and lengths, waits and programs use a
variable length number (7 bits per byte, high bit set on every byte but the last):
- note:          key (0 - 127), velocity, length
- wait:          0x80, ticks
- prg:           0x81, program
- opentrack:     0x88, track, 24-bit offset of the label from the start of the DATA block's body
- jump:          0x89, 24-bit offset of the label
- pan:           0xC0, value
- volume:        0xC1, value
- notewait_off:  0xC7, 0x00
- tempo:         0xE1, 16-bit tempo
- alloctrack:    0xFE, 16-bit track mask
- fin:           0xFF

File layout (little endian, references are a u16 type, 2 bytes of padding and a u32 offset):
- CSEQ header (0x40 bytes): magic, byte order mark 0xFEFF, header size, version 0x01000000, file size, block count 2,
  then references with sizes to the DATA (0x5000) and LABL (0x5001) blocks
- DATA block: magic, block size, the commands, one more fin (0xFF) after them, then zeros until the block size is a
  multiple of 0x20. Every track already ends with fin or jump, so the extra fin is never reached. All 101 of the
  game's own sequences in QueenSound.bcsar end their commands with it and align every block to 0x20 this way.
- LABL block: magic, block size, label count 0 (the game starts a sequence at offset 0, so no labels are needed)
"""

import re
import struct

NOTE_NAMES = [ 'cn', 'cs', 'dn', 'ds', 'en', 'fn', 'fs', 'gn', 'gs', 'an', 'as', 'bn' ]


class AssembleError( Exception ):
    pass


def variable_length( value ):
    if value < 0:
        raise AssembleError( 'negative value ' + str( value ) )
    groups = [ value & 0x7F ]
    value >>= 7
    while value:
        groups.append( ( value & 0x7F ) | 0x80 )
        value >>= 7
    return bytes( reversed( groups ) )


def note_key( name ):
    match = re.fullmatch( r"([a-g][sn])(m?)(\d+)", name )
    if match is None:
        return None
    octave = -int( match.group(3) ) if match.group(2) else int( match.group(3) )
    return ( octave + 1 ) * 12 + NOTE_NAMES.index( match.group(1) )


def assemble_commands( text ):
    """
    Returns the DATA block body for the .cseq text
    """

    lines = []
    for line in text.splitlines():
        line = line.split( ';', 1 )[0].strip()
        if line:
            lines.append( line )

    # The label offsets are only known after a first pass, and opentrack and jump always take 24 bits, so every
    # command's size is known in the first pass
    def encode( line, labels ):

        if line.endswith( ':' ):
            return b''

        command, _, arguments = line.partition( ' ' )
        values = [ value.strip() for value in arguments.split( ',' ) ] if arguments else []

        def label_offset( name ):
            if labels is None:
                return 0
            if name not in labels:
                raise AssembleError( 'unknown label ' + name )
            return labels[ name ]

        key = note_key( command )

        if key is not None:
            if not 0 <= key <= 127:
                raise AssembleError( 'note out of range: ' + line )
            return bytes( [ key, int( values[0] ) ] ) + variable_length( int( values[1] ) )
        if command == 'wait':
            return b'\x80' + variable_length( int( values[0] ) )
        if command == 'prg':
            return b'\x81' + variable_length( int( values[0] ) )
        if command == 'opentrack':
            return b'\x88' + bytes( [ int( values[0] ) ] ) + label_offset( values[1] ).to_bytes( 3, 'big' )
        if command == 'jump':
            return b'\x89' + label_offset( values[0] ).to_bytes( 3, 'big' )
        if command == 'pan':
            return bytes( [ 0xC0, int( values[0] ) ] )
        if command == 'volume':
            return bytes( [ 0xC1, int( values[0] ) ] )
        if command == 'notewait_off':
            return b'\xC7\x00'
        if command == 'tempo':
            return b'\xE1' + int( values[0] ).to_bytes( 2, 'big' )
        if command == 'alloctrack':
            return b'\xFE' + int( values[0] ).to_bytes( 2, 'big' )
        if command == 'fin':
            return b'\xFF'

        raise AssembleError( 'unsupported command: ' + line )

    labels = {}
    position = 0
    for line in lines:
        if line.endswith( ':' ):
            labels[ line[:-1] ] = position
        position += len( encode( line, None ) )

    return b''.join( encode( line, labels ) for line in lines )


def assemble( text ):
    """
    Returns the .bcseq bytes for the .cseq text
    """

    commands = assemble_commands( text ) + b'\xFF'
    data_body = commands + b'\x00' * ( -( 8 + len( commands ) ) % 0x20 )
    data_block = b'DATA' + struct.pack( '<I', 8 + len( data_body ) ) + data_body
    label_block = b'LABL' + struct.pack( '<II', 0x20, 0 ) + b'\x00' * ( 0x20 - 12 )

    header_size = 0x40
    data_offset = header_size
    label_offset = data_offset + len( data_block )
    file_size = label_offset + len( label_block )

    header = b'CSEQ' + struct.pack( '<HHII', 0xFEFF, header_size, 0x01000000, file_size )
    header += struct.pack( '<HH', 2, 0 )
    header += struct.pack( '<HHII', 0x5000, 0, data_offset, len( data_block ) )
    header += struct.pack( '<HHII', 0x5001, 0, label_offset, len( label_block ) )
    header += b'\x00' * ( header_size - len( header ) )

    return header + data_block + label_block


def assemble_file( cseq_path, bcseq_path ):
    with open( cseq_path, 'r', encoding='utf-8' ) as file:
        text = file.read()
    with open( bcseq_path, 'wb' ) as file:
        file.write( assemble( text ) )

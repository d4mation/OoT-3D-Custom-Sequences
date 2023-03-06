"""
This was determined by cross-referencing https://sites.google.com/site/deathbasketslair/zelda/ocarina-of-time/instrument-sets-and-sequences  with output from https://github.com/Gota7/Citric-Composer (To get bank IDs) and https://github.com/kr3nshaw/caesar (to confirm by listening to the MIDI)
"""
instrument_set_lookup = {
    '0x00': 5, # BANK_OCARINA
    '0x01': 0, # BANK_PLAYER(?) This is "Actor Sounds" in 64 and is unused
    '0x02': 42, # BANK_NATURE
    '0x03': 7, # BANK_ORCHE
    '0x04': 8, # BANK_YOUSEI
    '0x05': 9, # BANK_MARKET
    '0x06': 10, # BANK_TITLE
    '0x07': 11, # BANK_JAB
    '0x08': 12, # BANK_FOLK
    '0x09': 13, # BANK_MEGAMI
    '0x0A': 14, # BANK_HONOO
    '0x0B': 15, # BANK_DUNGEONBANK
    '0x0C': 16, # BANK_MORI
    '0x0D': 17, # BANK_RONRON
    '0x0E': 18, # BANK_GORON
    '0x0F': 19, # BANK_KOKIRI
    '0x10': 20, # BANK_TAMASHII
    '0x11': 21, # BANK_UMA
    '0x12': 22, # BANK_OK
    '0x13': 23, # BANK_DENSETSU
    '0x14': 24, # BANK_MATOATE
    '0x15': 25, # BANK_ZORA
    '0x16': 26, # BANK_OMISE
    '0x17': 27, # BANK_KOORI
    '0x18': 28, # BANK_YAMI
    '0x19': 29, # BANK_MIZU
    '0x1A': 0, # This one is labeled "Blank?" and unused on the 64 side. May as well assign to BANK_PLAYER as a backup
    '0x1B': 31, # BANK_GERUDO
    '0x1C': 32, # BANK_KUSURI
    '0x1D': 33, # BANK_KOTAKE
    '0x1E': 34, # BANK_GANONJYO
    '0x1F': 35, # BANK_CHIKA
    '0x20': 36, # BANK_VSGANON
    '0x21': 37, # BANK_STAFF
    '0x22': 38, # BANK_STAFF2
    '0x23': 39, # BANK_FANFARE
    '0x24': 40, # BANK_FUKUROU
}

import os
import subprocess
import struct
import shutil
import traceback

def parse_meta_file( root, file ):

    path = root + "/" + file

    with open( path, 'r', encoding='utf-8' ) as meta_file:
        lines = meta_file.readlines()

    # Strip newline(s)
    lines = [ line.rstrip() for line in lines ]

    song_name = lines[0]
    instrument_set = lines[1]
    seq_type = lines[2] if len(lines) >= 3 else 'bgm'
    groups = [ g.strip() for g in lines[3].split( ',' ) ] if len( lines ) >= 4 else []

    return song_name, instrument_set, seq_type, groups

def convert_to_3d():

    if not os.path.exists( 'data/Music' ):
        print( 'No data/Music directory found' )
        return False

    os.makedirs( './tmp', exist_ok=True )
    os.makedirs( './Custom Music', exist_ok=True )

    songs = os.walk( 'data/Music' )

    failure_count = 0

    for root, dirs, files in songs:
        
        for seq_file in files:

            if seq_file.endswith( '.meta' ):
                continue

            seq_type = 'bgm'
            seq_groups = []
            instrument_set = 0x9001

            try:

                song_name, instrument_set, seq_type, seq_groups = parse_meta_file( root, seq_file.replace( '.seq', '.meta' ) )
            
            except Exception as e:

                print( e.output )

            # Skip if already processed
            if not os.path.exists( './tmp/' + root + '/' + seq_file.replace( '.seq', '.bcseq' ) ) :

                os.makedirs( './tmp/' + root, exist_ok=True )

                try:

                    seq_to_midi = subprocess.run(
                        './seq64_console.exe --abi=4b --in="./' + root + '/' + seq_file + '" --out="./tmp/' + root + '/' + seq_file.replace( '.seq', '.mid' ) + '"',
                        check=True,
                        text=True,
                        capture_output=True
                    )

                except Exception as e:
                    print( root + '/' + seq_file )
                    print( 'seq_to_midi failure' )
                    print( e.output )
                    failure_count = failure_count + 1
                    continue

                try:

                    midi_to_sseq = subprocess.run(
                        './midi2sseq.exe "./tmp/' + root + '/' + seq_file.replace( '.seq', '.mid' ) + '" "./tmp/' + root + '/' + seq_file.replace( '.seq', '.sseq' ) + '"',
                        check=True,
                        text=True,
                        capture_output=True
                    )

                except Exception as e:
                    print( '.tmp/' + root + '/' + seq_file )
                    print( 'midi_to_sseq failure' )
                    print( e.output )
                    failure_count = failure_count + 1
                    continue

                try:

                    # We change the extension during this command to skip a step
                    sseq_to_cseq = subprocess.run(
                        './SequenceConvert.exe "./tmp/' + root + '/' + seq_file.replace( '.seq', '.sseq' ) + '" "./tmp/' + root + '/' + seq_file.replace( '.seq', '.cseq' ) + '"',
                        check=True,
                        text=True,
                        capture_output=True
                    )

                except Exception as e:
                    print( '.tmp/' + root + '/' + seq_file )
                    print( 'sseq_to_cseq failure' )
                    print( e.output )
                    failure_count = failure_count + 1
                    continue

                try:

                    cseq_to_bcseq = subprocess.run(
                        './SequenceConvert.exe "./tmp/' + root + '/' + seq_file.replace( '.seq', '.cseq' ) + '" "./tmp/' + root + '/' + seq_file.replace( '.seq', '.bcseq' ) + '"',
                        check=True,
                        text=True,
                        capture_output=True
                    )

                except Exception as e:
                    print( '.tmp/' + root + '/' + seq_file )
                    print( 'cseq_to_bcseq failure' )
                    print( e.output )
                    failure_count = failure_count + 1
                    continue

            os.makedirs( './Converted/' + root, exist_ok=True )

            shutil.copy( './tmp/' + root + '/' + seq_file.replace( '.seq', '.bcseq' ), './Converted/' + root )

            sound_bank = instrument_set_lookup.get( instrument_set )

            if sound_bank:

                cmeta = open( './tmp/' + root + '/' + seq_file.replace( '.seq', '.cmeta' ), 'wb' )

                cmeta.write( struct.pack( '1B', sound_bank ) )

                cmeta.close()

                shutil.copy( './tmp/' + root + '/' + seq_file.replace( '.seq', '.cmeta' ), './Converted/' + root )

    print( "%d failed" % failure_count )

    return True

def main():

    converted_to_3d = convert_to_3d()

    if converted_to_3d:
        print("All songs have been converted for Oot3D Rando")
        print("")
    else:
        print("An error occured moving songs")
    input("Press enter to quit.")


if __name__ == '__main__':
    main()

"""
with open( 'Lower Norfair.seq', mode='rb' ) as file:

    # Prepare Channel Offset data
    channel_offsets = {}

    file.seek( 8 )
    master_volume = file.read( 1 ).hex()

    # Prepare to parse Channel Header Offsets
    file.seek( 6 )
    
    """"""
    Each Channel Header Offset is 3 bytes long, so if the 4th byte is Hex DB, then we know we're now at Tempo Control
    """"""
    while file.seek( 3, 1 ):

        channel_header_number = file.read( 1 ).hex()

        # We've made it to Tempo Control, bail
        if channel_header_number == 'dd':
            break

        channel_header_offset = file.read( 2 ).hex()

        channel_offsets[ channel_header_number ] = channel_header_offset

        # Move back to the start of this Channel Header Offset block, so that the loop will proceed correctly to find Tempo Control
        file.seek( -3, 1 )

    tempo = file.read( 1 ).hex()

    file.seek( 1, 1 )
    timestamp = file.read( 1 ).hex()

    if ( timestamp > '7f' ):
        file.seek( -1, 1 )
        timestamp = hex( int( file.read( 2 ).hex(), 16 ) + int( '8000', 16 ) - int( '10000', 16 ) )

    file.seek( 1, 1 )
    loop_offset = file.read( 2 ).hex()

    file.seek( 1, 1 )
    disabled_channels = file.read( 2 ).hex()

    channel_commands = {}

    for channel_number, channel_offset in sorted( channel_offsets.items() ):

        channel_command = {}

        # Go to the start of the Channel Header Command
        file.seek( int( channel_offset, 16 ) )

        # Scoot one offset forward to the real data
        file.seek( 1, 1 )

        channel_command['note_layer'] = file.read( 1 ).hex()
        channel_command['music_data_offset'] = file.read( 1 ).hex()

        # Need to do the same loop as before to go through each Channel




#master_volume = hex( data[8] )

print( 'master_volume ' ) 
print( master_volume )
print( 'channel_offsets ' )
print( channel_offsets )
print( 'tempo ' ) 
print( tempo )
print( 'timestamp ' ) 
print( timestamp )
print( 'loop_offset ' ) 
print( loop_offset )
print( 'disabled_channels ' )
print( disabled_channels )
"""
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

"""
The N64 has a lot of empty Instrument indices, whereas the 3DS appears to just "collapse" those empty indices.

This List helps convert between them a bit more simply

This was created using https://sites.google.com/site/deathbasketslair/zelda/ocarina-of-time/instrument-lists as a reference
"""

# Loop through regex match of prg (\d), convert to Hex, match against lookup for correct index
instrument_list_lookup = {

    # Hyrule Field
    '0x03': {
        '0x00': 0, # Flute
        '0x01': 1, # Oboe
        '0x02': 2, # Clarinet
        '0x03': 3, # Bassoon
        '0x04': 4, # Horn
        '0x05': 5, # Trumpet
        '0x06': 6, # Trumpet
        '0x07': 7, # Tuba
        '0x08': 8, # Glockenspiel
        '0x09': False, # Empty
        '0x0A': 9, # Strings
        '0x0B': 10, # Strings
        '0x0C': 11, # Pizzicato Strings
        '0x0D': 12, # Piano
        '0x0E': 13, # Harp
        '0x0F': 14 # Xylophone
    },

    # Deku Tree
    '0x04': {
        '0x00': 0, # Pad
        '0x01': 1, # Pad
    },

    # Market
    '0x05': {
        '0x00': 0, # Koto
        '0x01': 1, # Ocarina
        '0x02': 2, # Bassoon
        '0x03': 3, # Oboe
        '0x04': False, # Empty
        '0x05': False, # Empty
        '0x06': False, # Empty
        '0x07': False, # Empty
        '0x08': False, # Empty
        '0x09': False, # Empty
        '0x0A': False, # Empty
        '0x0B': False, # Empty
        '0x0C': 4, # Pizzacato Strings
    },

    # Title Screen
    '0x06': {
        '0x00': False, # Empty,
        '0x01': 0, # Ocarina
        '0x02': False, # Empty
        '0x03': False, # Empty
        '0x04': False, # Empty
        '0x05': False, # Empty
        '0x06': False, # Empty
        '0x07': False, # Empty
        '0x08': False, # Empty
        '0x09': False, # Empty
        '0x0A': 1, # Strings
        '0x0B': 2, # Strings
        '0x0C': False, # Empty
        '0x0D': 3, # Piano
        '0x0E': 4, # Piano
    },

    # Jabu Jabu's Belly
    '0x07': {
        '0x00': 0, # Wind,
        '0x01': False, # Empty
        '0x02': 1, # Synth Strings
        '0x03': 2, # Creeking
        '0x04': 3, # Creeking 
        '0x05': False, # Empty
        '0x06': False, # Empty
        '0x07': False, # Empty
        '0x08': False, # Empty
        '0x09': False, # Empty
    },

    # Kakariko Village (guitar)
    '0x08': {
        '0x00': 0, # Harmonica
        '0x01': 1, # Guitar
        '0x02': 2, # Guitar
        '0x03': 3, # Ocarina
        '0x04': 4, # Glockenspiel
        '0x05': 5, # Accordion
        '0x06': 6, # Accordion
        '0x07': False, # Empty
        '0x08': False, # Empty
        '0x09': False, # Empty
    },

    # Fairy Fountain
    '0x09': {
        '0x00': 0, # Harp
        '0x01': 1, # Harp
        '0x02': 2, # Harp
        '0x03': 3, # Harp
        '0x04': 4, # Strings
        '0x05': 5, # Ocarina
        '0x06': 6, # Choir
        '0x07': 7, # Choir
        '0x08': 8, # Glockenspiel
        '0x09': False, # Empty
        '0x0A': 9, # Strings
        '0x0B': 10, # Strings
        '0x0C': 11, # Pizzacato Strings
    },

    # Fire Temple
    '0x0A': {
        '0x00': 0, # Islamic Chant (1.0 only?)
        '0x01': 1, # Islamic Chant (1.0 only?)
        '0x02': 2, # Islamic Chant (1.0 only?)
        '0x03': 3, # Xylophone
        '0x04': False, # Empty
        '0x05': 4, # Wind,
        '0x06': 5, # Cymbol
        '0x07': False, # Empty
        '0x08': False, # Empty
        '0x09': False, # Empty
        '0x0A': 6, # Choir (Other versions only?)
        '0x0B': 7, # Choir (Other versions only?)
        '0x0C': 8, # Choir (Other versions only?)
        '0x0D': 9, # Choir (Other versions only?)
    },

    # Dodongo's Cavern
    '0x0B': {
        '0x00': 0, # Wind
        '0x01': 1, # Sounds 1
        '0x02': 2, # Sounds 2
        '0x03': 3, # Sounds 3
    },

    # Forest Temple
    '0x0C': {
        '0x00': 0, # Pad
        '0x01': 1, # Voice thing
        '0x02': 2, # Wood chime
    },
    
    # Lon Lon Ranch
    '0x0D': {
        '0x00': 0, # Malon Voice
        '0x01': 1, # Malon Voice
        '0x02': 2, # Electric Guitar
        '0x03': 3, # Electric Guitar (high)
        '0x04': 4, # Electric Guitar (high)
        '0x05': False, # Empty
        '0x06': False, # Empty
        '0x07': False, # Empty
        '0x08': False, # Empty
        '0x09': False, # Empty
        '0x0A': False, # Empty
        '0x0B': 5, # Strings
        '0x0C': 6, # Strings
        '0x0D': 7, # Violin
        '0x0E': 8, # Violin
        '0x0F': 9, # Bell
    },

    # Goron City
    '0x0E': {
        '0x00': 0, # Drum
        '0x01': 1, # Clap
        '0x02': 2, # This is labeled as "lolwut". I assume this is an instrument and not an empty space?
        '0x03': 3, # Xylophone
        '0x04': 4, # Xylophone
    },

    # Kokiri Forest
    '0x0F': {
        '0x00': 0, # Flute
        '0x01': 1, # Oboe
        '0x02': 2, # Clarinet
        '0x03': 3, # Bassoon
        '0x04': 4, # Horn
        '0x05': False, # Empty
        '0x06': False, # Empty
        '0x07': False, # Empty
        '0x08': 5, # Glockenspiel
        '0x09': False, # Empty
        '0x0A': 6, # Strings
        '0x0B': 7, # Strings
        '0x0C': 8, # Pizzacato Strings
        '0x0D': 9, # Harspichord
        '0x0E': 10, # Harp
        '0x0F': 11, # Xylophone
    },

    # Spirit Temple
    '0x10': {
        '0x00': 0, # Voice pad
        '0x01': 1, # Synth
        '0x02': 2, # Egyptian flute
        '0x03': 3, # Clap
        '0x04': 4, # Synth
        '0x05': 5, # Egyptian flute
        '0x06': False, # Empty
        '0x07': False, # Empty
        '0x08': False, # Empty
        '0x09': False, # Empty
    },
    
    # Horse Race
    '0x11': {
        '0x00': 0, # Banjo
        '0x01': 1, # Banjo
        '0x02': False, # Empty
        '0x03': False, # Empty
        '0x04': False, # Empty
        '0x05': 2, # Bass guitar
        '0x06': 3, # Harmonica
        '0x07': 4, # Guitar
        '0x08': False, # Empty
        '0x09': False, # Empty
        '0x0A': False, # Empty
        '0x0B': False, # Empty
        '0x0C': False, # Empty
        '0x0D': 5, # Violin
        '0x0E': 6, # Violin
    },

    # Warp Songs
    '0x12': {
        '0x00': 0, # Harp
        '0x01': 1, # Harp
        '0x02': 2, # Harp
        '0x03': 3, # Harp
        '0x04': 4, # Strings
        '0x05': 5, # Ocarina
        '0x06': False, # Empty
        '0x07': False, # Empty
        '0x08': 6, # Glockenspiel
        '0x09': False, # Empty
        '0x0A': 7, # Strings
        '0x0B': 8, # Strings
        '0x0C': 9, # Pizzacato Strings
    },

    # Goddess Cutscene
    '0x13': {
        '0x00': 0, # Choir
        '0x01': 1, # Choir
        '0x02': 2, # Choir
        '0x03': 3, # Glockenspiel
    },

    # Shooting Gallery
    '0x14': {
        '0x00': 0, # Flute
        '0x01': 1, # Clarinet
        '0x02': 2, # Clarinet
        '0x03': 3, # Accordion
        '0x04': 4, # Glockenspiel
        '0x05': False, # Empty
        '0x06': False, # Empty
        '0x07': False, # Empty
        '0x08': False, # Empty
        '0x09': False, # Empty
    },
    
    # Zora's Domain
    '0x15': {
        '0x00': 0, # Steel Drum
        '0x01': 1, # Voice Pad
        '0x02': 2, # Guitar
        '0x03': False, # Empty
        '0x04': False, # Empty
        '0x05': False, # Empty
        '0x06': False, # Empty
        '0x07': False, # Empty
        '0x08': False, # Empty
        '0x09': False, # Empty
    },

    # Shop
    '0x16': {
        '0x00': 0, # Guitar
        '0x01': 1, # Accordion
        '0x02': 2, # Bass guitar
        '0x03': 3, # Trumpet
        '0x04': 4, # Trumpet (high)
        '0x05': False, # Empty
        '0x06': False, # Empty
        '0x07': False, # Empty
        '0x08': False, # Empty
        '0x09': False, # Empty
        '0x0A': 5, # Drum
    },

    # Ice Cavern
    '0x17': {
        '0x00': 0, # Bell Pad
        '0x01': 1, # Bell Pad
        '0x02': 2, # Wind
        '0x03': 3, # Bell Pad
    },

    # Shadow Temple
    '0x18': {
        '0x00': 0, # Drum
        '0x01': 1, # Wind
        '0x02': 2, # Sounds 1
        '0x03': 3, # Choir
        '0x04': 4, # Choir (high)
        '0x05': False, # Empty
        '0x06': 5, # Islamic chant
        '0x07': 6, # Sounds 2
        '0x08': 7, # Harpsichord
    },

    # Water Temple
    '0x19': {
        '0x00': 0, # Flute
        '0x01': 1, # Wind chime
        '0x02': False, # Empty
        '0x03': False, # Empty
        '0x04': 2, # Bell pad
        '0x05': 3, # Wood chime
        '0x06': 4, # Voice pad
        '0x07': 5, # Koto
    },

    # Unused
    '0x1A': {
        '0x00': False, # Empty
        '0x01': False, # Empty
        '0x02': False, # Empty
        '0x03': False, # Empty
        '0x04': False, # Empty
        '0x05': False, # Empty
        '0x06': False, # Empty
        '0x07': False, # Empty
        '0x08': False, # Empty
        '0x09': False, # Empty
        '0x0A': False, # Empty
        '0x0B': False, # Empty
        '0x0C': False, # Empty
        '0x0D': 0, # Piano
        '0x0E': 1, # Piano
    },

    # Gerudo Valley
    '0x1B': {
        '0x00': 0, # Trumpet
        '0x01': 1, # Trumpet (low)
        '0x02': 2, # Guitar
        '0x03': 3, # Guitar
        '0x04': False, # Empty
        '0x05': 4, # Bass guitar
        '0x06': False, # Empty
        '0x07': 5, # Guitar
        '0x08': False, # Empty
        '0x09': False, # Empty
        '0x0A': 6, # Clap
        '0x0B': 7, # Clap
    },

    # Lakeside Laboratory
    '0x1C': {
        '0x00': 0, # Koto
        '0x01': 1, # Drum
        '0x02': False, # Empty
        '0x03': 2, # Drum 2
        '0x04': 3, # Wind chime
    },

    # Kotake and Koume
    '0x1D': {
        '0x00': 0, # Koto
        '0x01': 1, # Drum
        '0x02': False, # Empty
        '0x03': False, # Empty
        '0x04': False, # Empty
        '0x05': 2, # Flute
        '0x06': False, # Empty
        '0x07': 3, # Flute
        '0x08': False, # Empty
        '0x09': False, # Empty
        '0x0A': 4, # Strings
        '0x0B': 5, # Strings
    },

    # Ganon's Castle (Organ)
    '0x1E': {
        '0x00': 0, # Organ
        '0x01': 1, # Organ
        '0x02': 2, # Organ
        '0x03': False, # Empty
        '0x04': 3, # Horn
    },

    # Inside Ganon's Castle
    '0x1F': {
        '0x00': False, # Empty
        '0x01': 0, # Wind
        '0x02': 1, # Sounds 1
        '0x03': 2, # Choir
        '0x04': 3, # Piano
        '0x05': 4, # Piano
        '0x06': False, # Empty
        '0x07': 5, # Sounds 2
    },

    # Ganondorf Battle
    '0x20': {
        '0x00': 0, # Flute
        '0x01': 1, # Choir
        '0x02': 2, # Choir (low)
        '0x03': False, # Empty
        '0x04': 3, # Horn
        '0x05': 4, # Trumpet
        '0x06': 5, # Trumpet (low)
        '0x07': 6, # Tuba
        '0x08': False, # Empty
        '0x09': False, # Empty
        '0x0A': 7, # Strings
        '0x0B': 8, # Strings
        '0x0C': False, # Empty
        '0x0D': 9, # Piano
        '0x0E': False, # Empty
        '0x0F': 10, # Xylophone
    },

    # Ending Sequence 1
    '0x21': {
        '0x00': 0, # Malon Voice
        '0x01': 1, # Malon Voice
        '0x02': 2, # Clarinet
        '0x03': False, # Empty
        '0x04': 3, # Horn
        '0x05': 4, # Oboe
        '0x06': 5, # Harp
        '0x07': 6, # Violin 
        '0x08': 7, # Glockenspiel
        '0x09': False, # Empty
        '0x0A': 8, # Strings
        '0x0B': 9, # Strings
        '0x0C': False, # Empty
        '0x0D': 10, # Bell
        '0x0E': 11, # Harp
        '0x0F': 12, # Choir
    },

    # Ending Sequence 2
    '0x22': {
        '0x00': 0, # Koto
        '0x01': 1, # Ocarina
        '0x02': 2, # Bassoon
        '0x03': 3, # Oboe
        '0x04': 4, # Choir
        '0x05': 5, # Tamourine
        '0x06': 6, # Harp
        '0x07': 7, # Glockenspiel
        '0x08': 8, # Malon Voice
        '0x09': False, # Empty
        '0x0A': 9, # Strings
        '0x0B': 10, # Strings
        '0x0C': 11, # Pizzicato Strings
        '0x0D': 12, # Horn
        '0x0E': 13, # Choir
        '0x0F': 14, # This is labeled as "lolwut". I assume this is an instrument and not an empty space?
    },

    # Fanfares
    '0x23': {
        '0x00': False, # Empty
        '0x01': False, # Empty
        '0x02': False, # Empty
        '0x03': False, # Empty
        '0x04': False, # Empty
        '0x05': 0, # Trumpet
        '0x06': 1, # Trumpet (low)
        '0x07': 2, # Tuba
        '0x08': 3, # Glockenspiel
        '0x09': False, # Empty
        '0x0A': 4, # Strings
        '0x0B': 5, # Strings
        '0x0C': False, # Empty
        '0x0D': False, # Empty
        '0x0E': 6, # Harp
    },

    # Owl
    '0x24': {
        '0x00': False, # Empty
        '0x01': 0, # Oboe
        '0x02': False, # Empty
        '0x03': 1, # Bassoon
        '0x04': False, # Empty
        '0x05': False, # Empty
        '0x06': False, # Empty
        '0x07': False, # Empty
        '0x08': False, # Empty
        '0x09': False, # Empty
        '0x0A': 2, # Strings
        '0x0B': 3, # Strings
        '0x0C': 4, # Pizzicato Strings
        '0x0D': False, # Empty
        '0x0E': 5, # Harp
    }

}

import os
import subprocess
import struct
import shutil
import traceback
import fileinput
import sys
import re

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

                instrument_set = "0x{:02X}".format( int( instrument_set, 16 ) )
            
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

                    for line in fileinput.input( './tmp/' + root + '/' + seq_file.replace( '.seq', '.cseq' ), inplace=True ):

                        match = re.search( r"prg (\d+)", line )

                        if not match:
                            print( line.rstrip() )
                            continue

                        instrument_index = match.group(1)

                        new_instrument_index = instrument_list_lookup.get( instrument_set ).get( "0x{:02X}".format( int( instrument_index ) ) )

                        if not new_instrument_index:
                            print( line.rstrip() )
                            continue

                        print( line.replace( instrument_index, str( new_instrument_index ) ).rstrip() )

                    fileinput.close()

                except Exception as e:
                    print( '.tmp/' + root + '/' + seq_file, file=sys.stderr )
                    print( 'cseq instrument fix failure', file=sys.stderr )
                    print( e, file=sys.stderr )
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
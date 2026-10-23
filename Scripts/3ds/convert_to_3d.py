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
    '0x1A': 30, # BANK_SARIA. Unused on the 64 side, but its two pianos match the two instruments in BANK_SARIA
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
    # 3DS indices match the 3DS NA_BGM_FIRE_DUNGEON sequence. Slots 0x0C and 0x0D are the same instrument, which the 3DS has once.
    '0x0A': {
        '0x00': False, # Chant (N64 1.0 and 1.1 only, see instruments_missing_on_3ds)
        '0x01': False, # Chant (N64 1.0 and 1.1 only, see instruments_missing_on_3ds)
        '0x02': False, # Chant (N64 1.0 and 1.1 only, see instruments_missing_on_3ds)
        '0x03': 3, # Xylophone
        '0x04': False, # Empty
        '0x05': 4, # Wind,
        '0x06': 5, # Cymbol
        '0x07': False, # Empty
        '0x08': False, # Empty
        '0x09': False, # Empty
        '0x0A': 1, # Choir (not in N64 1.0 and 1.1)
        '0x0B': 2, # Choir (not in N64 1.0 and 1.1)
        '0x0C': 0, # Choir (not in N64 1.0 and 1.1)
        '0x0D': 0, # Choir (not in N64 1.0 and 1.1)
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
    # The 3DS bank has these in a different order, found by matching each instrument's key ranges, sample lengths and pitch
    '0x10': {
        '0x00': 5, # Voice pad
        '0x01': 0, # Synth
        '0x02': 1, # Egyptian flute
        '0x03': 2, # Clap
        '0x04': 3, # Synth
        '0x05': 4, # Egyptian flute
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
    # Slots 0x02 and 0x03 are empty in the OoT decomp (assets/xml/audio/soundfonts/Soundfont_18.xml), and BANK_OK has 8 instruments
    '0x12': {
        '0x00': 0, # Harp
        '0x01': 1, # Harp
        '0x02': False, # Empty
        '0x03': False, # Empty
        '0x04': 2, # Strings
        '0x05': 3, # Ocarina
        '0x06': False, # Empty
        '0x07': False, # Empty
        '0x08': 4, # Glockenspiel
        '0x09': False, # Empty
        '0x0A': 5, # Strings
        '0x0B': 6, # Strings
        '0x0C': 7, # Pizzacato Strings
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
    # The 3DS bank has these in a different order, found by matching each instrument's key ranges, sample lengths and pitch
    '0x19': {
        '0x00': 0, # Flute
        '0x01': 5, # Wind chime
        '0x02': False, # Empty
        '0x03': False, # Empty
        '0x04': 1, # Bell pad
        '0x05': 2, # Wood chime
        '0x06': 3, # Voice pad
        '0x07': 4, # Koto
    },

    # Unused on the N64. Its two pianos match the two instruments in BANK_SARIA.
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
    # The 3DS bank has these in a different order, found by matching each instrument's key ranges, sample lengths and pitch
    '0x1C': {
        '0x00': 0, # Koto
        '0x01': 1, # Drum
        '0x02': False, # Empty
        '0x03': 3, # Drum 2
        '0x04': 2, # Wind chime
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
    # 3DS indices match the 3DS NA_BGM_UNDERGROUND sequence
    '0x1F': {
        '0x00': False, # Empty
        '0x01': 0, # Wind
        '0x02': 1, # Sounds 1
        '0x03': 2, # Choir
        '0x04': 4, # Piano
        '0x05': 5, # Piano
        '0x06': False, # Empty
        '0x07': 3, # Sounds 2
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
    # 3DS indices match the 3DS NA_BGM_STAFF_1 and NA_BGM_STAFF_3 sequences. Slot 0x0D matches by key ranges, sample lengths and pitch.
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
        '0x0D': 12, # Bell
        '0x0E': 10, # Harp
        '0x0F': 11, # Choir
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

"""
Instruments that exist on the N64 but have no 3DS equivalent. Songs that use them are skipped.

The Fire Temple chant (0x00 - 0x02) is only in N64 version 1.0. Those slots are empty in the MQ debug ROM, and no 3DS
bank has a matching instrument.
"""
instruments_missing_on_3ds = {
    '0x0A': [ 0x00, 0x01, 0x02 ],
}

"""
3DS drum kit program and key for each N64 drum, generated by generate_lookup_tables.py from the MQ debug ROM and the
3DS QueenSound.bcsar banks.

Each N64 drum maps to the 3DS key that plays the same sample at the nearest pitch, up to 3 semitones away. Many N64 drum
pitches do not exist on the 3DS, and the 3DS game's own sequences also play those drums 1 - 3 semitones off. See
PITCH_TOLERANCE in generate_lookup_tables.py for the numbers behind this. None means no 3DS key is within 3 semitones,
and songs that play that drum are skipped.
"""
drum_note_lookup = {
    # BANK_ORCHE
    '0x03': {
        'program': 15,
        'notes': {
            0: None, 1: None, 2: 27, 3: 27, 4: 27, 5: 27, 6: 26, 7: 25,
            8: 24, 9: 23, 10: 22, 11: 21, 12: 20, 13: 19, 14: 18, 15: 17,
            16: 28, 17: 28, 18: 28, 19: 28, 20: 28, 21: 44, 22: 44, 23: 44,
            24: 44, 25: 43, 26: 42, 27: 41, 28: 40, 29: 39, 30: 38, 31: 37,
            32: 36, 33: None, 34: 45, 35: 45, 36: 45, 37: 45, 38: 45, 39: 75,
            40: 74, 41: 73, 42: 72, 43: 71, 44: 70, 45: 69, 46: 68, 47: 67,
            48: 66, 49: 65, 50: 64, 51: 63, 52: 62, 53: 61, 54: 60, 55: 59,
            56: 58, 57: 57, 58: 56, 59: 55, 60: 54, 61: 53, 62: 52, 63: 51,
        },
    },
    # BANK_MARKET
    '0x05': {
        'program': 5,
        'notes': {
            0: 0, 1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7,
            8: 8, 9: 9, 10: 10, 11: 11, 12: 12, 13: 13, 14: 14, 15: 15,
            16: 16, 17: 17, 18: 18, 19: 19, 20: 20, 21: 21, 22: 22, 23: 23,
            24: 24, 25: 25, 26: 26, 27: 53, 28: 53, 29: 55, 30: 55, 31: 56,
            32: 56, 33: 56, 34: 56, 35: None, 36: None, 37: None, 38: None, 39: None,
            40: None, 41: None, 42: None, 43: None, 44: None, 45: None, 46: None, 47: None,
            48: None, 49: None, 50: None, 51: None, 52: None, 53: None, 54: None, 55: None,
            56: None, 57: None, 58: None, 59: None, 60: None, 61: None, 62: None, 63: None,
        },
    },
    # BANK_JAB
    '0x07': {
        'program': 4,
        'notes': {
            0: None, 1: None, 2: None, 3: None, 4: None, 5: None, 6: None, 7: None,
            8: None, 9: None, 10: None, 11: 32, 12: 32, 13: 32, 14: 32, 15: 31,
            16: 30, 17: 33, 18: 33, 19: 33, 20: 33, 21: None, 22: None, 23: None,
            24: None, 25: None, 26: None, 27: None, 28: None, 29: None, 30: None, 31: None,
            32: None, 33: None, 34: None, 35: None, 36: None, 37: None, 38: None, 39: None,
            40: None, 41: None, 42: None, 43: None, 44: None, 45: None, 46: None, 47: None,
            48: None, 49: None, 50: None, 51: None, 52: None, 53: None, 54: None, 55: None,
            56: None, 57: None, 58: None, 59: None, 60: None, 61: None, 62: None, 63: None,
        },
    },
    # BANK_FOLK
    '0x08': {
        'program': 7,
        'notes': {
            0: None, 1: None, 2: None, 3: None, 4: None, 5: None, 6: None, 7: None,
            8: None, 9: None, 10: None, 11: None, 12: None, 13: None, 14: None, 15: None,
            16: None, 17: None, 18: None, 19: None, 20: None, 21: None, 22: None, 23: 52,
            24: 52, 25: 52, 26: 52, 27: 53, 28: 53, 29: 55, 30: 56, 31: 56,
            32: 56, 33: 56, 34: None, 35: None, 36: None, 37: None, 38: None, 39: None,
            40: None, 41: None, 42: None, 43: None, 44: None, 45: None, 46: None, 47: None,
            48: None, 49: None, 50: None, 51: None, 52: None, 53: None, 54: None, 55: None,
            56: None, 57: None, 58: None, 59: None, 60: None, 61: None, 62: None, 63: None,
        },
    },
    # BANK_MEGAMI
    '0x09': {
        'program': 12,
        'notes': {
            0: None, 1: None, 2: 27, 3: 27, 4: 27, 5: 27, 6: 26, 7: 25,
            8: 24, 9: 23, 10: 22, 11: 21, 12: 20, 13: 19, 14: 18, 15: 17,
            16: 28, 17: 28, 18: 28, 19: 28, 20: 28, 21: 44, 22: 44, 23: 44,
            24: 44, 25: 43, 26: 42, 27: 41, 28: 40, 29: 39, 30: 38, 31: 37,
            32: 36, 33: None, 34: None, 35: None, 36: 75, 37: 75, 38: 75, 39: 75,
            40: 74, 41: 73, 42: 72, 43: 71, 44: 70, 45: 69, 46: 68, 47: 67,
            48: 66, 49: 65, 50: 64, 51: 63, 52: 62, 53: 61, 54: 60, 55: 59,
            56: 58, 57: 57, 58: 56, 59: 55, 60: 54, 61: 53, 62: 52, 63: 51,
        },
    },
    # BANK_HONOO
    '0x0A': {
        'program': 6,
        'notes': {
            0: 11, 1: 12, 2: 13, 3: 14, 4: 15, 5: 16, 6: 17, 7: 18,
            8: 19, 9: 20, 10: 21, 11: 22, 12: 23, 13: 24, 14: 25, 15: 26,
            16: 27, 17: 50, 18: 49, 19: 48, 20: 47, 21: 46, 22: 45, 23: 44,
            24: 43, 25: 42, 26: 41, 27: 40, 28: 40, 29: 40, 30: 40, 31: None,
            32: None, 33: None, 34: None, 35: None, 36: None, 37: None, 38: None, 39: None,
            40: None, 41: None, 42: None, 43: None, 44: None, 45: None, 46: None, 47: None,
            48: None, 49: None, 50: None, 51: None, 52: None, 53: None, 54: None, 55: None,
            56: None, 57: None, 58: None, 59: None, 60: None, 61: None, 62: None, 63: None,
        },
    },
    # BANK_TAMASHII
    '0x10': {
        'program': 6,
        'notes': {
            0: None, 1: None, 2: None, 3: None, 4: 57, 5: 57, 6: 57, 7: 57,
            8: 56, 9: 55, 10: 54, 11: 53, 12: 52, 13: 51, 14: 50, 15: 49,
            16: 48, 17: 47, 18: 46, 19: 45, 20: 44, 21: 43, 22: 42, 23: 41,
            24: 40, 25: 39, 26: 38, 27: 37, 28: 36, 29: 35, 30: 34, 31: 33,
            32: 32, 33: 31, 34: 82, 35: 81, 36: 80, 37: 79, 38: 78, 39: 77,
            40: 76, 41: 75, 42: 74, 43: 73, 44: 72, 45: 71, 46: 70, 47: 69,
            48: 68, 49: 67, 50: 66, 51: 65, 52: 64, 53: 63, 54: 62, 55: 61,
            56: 60, 57: 59, 58: 58, 59: 58, 60: 58, 61: 58, 62: None, 63: None,
        },
    },
    # BANK_OK
    '0x12': {
        'program': 8,
        'notes': {
            0: None, 1: None, 2: 27, 3: 27, 4: 27, 5: 27, 6: 26, 7: 25,
            8: 24, 9: 23, 10: 22, 11: 21, 12: 20, 13: 19, 14: 18, 15: 17,
            16: 28, 17: 28, 18: 28, 19: 28, 20: 28, 21: 44, 22: 44, 23: 44,
            24: 44, 25: 43, 26: 42, 27: 41, 28: 40, 29: 39, 30: 38, 31: 37,
            32: 36, 33: None, 34: None, 35: None, 36: None, 37: None, 38: None, 39: None,
            40: None, 41: None, 42: None,
        },
    },
    # BANK_MATOATE
    '0x14': {
        'program': 5,
        'notes': {
            0: None, 1: None, 2: 27, 3: 27, 4: 27, 5: 27, 6: 26, 7: 25,
            8: 24, 9: 23, 10: 22, 11: 21, 12: 20, 13: 19, 14: 18, 15: 17,
            16: 28, 17: 28, 18: 28, 19: 28, 20: 28, 21: 44, 22: 44, 23: 44,
            24: 44, 25: 43, 26: 42, 27: 41, 28: 40, 29: 39, 30: 38, 31: 37,
            32: 36, 33: None, 34: None, 35: None, 36: 75, 37: 75, 38: 75, 39: 75,
            40: 74, 41: 73, 42: 72, 43: 71, 44: 70, 45: 69, 46: 68, 47: 67,
            48: 66, 49: 65, 50: 64, 51: 63, 52: 62, 53: 61, 54: 60, 55: 59,
            56: 58, 57: 57, 58: 56, 59: 55, 60: 54, 61: 53, 62: 52, 63: 51,
        },
    },
    # BANK_ZORA
    '0x15': {
        'program': 3,
        'notes': {
            0: None, 1: None, 2: None, 3: None, 4: None, 5: None, 6: None, 7: 44,
            8: 44, 9: 44, 10: 44, 11: 43, 12: 42, 13: 41, 14: 24, 15: 39,
            16: 38, 17: 37, 18: 36, 19: 35, 20: 34, 21: 45, 22: 45, 23: 45,
            24: 45, 25: 46, 26: 46, 27: 46, 28: 46, 29: 46, 30: 47, 31: 47,
            32: 47, 33: 47, 34: 47, 35: 48, 36: 48, 37: 48, 38: 48, 39: 63,
            40: 64, 41: 64, 42: 64, 43: None, 44: None, 45: None, 46: None, 47: None,
            48: None, 49: None, 50: None, 51: None, 52: None, 53: None, 54: None, 55: None,
            56: None, 57: None, 58: None, 59: None, 60: 84, 61: 84, 62: 84, 63: 84,
        },
    },
    # BANK_OMISE
    '0x16': {
        'program': 6,
        'notes': {
            0: None, 1: None, 2: None, 3: None, 4: None, 5: None, 6: None, 7: 44,
            8: 44, 9: 44, 10: 44, 11: 43, 12: 42, 13: 41, 14: 40, 15: 39,
            16: 38, 17: 37, 18: 36, 19: 35, 20: 34, 21: None, 22: None, 23: None,
            24: None, 25: None, 26: None, 27: 47, 28: 47, 29: 47, 30: 47, 31: 47,
            32: 45, 33: 45, 34: 45, 35: 45, 36: 49, 37: 49, 38: 46, 39: 63,
            40: 64, 41: 64, 42: 64, 43: 64, 44: 64, 45: None, 46: None, 47: None,
            48: None, 49: None, 50: None, 51: None, 52: None, 53: None, 54: None, 55: None,
            56: None, 57: None, 58: None, 59: None, 60: 84, 61: 84, 62: 84, 63: 84,
        },
    },
    # BANK_KOTAKE
    '0x1D': {
        'program': 6,
        'notes': {
            0: None, 1: None, 2: None, 3: None, 4: 57, 5: 57, 6: 57, 7: 57,
            8: 56, 9: 55, 10: 54, 11: 53, 12: 52, 13: 51, 14: 50, 15: 49,
            16: 48, 17: 47, 18: 46, 19: 45, 20: 44, 21: 43, 22: 42, 23: 41,
            24: 40, 25: 39, 26: 38, 27: 37, 28: 36, 29: 35, 30: 34, 31: 33,
            32: 32, 33: 31, 34: 82, 35: 81, 36: 80, 37: 79, 38: 78, 39: 77,
            40: 76, 41: 75, 42: 74, 43: 73, 44: 72, 45: 71, 46: 70, 47: 69,
            48: 68, 49: 67, 50: 66, 51: 65, 52: 64, 53: 63, 54: 62, 55: 61,
            56: 60, 57: 59, 58: 58, 59: 58, 60: 58, 61: 58, 62: None, 63: None,
        },
    },
    # BANK_VSGANON
    '0x20': {
        'program': 11,
        'notes': {
            0: None, 1: None, 2: 27, 3: 27, 4: 27, 5: 27, 6: 26, 7: 25,
            8: 24, 9: 23, 10: 22, 11: 21, 12: 20, 13: 19, 14: 18, 15: 17,
            16: 28, 17: 28, 18: 28, 19: 28, 20: 28, 21: 44, 22: 44, 23: 44,
            24: 44, 25: 43, 26: 42, 27: 41, 28: 40, 29: 39, 30: 38, 31: 37,
            32: 36, 33: 45, 34: 45, 35: 45, 36: 45, 37: 75, 38: 75, 39: 76,
            40: 74, 41: 73, 42: 72, 43: 71, 44: 70, 45: 69, 46: 68, 47: 67,
            48: 66, 49: 65, 50: 64, 51: 63, 52: 62, 53: 61, 54: 60, 55: 59,
            56: 58, 57: 57, 58: 56, 59: 55, 60: 54, 61: 53, 62: 52, 63: 51,
        },
    },
    # BANK_STAFF
    '0x21': {
        'program': 13,
        'notes': {
            0: None, 1: None, 2: 27, 3: 27, 4: 27, 5: 27, 6: 26, 7: 25,
            8: 24, 9: 23, 10: 22, 11: 21, 12: 20, 13: 19, 14: 18, 15: 17,
            16: 28, 17: 28, 18: 28, 19: 28, 20: 28, 21: 44, 22: 44, 23: 44,
            24: 44, 25: 43, 26: 42, 27: 41, 28: 40, 29: 39, 30: 38, 31: 37,
            32: 36, 33: None, 34: None, 35: None, 36: 75, 37: 75, 38: 75, 39: 75,
            40: 74, 41: 73, 42: 72, 43: 71, 44: 70, 45: 69, 46: 68, 47: 67,
            48: 66, 49: 65, 50: 64, 51: 63, 52: 62, 53: 61, 54: 60, 55: 59,
            56: 58, 57: 57, 58: 56, 59: 55, 60: 54, 61: 53, 62: 52, 63: 51,
        },
    },
    # BANK_STAFF2
    '0x22': {
        'program': 15,
        'notes': {
            0: None, 1: None, 2: 27, 3: 27, 4: 27, 5: 27, 6: 26, 7: 25,
            8: 24, 9: 23, 10: 22, 11: 21, 12: 20, 13: 19, 14: 18, 15: 17,
            16: 28, 17: 28, 18: 28, 19: 28, 20: 28, 21: 44, 22: 44, 23: 44,
            24: 44, 25: 43, 26: 42, 27: 41, 28: 40, 29: 39, 30: 38, 31: 37,
            32: 36, 33: None, 34: None, 35: None, 36: 75, 37: 75, 38: 75, 39: 75,
            40: 74, 41: 73, 42: 72, 43: 71, 44: 70, 45: 69, 46: 68, 47: 67,
            48: 66, 49: 65, 50: 64, 51: 63, 52: 62, 53: 61, 54: 60, 55: 59,
            56: 58, 57: 57, 58: 56, 59: 55, 60: 54, 61: 53, 62: 52, 63: 51,
        },
    },
    # BANK_FANFARE
    '0x23': {
        'program': 7,
        'notes': {
            0: None, 1: None, 2: 27, 3: 27, 4: 27, 5: 27, 6: 26, 7: 25,
            8: 24, 9: 23, 10: 22, 11: 21, 12: 20, 13: 19, 14: 18, 15: 17,
            16: 28, 17: 28, 18: 28, 19: 28, 20: 28, 21: 44, 22: 44, 23: 44,
            24: 44, 25: 43, 26: 42, 27: 41, 28: 40, 29: 39, 30: 38, 31: 37,
            32: 36, 33: None, 34: None, 35: None, 36: 75, 37: 75, 38: 75, 39: 75,
            40: 74, 41: 73, 42: 72, 43: 71, 44: 70, 45: 69, 46: 68, 47: 67,
            48: 66, 49: 65, 50: 64, 51: 63, 52: 62, 53: 61, 54: 60, 55: 59,
            56: 58, 57: 57, 58: 56, 59: 55, 60: 54, 61: 53, 62: 52, 63: 51,
        },
    },
}

"""
The loop end and tuning of every N64 instrument and drum sample, generated by generate_lookup_tables.py from the MQ
debug ROM. Instruments are { slot: ( normal range low, normal range high, low, normal, high ) }, where low, normal and
high are the ( loop end, tuning ) of the sample for notes below, inside and above the normal range.

n64_to_cseq.py uses these to time a note with a delay of 0, which plays its whole sample.
"""
sample_lookup = {
    '0x03': {
        'instruments': {
            0: ( 0, 127, None, ( 32069, 0.3337100148200989 ), None ),
            1: ( 0, 127, None, ( 8456, 0.39684998989105225 ), None ),
            2: ( 0, 127, None, ( 5408, 0.5 ), None ),
            3: ( 0, 127, None, ( 9533, 2.3784139156341553 ), None ),
            4: ( 0, 127, None, ( 55209, 1.0 ), None ),
            5: ( 0, 127, None, ( 25395, 0.5 ), None ),
            6: ( 0, 127, None, ( 34693, 0.6674200296401978 ), None ),
            7: ( 0, 127, None, ( 21545, 3.1748030185699463 ), None ),
            8: ( 0, 127, None, ( 38000, 0.5297319889068604 ), None ),
            10: ( 30, 40, ( 36435, 4.0 ), ( 32149, 1.2599209547042847 ), ( 27693, 0.6299610137939453 ) ),
            11: ( 30, 40, ( 36435, 4.0 ), ( 32149, 1.2599209547042847 ), ( 27693, 0.6299610137939453 ) ),
            12: ( 0, 43, None, ( 23065, 2.1189260482788086 ), ( 23852, 0.5612310171127319 ) ),
            13: ( 24, 44, ( 55394, 2.317720890045166 ), ( 69011, 1.0 ), ( 47587, 0.5 ) ),
            14: ( 0, 47, None, ( 27578, 0.75 ), ( 31472, 0.375 ) ),
            15: ( 0, 50, None, ( 17548, 0.8908990025520325 ), ( 15237, 0.44544899463653564 ) ),
        },
        'drums': {
            0: ( 35313, 0.3858463168144226 ), 1: ( 35313, 0.40879026055336 ), 2: ( 35313, 0.4330981969833374 ), 3: ( 35313, 0.45885127782821655 ),
            4: ( 35313, 0.4861360788345337 ), 5: ( 35313, 0.5150433778762817 ), 6: ( 35313, 0.545669436454773 ), 7: ( 35313, 0.5781167149543762 ),
            8: ( 35313, 0.6124930381774902 ), 9: ( 35313, 0.648914098739624 ), 10: ( 35313, 0.6875 ), 11: ( 35313, 0.7283807992935181 ),
            12: ( 35313, 0.7716926336288452 ), 13: ( 35313, 0.8175798058509827 ), 14: ( 35313, 0.8661956787109375 ), 15: ( 35313, 0.9177025556564331 ),
            16: ( 18001, 1.0 ), 17: ( 18001, 1.0594630241394043 ), 18: ( 18001, 1.0594630241394043 ), 19: ( 18001, 1.1224620342254639 ),
            20: ( 18001, 1.1892069578170776 ), 21: ( 61617, 0.6674200296401978 ), 22: ( 61617, 0.7071070075035095 ), 23: ( 61617, 0.7491539716720581 ),
            24: ( 61617, 0.7937009930610657 ), 25: ( 61617, 0.8408970236778259 ), 26: ( 61617, 0.8908990025520325 ), 27: ( 61617, 0.9438750147819519 ),
            28: ( 61617, 1.0 ), 29: ( 61617, 1.0594630241394043 ), 30: ( 61617, 1.1224620342254639 ), 31: ( 61617, 1.1892069578170776 ),
            32: ( 61617, 1.2599209547042847 ), 33: ( 59996, 0.35355299711227417 ), 34: ( 59996, 0.37457698583602905 ), 35: ( 59996, 0.39684998989105225 ),
            36: ( 59996, 0.4204480051994324 ), 37: ( 59996, 0.44544899463653564 ), 38: ( 59996, 0.47193700075149536 ), 39: ( 59996, 0.5 ),
            40: ( 59996, 0.5297319889068604 ), 41: ( 59996, 0.5612310171127319 ), 42: ( 59996, 0.5946040153503418 ), 43: ( 59996, 0.6299610137939453 ),
            44: ( 59996, 0.6674200296401978 ), 45: ( 59996, 0.7071070075035095 ), 46: ( 59996, 0.7491539716720581 ), 47: ( 59996, 0.7937009930610657 ),
            48: ( 59996, 0.8408970236778259 ), 49: ( 59996, 0.8908990025520325 ), 50: ( 59996, 0.9438750147819519 ), 51: ( 59996, 1.0 ),
            52: ( 59996, 1.0594630241394043 ), 53: ( 59996, 1.1224620342254639 ), 54: ( 59996, 1.1892069578170776 ), 55: ( 59996, 1.2599209547042847 ),
            56: ( 59996, 1.3348400592803955 ), 57: ( 59996, 1.414214015007019 ), 58: ( 59996, 1.4983069896697998 ), 59: ( 59996, 1.587401032447815 ),
            60: ( 59996, 1.681792974472046 ), 61: ( 59996, 1.781798005104065 ), 62: ( 59996, 1.8877489566802979 ), 63: ( 59996, 2.0 ),
        },
    },
    '0x04': {
        'instruments': {
            0: ( 0, 127, None, ( 42205, 1.3348400592803955 ), None ),
            1: ( 0, 127, None, ( 42205, 1.3348400592803955 ), None ),
        },
        'drums': {
        },
    },
    '0x05': {
        'instruments': {
            0: ( 34, 127, ( 24925, 1.781798005104065 ), ( 33032, 0.8908990025520325 ), None ),
            1: ( 0, 127, None, ( 22948, 0.6299610137939453 ), None ),
            2: ( 0, 127, None, ( 9533, 2.3784139156341553 ), None ),
            3: ( 0, 127, None, ( 8456, 0.39684998989105225 ), None ),
            12: ( 0, 43, None, ( 23065, 2.1189260482788086 ), ( 23852, 0.5612310171127319 ) ),
        },
        'drums': {
            0: ( 15840, 0.2227250039577484 ), 1: ( 15840, 0.23596900701522827 ), 2: ( 15840, 0.25 ), 3: ( 15840, 0.2648659944534302 ),
            4: ( 15840, 0.28061598539352417 ), 5: ( 15840, 0.2973020076751709 ), 6: ( 15840, 0.31498000025749207 ), 7: ( 15840, 0.3337100148200989 ),
            8: ( 15840, 0.35355299711227417 ), 9: ( 15840, 0.37457698583602905 ), 10: ( 15840, 0.39684998989105225 ), 11: ( 15840, 0.4204480051994324 ),
            12: ( 15840, 0.44544899463653564 ), 13: ( 15840, 0.47193700075149536 ), 14: ( 15840, 0.5 ), 15: ( 15840, 0.5297319889068604 ),
            16: ( 15840, 0.5612310171127319 ), 17: ( 15840, 0.5946040153503418 ), 18: ( 15840, 0.6299610137939453 ), 19: ( 15840, 0.6674200296401978 ),
            20: ( 15840, 0.7071070075035095 ), 21: ( 15840, 0.7491539716720581 ), 22: ( 15840, 0.7937009930610657 ), 23: ( 15840, 0.8408970236778259 ),
            24: ( 15840, 0.8908990025520325 ), 25: ( 15840, 0.9438750147819519 ), 26: ( 15840, 1.0 ), 27: ( 4640, 1.0 ),
            28: ( 4640, 1.0594630241394043 ), 29: ( 16913, 1.0 ), 30: ( 16913, 1.0594630241394043 ), 31: ( 16913, 1.1224620342254639 ),
            32: ( 16913, 1.1892069578170776 ), 33: ( 16913, 1.2599209547042847 ), 34: ( 16913, 1.3348400592803955 ), 35: ( 16913, 1.414214015007019 ),
            36: ( 16913, 1.4983069896697998 ), 37: ( 16913, 1.587401032447815 ), 38: ( 16913, 1.681792974472046 ), 39: ( 16913, 1.781798005104065 ),
            40: ( 16913, 1.8877489566802979 ), 41: ( 16913, 2.0 ), 42: ( 16913, 2.1189260482788086 ), 43: ( 16913, 2.2449240684509277 ),
            44: ( 16913, 2.3784139156341553 ), 45: ( 16913, 2.5198419094085693 ), 46: ( 16913, 2.669680118560791 ), 47: ( 16913, 2.828428030014038 ),
            48: ( 16913, 2.996614933013916 ), 49: ( 16913, 3.1748030185699463 ), 50: ( 16913, 3.363585948944092 ), 51: ( 16913, 3.56359601020813 ),
            52: ( 16913, 3.7754979133605957 ), 53: ( 16913, 4.0 ), 54: ( 16913, 4.237853050231934 ), 55: ( 16913, 4.489849090576172 ),
            56: ( 16913, 4.756828784942627 ), 57: ( 16913, 5.039684772491455 ), 58: ( 16913, 5.339360237121582 ), 59: ( 16913, 5.65685510635376 ),
            60: ( 16913, 5.993228912353516 ), 61: ( 16913, 6.349606037139893 ), 62: ( 16913, 6.7271728515625 ), 63: ( 16913, 7.12719202041626 ),
        },
    },
    '0x06': {
        'instruments': {
            1: ( 0, 127, None, ( 22948, 0.6299610137939453 ), None ),
            10: ( 30, 40, ( 36435, 4.0 ), ( 32149, 1.2599209547042847 ), ( 27693, 0.6299610137939453 ) ),
            11: ( 30, 40, ( 36435, 4.0 ), ( 32149, 1.2599209547042847 ), ( 27693, 0.6299610137939453 ) ),
            13: ( 24, 44, ( 55394, 2.317720890045166 ), ( 69011, 1.0 ), ( 47587, 0.5 ) ),
            14: ( 22, 44, ( 55394, 2.317720890045166 ), ( 69011, 1.0 ), ( 47587, 0.5 ) ),
        },
        'drums': {
        },
    },
    '0x07': {
        'instruments': {
            0: ( 0, 127, None, ( 63561, 1.0 ), None ),
            2: ( 0, 127, None, ( 80438, 1.0 ), None ),
            3: ( 0, 127, None, ( 49216, 1.0 ), None ),
            4: ( 0, 127, None, ( 49216, 1.0 ), None ),
        },
        'drums': {
            0: ( 11729, 0.4204480051994324 ), 1: ( 11729, 0.44544899463653564 ), 2: ( 11729, 0.47193700075149536 ), 3: ( 11729, 0.5 ),
            4: ( 11729, 0.5297319889068604 ), 5: ( 11729, 0.5612310171127319 ), 6: ( 11729, 0.5946040153503418 ), 7: ( 11729, 0.6299610137939453 ),
            8: ( 11729, 0.6674200296401978 ), 9: ( 11729, 0.7071070075035095 ), 10: ( 11729, 0.7491539716720581 ), 11: ( 11729, 0.7937009930610657 ),
            12: ( 11729, 0.8408970236778259 ), 13: ( 11729, 0.8908990025520325 ), 14: ( 11729, 0.9438750147819519 ), 15: ( 11729, 1.0 ),
            16: ( 11729, 1.0594630241394043 ), 17: ( 6417, 1.0 ), 18: ( 6417, 1.0594630241394043 ), 19: ( 6417, 1.1224620342254639 ),
            20: ( 6417, 1.1892069578170776 ), 21: ( 6417, 1.2599209547042847 ), 22: ( 6417, 1.3348400592803955 ), 23: ( 6417, 1.414214015007019 ),
            24: ( 6417, 1.4983069896697998 ), 25: ( 6417, 1.587401032447815 ), 26: ( 6417, 1.681792974472046 ), 27: ( 6417, 1.781798005104065 ),
            28: ( 6417, 1.8877489566802979 ), 29: ( 6417, 2.0 ), 30: ( 6417, 2.1189260482788086 ), 31: ( 6417, 2.2449240684509277 ),
            32: ( 6417, 2.3784139156341553 ), 33: ( 6417, 2.5198419094085693 ), 34: ( 6417, 2.669680118560791 ), 35: ( 6417, 2.828428030014038 ),
            36: ( 6417, 2.996614933013916 ), 37: ( 6417, 3.1748030185699463 ), 38: ( 6417, 3.363585948944092 ), 39: ( 6417, 3.56359601020813 ),
            40: ( 6417, 3.7754979133605957 ), 41: ( 6417, 4.0 ), 42: ( 6417, 4.237853050231934 ), 43: ( 6417, 4.489849090576172 ),
            44: ( 6417, 4.756828784942627 ), 45: ( 6417, 5.039684772491455 ), 46: ( 6417, 5.339360237121582 ), 47: ( 6417, 5.65685510635376 ),
            48: ( 6417, 5.993228912353516 ), 49: ( 6417, 6.349606037139893 ), 50: ( 6417, 6.7271728515625 ), 51: ( 6417, 7.12719202041626 ),
            52: ( 6417, 7.550995826721191 ), 53: ( 6417, 8.0 ), 54: ( 6417, 8.47570514678955 ), 55: ( 6417, 8.979697227478027 ),
            56: ( 6417, 9.513657569885254 ), 57: ( 6417, 10.07936954498291 ), 58: ( 6417, 10.678720474243164 ), 59: ( 6417, 11.31371021270752 ),
            60: ( 6417, 11.986458778381348 ), 61: ( 6417, 12.699211120605469 ), 62: ( 6417, 13.454345703125 ), 63: ( 6417, 14.254383087158203 ),
        },
    },
    '0x08': {
        'instruments': {
            0: ( 0, 127, None, ( 15748, 0.6299610137939453 ), None ),
            1: ( 0, 45, None, ( 29276, 1.2599209547042847 ), ( 19171, 0.4204480051994324 ) ),
            2: ( 0, 45, None, ( 29276, 1.2599209547042847 ), ( 19171, 0.4204480051994324 ) ),
            3: ( 0, 127, None, ( 22948, 0.6299610137939453 ), None ),
            4: ( 0, 127, None, ( 38000, 0.5297319889068604 ), None ),
            5: ( 0, 127, None, ( 32366, 1.0 ), None ),
            6: ( 0, 127, None, ( 32366, 1.0 ), None ),
        },
        'drums': {
            0: ( 15840, 0.2227250039577484 ), 1: ( 15840, 0.23596900701522827 ), 2: ( 15840, 0.25 ), 3: ( 15840, 0.2648659944534302 ),
            4: ( 15840, 0.28061598539352417 ), 5: ( 15840, 0.2973020076751709 ), 6: ( 15840, 0.31498000025749207 ), 7: ( 15840, 0.3337100148200989 ),
            8: ( 15840, 0.35355299711227417 ), 9: ( 15840, 0.37457698583602905 ), 10: ( 15840, 0.39684998989105225 ), 11: ( 15840, 0.4204480051994324 ),
            12: ( 15840, 0.44544899463653564 ), 13: ( 15840, 0.47193700075149536 ), 14: ( 15840, 0.5 ), 15: ( 15840, 0.5297319889068604 ),
            16: ( 15840, 0.5612310171127319 ), 17: ( 15840, 0.5946040153503418 ), 18: ( 15840, 0.6299610137939453 ), 19: ( 15840, 0.6674200296401978 ),
            20: ( 15840, 0.7071070075035095 ), 21: ( 15840, 0.7491539716720581 ), 22: ( 15840, 0.7937009930610657 ), 23: ( 15840, 0.8408970236778259 ),
            24: ( 15840, 0.8908990025520325 ), 25: ( 15840, 0.9438750147819519 ), 26: ( 15840, 1.0 ), 27: ( 4640, 1.0 ),
            28: ( 4640, 1.0594630241394043 ), 29: ( 16913, 1.0 ), 30: ( 16913, 1.0594630241394043 ), 31: ( 16913, 1.1224620342254639 ),
            32: ( 16913, 1.1892069578170776 ), 33: ( 16913, 1.2599209547042847 ), 34: ( 16913, 1.3348400592803955 ), 35: ( 16913, 1.414214015007019 ),
            36: ( 16913, 1.4983069896697998 ), 37: ( 16913, 1.587401032447815 ), 38: ( 16913, 1.681792974472046 ), 39: ( 16913, 1.781798005104065 ),
            40: ( 16913, 1.8877489566802979 ), 41: ( 16913, 2.0 ), 42: ( 16913, 2.1189260482788086 ), 43: ( 16913, 2.2449240684509277 ),
            44: ( 16913, 2.3784139156341553 ), 45: ( 16913, 2.5198419094085693 ), 46: ( 16913, 2.669680118560791 ), 47: ( 16913, 2.828428030014038 ),
            48: ( 16913, 2.996614933013916 ), 49: ( 16913, 3.1748030185699463 ), 50: ( 16913, 3.363585948944092 ), 51: ( 16913, 3.56359601020813 ),
            52: ( 16913, 3.7754979133605957 ), 53: ( 16913, 4.0 ), 54: ( 16913, 4.237853050231934 ), 55: ( 16913, 4.489849090576172 ),
            56: ( 16913, 4.756828784942627 ), 57: ( 16913, 5.039684772491455 ), 58: ( 16913, 5.339360237121582 ), 59: ( 16913, 5.65685510635376 ),
            60: ( 16913, 5.993228912353516 ), 61: ( 16913, 6.349606037139893 ), 62: ( 16913, 6.7271728515625 ), 63: ( 16913, 7.12719202041626 ),
        },
    },
    '0x09': {
        'instruments': {
            0: ( 0, 47, None, ( 27578, 0.75 ), ( 31472, 0.375 ) ),
            1: ( 0, 47, None, ( 27578, 0.75 ), ( 31472, 0.375 ) ),
            2: ( 0, 47, None, ( 27578, 0.75 ), ( 31472, 0.375 ) ),
            3: ( 0, 127, None, ( 27578, 0.75 ), None ),
            4: ( 30, 40, ( 36435, 4.0 ), ( 32149, 1.2599209547042847 ), ( 27693, 0.6299610137939453 ) ),
            5: ( 0, 127, None, ( 22948, 0.6299610137939453 ), None ),
            6: ( 35, 127, ( 38000, 0.9744818210601807 ), ( 41218, 0.6890624761581421 ), None ),
            7: ( 35, 127, ( 38000, 0.9744818210601807 ), ( 41218, 0.6890624761581421 ), None ),
            8: ( 0, 127, None, ( 38000, 0.5297319889068604 ), None ),
            10: ( 30, 40, ( 36435, 4.0 ), ( 32149, 1.2599209547042847 ), ( 27693, 0.6299610137939453 ) ),
            11: ( 30, 40, ( 36435, 4.0 ), ( 32149, 1.2599209547042847 ), ( 27693, 0.6299610137939453 ) ),
            12: ( 0, 43, None, ( 23065, 2.1189260482788086 ), ( 23852, 0.5612310171127319 ) ),
        },
        'drums': {
            0: ( 35313, 0.3858463168144226 ), 1: ( 35313, 0.40879026055336 ), 2: ( 35313, 0.4330981969833374 ), 3: ( 35313, 0.45885127782821655 ),
            4: ( 35313, 0.4861360788345337 ), 5: ( 35313, 0.5150433778762817 ), 6: ( 35313, 0.545669436454773 ), 7: ( 35313, 0.5781167149543762 ),
            8: ( 35313, 0.6124930381774902 ), 9: ( 35313, 0.648914098739624 ), 10: ( 35313, 0.6875 ), 11: ( 35313, 0.7283807992935181 ),
            12: ( 35313, 0.7716926336288452 ), 13: ( 35313, 0.8175798058509827 ), 14: ( 35313, 0.8661956787109375 ), 15: ( 35313, 0.9177025556564331 ),
            16: ( 18001, 1.0 ), 17: ( 18001, 1.0594630241394043 ), 18: ( 18001, 1.0594630241394043 ), 19: ( 18001, 1.1224620342254639 ),
            20: ( 18001, 1.1892069578170776 ), 21: ( 61617, 0.6674200296401978 ), 22: ( 61617, 0.7071070075035095 ), 23: ( 61617, 0.7491539716720581 ),
            24: ( 61617, 0.7937009930610657 ), 25: ( 61617, 0.8408970236778259 ), 26: ( 61617, 0.8908990025520325 ), 27: ( 61617, 0.9438750147819519 ),
            28: ( 61617, 1.0 ), 29: ( 61617, 1.0594630241394043 ), 30: ( 61617, 1.1224620342254639 ), 31: ( 61617, 1.1892069578170776 ),
            32: ( 61617, 1.2599209547042847 ), 33: ( 59996, 0.35355299711227417 ), 34: ( 59996, 0.37457698583602905 ), 35: ( 59996, 0.39684998989105225 ),
            36: ( 59996, 0.4204480051994324 ), 37: ( 59996, 0.44544899463653564 ), 38: ( 59996, 0.47193700075149536 ), 39: ( 59996, 0.5 ),
            40: ( 59996, 0.5297319889068604 ), 41: ( 59996, 0.5612310171127319 ), 42: ( 59996, 0.5946040153503418 ), 43: ( 59996, 0.6299610137939453 ),
            44: ( 59996, 0.6674200296401978 ), 45: ( 59996, 0.7071070075035095 ), 46: ( 59996, 0.7491539716720581 ), 47: ( 59996, 0.7937009930610657 ),
            48: ( 59996, 0.8408970236778259 ), 49: ( 59996, 0.8908990025520325 ), 50: ( 59996, 0.9438750147819519 ), 51: ( 59996, 1.0 ),
            52: ( 59996, 1.0594630241394043 ), 53: ( 59996, 1.1224620342254639 ), 54: ( 59996, 1.1892069578170776 ), 55: ( 59996, 1.2599209547042847 ),
            56: ( 59996, 1.3348400592803955 ), 57: ( 59996, 1.414214015007019 ), 58: ( 59996, 1.4983069896697998 ), 59: ( 59996, 1.587401032447815 ),
            60: ( 59996, 1.681792974472046 ), 61: ( 59996, 1.781798005104065 ), 62: ( 59996, 1.8877489566802979 ), 63: ( 59996, 2.0 ),
        },
    },
    '0x0A': {
        'instruments': {
            3: ( 0, 127, None, ( 53009, 0.5794305801391602 ), None ),
            5: ( 0, 127, None, ( 84153, 0.6890624761581421 ), None ),
            6: ( 0, 127, None, ( 35328, 0.8680312633514404 ), None ),
            10: ( 35, 127, ( 38000, 0.9744818210601807 ), ( 41218, 0.6890624761581421 ), None ),
            11: ( 35, 127, ( 38000, 0.9744818210601807 ), ( 41218, 0.6890624761581421 ), None ),
            12: ( 0, 45, None, ( 53120, 0.5162138938903809 ), ( 59237, 0.36501842737197876 ) ),
            13: ( 0, 45, None, ( 53120, 0.5162138938903809 ), ( 59237, 0.36501842737197876 ) ),
        },
        'drums': {
            0: ( 25120, 0.31498000025749207 ), 1: ( 25120, 0.3337100148200989 ), 2: ( 25120, 0.35355299711227417 ), 3: ( 25120, 0.37457698583602905 ),
            4: ( 25120, 0.39684998989105225 ), 5: ( 25120, 0.4204480051994324 ), 6: ( 25120, 0.44544899463653564 ), 7: ( 25120, 0.47193700075149536 ),
            8: ( 25120, 0.5 ), 9: ( 25120, 0.5297319889068604 ), 10: ( 25120, 0.5612310171127319 ), 11: ( 25120, 0.5946040153503418 ),
            12: ( 25120, 0.6299610137939453 ), 13: ( 25120, 0.6674200296401978 ), 14: ( 25120, 0.7071070075035095 ), 15: ( 25120, 0.7491539716720581 ),
            16: ( 25120, 0.7937009930610657 ), 17: ( 16064, 0.7491539716720581 ), 18: ( 16064, 0.7937009930610657 ), 19: ( 16064, 0.8408970236778259 ),
            20: ( 16064, 0.8908990025520325 ), 21: ( 16064, 0.9438750147819519 ), 22: ( 16064, 1.0 ), 23: ( 16064, 1.0594630241394043 ),
            24: ( 16064, 1.1224620342254639 ), 25: ( 16064, 1.1892069578170776 ), 26: ( 16064, 1.2599209547042847 ), 27: ( 16064, 1.3348400592803955 ),
            28: ( 16064, 1.414214015007019 ), 29: ( 16064, 1.4983069896697998 ), 30: ( 16064, 1.587401032447815 ), 31: ( 16064, 1.681792974472046 ),
            32: ( 16064, 1.781798005104065 ), 33: ( 16064, 1.8877489566802979 ), 34: ( 16064, 2.0 ), 35: ( 16064, 2.1189260482788086 ),
            36: ( 16064, 2.2449240684509277 ), 37: ( 16064, 2.3784139156341553 ), 38: ( 16064, 2.5198419094085693 ), 39: ( 16064, 2.669680118560791 ),
            40: ( 16064, 2.828428030014038 ), 41: ( 16064, 2.996614933013916 ), 42: ( 16064, 3.1748030185699463 ), 43: ( 16064, 3.363585948944092 ),
            44: ( 16064, 3.56359601020813 ), 45: ( 16064, 3.7754979133605957 ), 46: ( 16064, 4.0 ), 47: ( 16064, 4.237853050231934 ),
            48: ( 16064, 4.489849090576172 ), 49: ( 16064, 4.756828784942627 ), 50: ( 16064, 5.039684772491455 ), 51: ( 16064, 5.339360237121582 ),
            52: ( 16064, 5.65685510635376 ), 53: ( 16064, 5.993228912353516 ), 54: ( 16064, 6.349606037139893 ), 55: ( 16064, 6.7271728515625 ),
            56: ( 16064, 7.12719202041626 ), 57: ( 16064, 7.550995826721191 ), 58: ( 16064, 8.0 ), 59: ( 16064, 8.47570514678955 ),
            60: ( 16064, 8.979697227478027 ), 61: ( 16064, 9.513657569885254 ), 62: ( 16064, 10.07936954498291 ), 63: ( 16064, 10.678720474243164 ),
        },
    },
    '0x0B': {
        'instruments': {
            0: ( 0, 127, None, ( 35945, 1.0 ), None ),
            1: ( 39, 127, ( 25358, 1.4983069896697998 ), ( 48727, 0.25 ), None ),
            2: ( 0, 127, None, ( 9059, 1.0 ), None ),
            3: ( 0, 127, None, ( 104977, 0.6890624761581421 ), None ),
        },
        'drums': {
        },
    },
    '0x0C': {
        'instruments': {
            0: ( 0, 127, None, ( 45509, 0.75 ), None ),
            1: ( 26, 37, ( 6688, 3.1748030185699463 ), ( 6993, 1.2599209547042847 ), ( 6368, 0.6299610137939453 ) ),
            2: ( 0, 127, None, ( 9799, 1.0594630241394043 ), None ),
        },
        'drums': {
        },
    },
    '0x0D': {
        'instruments': {
            0: ( 0, 127, None, ( 11988, 0.4340825080871582 ), None ),
            1: ( 0, 127, None, ( 11988, 0.4340825080871582 ), None ),
            2: ( 29, 48, ( 18107, 2.3811023235321045 ), ( 15341, 1.0011301040649414 ), ( 13987, 0.33408674597740173 ) ),
            3: ( 0, 127, None, ( 13987, 0.6681742668151855 ), None ),
            4: ( 0, 127, None, ( 13987, 0.6681742668151855 ), None ),
            11: ( 30, 40, ( 36435, 4.0 ), ( 32149, 1.2599209547042847 ), ( 27693, 0.6299610137939453 ) ),
            12: ( 30, 40, ( 36435, 4.0 ), ( 32149, 1.2599209547042847 ), ( 27693, 0.6299610137939453 ) ),
            13: ( 0, 127, None, ( 29315, 0.5946040153503418 ), None ),
            14: ( 0, 127, None, ( 29315, 0.5946040153503418 ), None ),
            15: ( 0, 127, None, ( 34720, 0.6890624761581421 ), None ),
        },
        'drums': {
        },
    },
    '0x0E': {
        'instruments': {
            0: ( 0, 127, None, ( 16928, 0.5 ), None ),
            1: ( 28, 127, ( 15808, 1.0 ), ( 19473, 1.2277700901031494 ), None ),
            2: ( 16, 127, ( 3921, 2.118926525115967 ), ( 4881, 2.6015539169311523 ), None ),
            3: ( 0, 127, None, ( 53009, 0.5794305801391602 ), None ),
            4: ( 0, 127, None, ( 53009, 0.5794305801391602 ), None ),
        },
        'drums': {
        },
    },
    '0x0F': {
        'instruments': {
            0: ( 0, 127, None, ( 32069, 0.3337100148200989 ), None ),
            1: ( 0, 127, None, ( 8456, 0.39684998989105225 ), None ),
            2: ( 0, 127, None, ( 5408, 0.5 ), None ),
            3: ( 0, 127, None, ( 9533, 2.3784139156341553 ), None ),
            4: ( 0, 127, None, ( 55209, 1.0 ), None ),
            8: ( 0, 127, None, ( 38000, 0.5297319889068604 ), None ),
            10: ( 30, 40, ( 36435, 4.0 ), ( 32149, 1.2599209547042847 ), ( 27693, 0.6299610137939453 ) ),
            11: ( 30, 40, ( 36435, 4.0 ), ( 32149, 1.2599209547042847 ), ( 27693, 0.6299610137939453 ) ),
            12: ( 0, 43, None, ( 23065, 2.1189260482788086 ), ( 23852, 0.5612310171127319 ) ),
            13: ( 0, 127, None, ( 53462, 1.3348400592803955 ), None ),
            14: ( 0, 47, None, ( 27578, 0.75 ), ( 31472, 0.375 ) ),
            15: ( 0, 50, None, ( 17548, 0.8908990025520325 ), ( 15237, 0.44544899463653564 ) ),
        },
        'drums': {
        },
    },
    '0x10': {
        'instruments': {
            0: ( 0, 127, None, ( 45509, 0.75 ), None ),
            1: ( 0, 127, None, ( 80438, 1.0 ), None ),
            2: ( 0, 127, None, ( 21951, 0.44544899463653564 ), None ),
            3: ( 28, 127, ( 15808, 1.0 ), ( 19473, 1.2277700901031494 ), None ),
            4: ( 0, 127, None, ( 80438, 1.0 ), None ),
            5: ( 0, 127, None, ( 21951, 0.44544899463653564 ), None ),
        },
        'drums': {
            0: ( 75148, 0.31498000025749207 ), 1: ( 75148, 0.3337100148200989 ), 2: ( 75148, 0.35355299711227417 ), 3: ( 75148, 0.37457698583602905 ),
            4: ( 75148, 0.39684998989105225 ), 5: ( 75148, 0.4204480051994324 ), 6: ( 75148, 0.44544899463653564 ), 7: ( 75148, 0.47193700075149536 ),
            8: ( 75148, 0.5 ), 9: ( 75148, 0.5297319889068604 ), 10: ( 75148, 0.5612310171127319 ), 11: ( 75148, 0.5946040153503418 ),
            12: ( 75148, 0.6299610137939453 ), 13: ( 75148, 0.6674200296401978 ), 14: ( 75148, 0.7071070075035095 ), 15: ( 75148, 0.7491539716720581 ),
            16: ( 75148, 0.7937009930610657 ), 17: ( 75148, 0.8408970236778259 ), 18: ( 75148, 0.8908990025520325 ), 19: ( 75148, 0.9438750147819519 ),
            20: ( 75148, 1.0 ), 21: ( 75148, 1.0594630241394043 ), 22: ( 75148, 1.1224620342254639 ), 23: ( 75148, 1.1892069578170776 ),
            24: ( 75148, 1.2599209547042847 ), 25: ( 75148, 1.3348400592803955 ), 26: ( 75148, 1.414214015007019 ), 27: ( 75148, 1.4983069896697998 ),
            28: ( 75148, 1.587401032447815 ), 29: ( 75148, 1.681792974472046 ), 30: ( 75148, 1.781798005104065 ), 31: ( 75148, 1.8877489566802979 ),
            32: ( 75148, 2.0 ), 33: ( 75148, 2.1189260482788086 ), 34: ( 41408, 0.375 ), 35: ( 41408, 0.39729899168014526 ),
            36: ( 41408, 0.42092326283454895 ), 37: ( 41408, 0.44595301151275635 ), 38: ( 41408, 0.472470760345459 ), 39: ( 41408, 0.5005650520324707 ),
            40: ( 41408, 0.530330240726471 ), 41: ( 41408, 0.5618654489517212 ), 42: ( 41408, 0.5952757596969604 ), 43: ( 41408, 0.6306727528572083 ),
            44: ( 41408, 0.6681742668151855 ), 45: ( 41408, 0.7079062461853027 ), 46: ( 41408, 0.75 ), 47: ( 41408, 0.7945972681045532 ),
            48: ( 41408, 0.8418465256690979 ), 49: ( 41408, 0.8919051885604858 ), 50: ( 41408, 0.9449406862258911 ), 51: ( 41408, 1.0011301040649414 ),
            52: ( 41408, 1.060660481452942 ), 53: ( 41408, 1.123730182647705 ), 54: ( 41408, 1.1905508041381836 ), 55: ( 41408, 1.2613446712493896 ),
            56: ( 41408, 1.336348533630371 ), 57: ( 41408, 1.4158117771148682 ), 58: ( 41408, 1.5 ), 59: ( 41408, 1.5891945362091064 ),
            60: ( 41408, 1.6836930513381958 ), 61: ( 41408, 1.7838103771209717 ), 62: ( 41408, 1.8898813724517822 ), 63: ( 41408, 2.002260208129883 ),
        },
    },
    '0x11': {
        'instruments': {
            0: ( 41, 127, ( 21000, 1.781798005104065 ), ( 18452, 1.1892069578170776 ), None ),
            1: ( 41, 127, ( 21000, 1.781798005104065 ), ( 18452, 1.1892069578170776 ), None ),
            5: ( 0, 127, None, ( 25236, 2.3811023235321045 ), None ),
            6: ( 0, 127, None, ( 15748, 0.6299610137939453 ), None ),
            7: ( 0, 45, None, ( 29276, 1.2599209547042847 ), ( 19171, 0.4204480051994324 ) ),
            13: ( 0, 127, None, ( 29315, 0.5946040153503418 ), None ),
            14: ( 0, 127, None, ( 29315, 0.5946040153503418 ), None ),
        },
        'drums': {
        },
    },
    '0x12': {
        'instruments': {
            0: ( 0, 47, None, ( 27578, 0.75 ), ( 31472, 0.375 ) ),
            1: ( 0, 47, None, ( 27578, 0.75 ), ( 31472, 0.375 ) ),
            4: ( 30, 40, ( 36435, 4.0 ), ( 32149, 1.2599209547042847 ), ( 27693, 0.6299610137939453 ) ),
            5: ( 0, 127, None, ( 22948, 0.6299610137939453 ), None ),
            8: ( 0, 127, None, ( 38000, 0.5297319889068604 ), None ),
            10: ( 30, 40, ( 36435, 4.0 ), ( 32149, 1.2599209547042847 ), ( 27693, 0.6299610137939453 ) ),
            11: ( 30, 40, ( 36435, 4.0 ), ( 32149, 1.2599209547042847 ), ( 27693, 0.6299610137939453 ) ),
            12: ( 0, 43, None, ( 23065, 2.1189260482788086 ), ( 23852, 0.5612310171127319 ) ),
        },
        'drums': {
            0: ( 35313, 0.3858463168144226 ), 1: ( 35313, 0.40879026055336 ), 2: ( 35313, 0.4330981969833374 ), 3: ( 35313, 0.45885127782821655 ),
            4: ( 35313, 0.4861360788345337 ), 5: ( 35313, 0.5150433778762817 ), 6: ( 35313, 0.545669436454773 ), 7: ( 35313, 0.5781167149543762 ),
            8: ( 35313, 0.6124930381774902 ), 9: ( 35313, 0.648914098739624 ), 10: ( 35313, 0.6875 ), 11: ( 35313, 0.7283807992935181 ),
            12: ( 35313, 0.7716926336288452 ), 13: ( 35313, 0.8175798058509827 ), 14: ( 35313, 0.8661956787109375 ), 15: ( 35313, 0.9177025556564331 ),
            16: ( 18001, 1.0 ), 17: ( 18001, 1.0594630241394043 ), 18: ( 18001, 1.0594630241394043 ), 19: ( 18001, 1.1224620342254639 ),
            20: ( 18001, 1.1892069578170776 ), 21: ( 61617, 0.6674200296401978 ), 22: ( 61617, 0.7071070075035095 ), 23: ( 61617, 0.7491539716720581 ),
            24: ( 61617, 0.7937009930610657 ), 25: ( 61617, 0.8408970236778259 ), 26: ( 61617, 0.8908990025520325 ), 27: ( 61617, 0.9438750147819519 ),
            28: ( 61617, 1.0 ), 29: ( 61617, 1.0594630241394043 ), 30: ( 61617, 1.1224620342254639 ), 31: ( 61617, 1.1892069578170776 ),
            32: ( 61617, 1.2599209547042847 ), 33: ( 59996, 0.35355299711227417 ), 34: ( 59996, 0.37457698583602905 ), 35: ( 59996, 0.39684998989105225 ),
            36: ( 59996, 0.4204480051994324 ), 37: ( 59996, 0.44544899463653564 ), 38: ( 59996, 0.47193700075149536 ), 39: ( 59996, 0.5 ),
            40: ( 59996, 0.5297319889068604 ), 41: ( 59996, 0.5612310171127319 ), 42: ( 59996, 0.5946040153503418 ),
        },
    },
    '0x13': {
        'instruments': {
            0: ( 0, 45, None, ( 53120, 0.5162138938903809 ), ( 59237, 0.36501842737197876 ) ),
            1: ( 0, 45, None, ( 53120, 0.5162138938903809 ), ( 59237, 0.36501842737197876 ) ),
            2: ( 0, 47, None, ( 27578, 0.75 ), ( 31472, 0.375 ) ),
            3: ( 0, 127, None, ( 38000, 0.5297319889068604 ), None ),
        },
        'drums': {
        },
    },
    '0x14': {
        'instruments': {
            0: ( 0, 127, None, ( 32069, 0.3337100148200989 ), None ),
            1: ( 0, 127, None, ( 5408, 0.5 ), None ),
            2: ( 0, 127, None, ( 5408, 0.5 ), None ),
            3: ( 0, 127, None, ( 32366, 1.0 ), None ),
            4: ( 0, 127, None, ( 38000, 0.5297319889068604 ), None ),
        },
        'drums': {
            0: ( 35313, 0.3858463168144226 ), 1: ( 35313, 0.40879026055336 ), 2: ( 35313, 0.4330981969833374 ), 3: ( 35313, 0.45885127782821655 ),
            4: ( 35313, 0.4861360788345337 ), 5: ( 35313, 0.5150433778762817 ), 6: ( 35313, 0.545669436454773 ), 7: ( 35313, 0.5781167149543762 ),
            8: ( 35313, 0.6124930381774902 ), 9: ( 35313, 0.648914098739624 ), 10: ( 35313, 0.6875 ), 11: ( 35313, 0.7283807992935181 ),
            12: ( 35313, 0.7716926336288452 ), 13: ( 35313, 0.8175798058509827 ), 14: ( 35313, 0.8661956787109375 ), 15: ( 35313, 0.9177025556564331 ),
            16: ( 18001, 1.0 ), 17: ( 18001, 1.0594630241394043 ), 18: ( 18001, 1.0594630241394043 ), 19: ( 18001, 1.1224620342254639 ),
            20: ( 18001, 1.1892069578170776 ), 21: ( 61617, 0.6674200296401978 ), 22: ( 61617, 0.7071070075035095 ), 23: ( 61617, 0.7491539716720581 ),
            24: ( 61617, 0.7937009930610657 ), 25: ( 61617, 0.8408970236778259 ), 26: ( 61617, 0.8908990025520325 ), 27: ( 61617, 0.9438750147819519 ),
            28: ( 61617, 1.0 ), 29: ( 61617, 1.0594630241394043 ), 30: ( 61617, 1.1224620342254639 ), 31: ( 61617, 1.1892069578170776 ),
            32: ( 61617, 1.2599209547042847 ), 33: ( 59996, 0.35355299711227417 ), 34: ( 59996, 0.37457698583602905 ), 35: ( 59996, 0.39684998989105225 ),
            36: ( 59996, 0.4204480051994324 ), 37: ( 59996, 0.44544899463653564 ), 38: ( 59996, 0.47193700075149536 ), 39: ( 59996, 0.5 ),
            40: ( 59996, 0.5297319889068604 ), 41: ( 59996, 0.5612310171127319 ), 42: ( 59996, 0.5946040153503418 ), 43: ( 59996, 0.6299610137939453 ),
            44: ( 59996, 0.6674200296401978 ), 45: ( 59996, 0.7071070075035095 ), 46: ( 59996, 0.7491539716720581 ), 47: ( 59996, 0.7937009930610657 ),
            48: ( 59996, 0.8408970236778259 ), 49: ( 59996, 0.8908990025520325 ), 50: ( 59996, 0.9438750147819519 ), 51: ( 59996, 1.0 ),
            52: ( 59996, 1.0594630241394043 ), 53: ( 59996, 1.1224620342254639 ), 54: ( 59996, 1.1892069578170776 ), 55: ( 59996, 1.2599209547042847 ),
            56: ( 59996, 1.3348400592803955 ), 57: ( 59996, 1.414214015007019 ), 58: ( 59996, 1.4983069896697998 ), 59: ( 59996, 1.587401032447815 ),
            60: ( 59996, 1.681792974472046 ), 61: ( 59996, 1.781798005104065 ), 62: ( 59996, 1.8877489566802979 ), 63: ( 59996, 2.0 ),
        },
    },
    '0x15': {
        'instruments': {
            0: ( 0, 51, None, ( 34735, 1.0 ), ( 17682, 0.44544899463653564 ) ),
            1: ( 0, 127, None, ( 45509, 0.75 ), None ),
            2: ( 0, 45, None, ( 29276, 1.2599209547042847 ), ( 19171, 0.4204480051994324 ) ),
        },
        'drums': {
            0: ( 15808, 0.2102240025997162 ), 1: ( 15808, 0.22272449731826782 ), 2: ( 15808, 0.23596850037574768 ), 3: ( 15808, 0.25 ),
            4: ( 15808, 0.2648659944534302 ), 5: ( 15808, 0.28061550855636597 ), 6: ( 15808, 0.2973020076751709 ), 7: ( 15808, 0.31498050689697266 ),
            8: ( 15808, 0.3337100148200989 ), 9: ( 15808, 0.35355350375175476 ), 10: ( 15808, 0.37457698583602905 ), 11: ( 15808, 0.39685049653053284 ),
            12: ( 15808, 0.42044851183891296 ), 13: ( 15808, 0.44544950127601624 ), 14: ( 15808, 0.47193750739097595 ), 15: ( 15808, 0.5 ),
            16: ( 15808, 0.5297315120697021 ), 17: ( 15808, 0.5612310171127319 ), 18: ( 15808, 0.5946034789085388 ), 19: ( 15808, 0.6299604773521423 ),
            20: ( 15808, 0.6674200296401978 ), 21: ( 18097, 0.35355299711227417 ), 22: ( 18097, 0.37457698583602905 ), 23: ( 18097, 0.39684998989105225 ),
            24: ( 18097, 0.4204480051994324 ), 25: ( 18097, 0.44544899463653564 ), 26: ( 18097, 0.47193700075149536 ), 27: ( 18097, 0.5 ),
            28: ( 18097, 0.5297319889068604 ), 29: ( 18097, 0.5612310171127319 ), 30: ( 18097, 0.5946040153503418 ), 31: ( 18097, 0.6299610137939453 ),
            32: ( 18097, 0.6674200296401978 ), 33: ( 18097, 0.7071070075035095 ), 34: ( 18097, 0.7491539716720581 ), 35: ( 18097, 0.7937009930610657 ),
            36: ( 18097, 0.8408970236778259 ), 37: ( 18097, 0.8908990025520325 ), 38: ( 18097, 0.9438750147819519 ), 39: ( 18097, 1.0 ),
            40: ( 19473, 1.3007769584655762 ), 41: ( 19473, 1.3781249523162842 ), 42: ( 19473, 1.46007239818573 ), 43: ( 19473, 1.5468928813934326 ),
            44: ( 19473, 1.6388757228851318 ), 45: ( 19473, 1.7363284826278687 ), 46: ( 19473, 1.8395763635635376 ), 47: ( 19473, 1.9489636421203613 ),
            48: ( 19473, 2.064854860305786 ), 49: ( 19473, 2.1876375675201416 ), 50: ( 19473, 2.317720890045166 ), 51: ( 19473, 2.455540180206299 ),
            52: ( 19473, 2.6015539169311523 ), 53: ( 19473, 2.7562499046325684 ), 54: ( 19473, 2.9201455116271973 ), 55: ( 19473, 3.0937864780426025 ),
            56: ( 19473, 3.277752161026001 ), 57: ( 19473, 3.4726576805114746 ), 58: ( 19473, 3.679152727127075 ), 59: ( 19473, 3.8979265689849854 ),
            60: ( 6961, 1.0 ), 61: ( 6961, 1.0594630241394043 ), 62: ( 6961, 1.1224620342254639 ), 63: ( 6961, 1.1892069578170776 ),
        },
    },
    '0x16': {
        'instruments': {
            0: ( 0, 45, None, ( 29276, 1.2599209547042847 ), ( 19171, 0.4204480051994324 ) ),
            1: ( 0, 127, None, ( 32366, 1.0 ), None ),
            2: ( 0, 127, None, ( 25236, 2.3811023235321045 ), None ),
            3: ( 0, 127, None, ( 34693, 0.6674200296401978 ), None ),
            4: ( 0, 127, None, ( 25395, 0.5 ), None ),
            10: ( 0, 127, None, ( 5792, 0.2102240025997162 ), None ),
        },
        'drums': {
            0: ( 15808, 0.2102240025997162 ), 1: ( 15808, 0.22272449731826782 ), 2: ( 15808, 0.23596850037574768 ), 3: ( 15808, 0.25 ),
            4: ( 15808, 0.2648659944534302 ), 5: ( 15808, 0.28061550855636597 ), 6: ( 15808, 0.2973020076751709 ), 7: ( 15808, 0.31498050689697266 ),
            8: ( 15808, 0.3337100148200989 ), 9: ( 15808, 0.35355350375175476 ), 10: ( 15808, 0.37457698583602905 ), 11: ( 15808, 0.39685049653053284 ),
            12: ( 15808, 0.42044851183891296 ), 13: ( 15808, 0.44544950127601624 ), 14: ( 15808, 0.47193750739097595 ), 15: ( 15808, 0.5 ),
            16: ( 15808, 0.5297315120697021 ), 17: ( 15808, 0.5612310171127319 ), 18: ( 15808, 0.5946034789085388 ), 19: ( 15808, 0.6299604773521423 ),
            20: ( 15808, 0.6674200296401978 ), 21: ( 18097, 0.35355299711227417 ), 22: ( 18097, 0.37457698583602905 ), 23: ( 18097, 0.39684998989105225 ),
            24: ( 18097, 0.4204480051994324 ), 25: ( 18097, 0.44544899463653564 ), 26: ( 18097, 0.47193700075149536 ), 27: ( 18097, 0.5 ),
            28: ( 18097, 0.5297319889068604 ), 29: ( 18097, 0.5612310171127319 ), 30: ( 18097, 0.5946040153503418 ), 31: ( 18097, 0.6299610137939453 ),
            32: ( 18097, 0.6674200296401978 ), 33: ( 18097, 0.7071070075035095 ), 34: ( 18097, 0.7491539716720581 ), 35: ( 18097, 0.7937009930610657 ),
            36: ( 18097, 0.8408970236778259 ), 37: ( 18097, 0.8908990025520325 ), 38: ( 18097, 0.9438750147819519 ), 39: ( 18097, 1.0 ),
            40: ( 19473, 1.3007769584655762 ), 41: ( 19473, 1.3781249523162842 ), 42: ( 19473, 1.46007239818573 ), 43: ( 19473, 1.5468928813934326 ),
            44: ( 19473, 1.6388757228851318 ), 45: ( 19473, 1.7363284826278687 ), 46: ( 19473, 1.8395763635635376 ), 47: ( 19473, 1.9489636421203613 ),
            48: ( 19473, 2.064854860305786 ), 49: ( 19473, 2.1876375675201416 ), 50: ( 19473, 2.317720890045166 ), 51: ( 19473, 2.455540180206299 ),
            52: ( 19473, 2.6015539169311523 ), 53: ( 19473, 2.7562499046325684 ), 54: ( 19473, 2.9201455116271973 ), 55: ( 19473, 3.0937864780426025 ),
            56: ( 19473, 3.277752161026001 ), 57: ( 19473, 3.4726576805114746 ), 58: ( 19473, 3.679152727127075 ), 59: ( 19473, 3.8979265689849854 ),
            60: ( 6961, 1.0 ), 61: ( 6961, 1.0594630241394043 ), 62: ( 6961, 1.1224620342254639 ), 63: ( 6961, 1.1892069578170776 ),
        },
    },
    '0x17': {
        'instruments': {
            0: ( 0, 127, None, ( 58063, 0.8418465256690979 ), None ),
            1: ( 0, 127, None, ( 58063, 0.8418465256690979 ), None ),
            2: ( 0, 127, None, ( 84153, 0.6890624761581421 ), None ),
            3: ( 0, 127, None, ( 58063, 0.8418465256690979 ), None ),
        },
        'drums': {
        },
    },
    '0x18': {
        'instruments': {
            0: ( 20, 20, ( 7313, 4.0 ), ( 10880, 2.996614933013916 ), ( 6880, 2.121320962905884 ) ),
            1: ( 0, 127, None, ( 35945, 1.0 ), None ),
            2: ( 39, 127, ( 25358, 1.4983069896697998 ), ( 48727, 0.25 ), None ),
            3: ( 35, 127, ( 38000, 0.9744818210601807 ), ( 41218, 0.6890624761581421 ), None ),
            4: ( 0, 45, None, ( 53120, 0.5162138938903809 ), ( 59237, 0.36501842737197876 ) ),
            6: ( 0, 127, None, ( 100320, 0.125 ), None ),
            7: ( 0, 127, None, ( 104977, 0.6890624761581421 ), None ),
            8: ( 0, 127, None, ( 53462, 1.3348400592803955 ), None ),
        },
        'drums': {
        },
    },
    '0x19': {
        'instruments': {
            0: ( 0, 127, None, ( 32069, 0.3337100148200989 ), None ),
            1: ( 34, 127, ( 75148, 2.996614933013916 ), ( 41408, 0.5005650520324707 ), None ),
            4: ( 0, 127, None, ( 58063, 0.8418465256690979 ), None ),
            5: ( 0, 127, None, ( 9799, 1.0594630241394043 ), None ),
            6: ( 0, 127, None, ( 45509, 0.75 ), None ),
            7: ( 34, 127, ( 24925, 1.781798005104065 ), ( 33032, 0.8908990025520325 ), None ),
        },
        'drums': {
        },
    },
    '0x1A': {
        'instruments': {
            13: ( 22, 44, ( 55394, 2.317720890045166 ), ( 69011, 1.0 ), ( 47587, 0.5 ) ),
            14: ( 22, 44, ( 55394, 2.317720890045166 ), ( 69011, 1.0 ), ( 47587, 0.5 ) ),
        },
        'drums': {
        },
    },
    '0x1B': {
        'instruments': {
            0: ( 0, 127, None, ( 25395, 0.5 ), None ),
            1: ( 0, 127, None, ( 34693, 0.6674200296401978 ), None ),
            2: ( 0, 45, None, ( 29276, 1.2599209547042847 ), ( 19171, 0.4204480051994324 ) ),
            3: ( 0, 45, None, ( 29276, 1.2599209547042847 ), ( 19171, 0.4204480051994324 ) ),
            5: ( 0, 127, None, ( 25236, 2.3811023235321045 ), None ),
            7: ( 0, 45, None, ( 29276, 1.2599209547042847 ), ( 19171, 0.4204480051994324 ) ),
            10: ( 0, 127, None, ( 3633, 0.5 ), None ),
            11: ( 0, 127, None, ( 3633, 0.5 ), None ),
        },
        'drums': {
        },
    },
    '0x1C': {
        'instruments': {
            0: ( 34, 127, ( 24925, 1.781798005104065 ), ( 33032, 0.8908990025520325 ), None ),
            1: ( 20, 20, ( 7313, 4.0 ), ( 10880, 2.996614933013916 ), ( 6880, 2.121320962905884 ) ),
            3: ( 0, 127, None, ( 16928, 0.5 ), None ),
            4: ( 34, 127, ( 75148, 2.996614933013916 ), ( 41408, 0.5005650520324707 ), None ),
        },
        'drums': {
        },
    },
    '0x1D': {
        'instruments': {
            0: ( 34, 127, ( 24925, 1.781798005104065 ), ( 33032, 0.8908990025520325 ), None ),
            1: ( 20, 20, ( 7313, 4.0 ), ( 10880, 2.996614933013916 ), ( 6880, 2.121320962905884 ) ),
            5: ( 0, 127, None, ( 32069, 0.3337100148200989 ), None ),
            7: ( 0, 127, None, ( 32069, 0.3337100148200989 ), None ),
            10: ( 30, 40, ( 36435, 4.0 ), ( 32149, 1.2599209547042847 ), ( 27693, 0.6299610137939453 ) ),
            11: ( 30, 40, ( 36435, 4.0 ), ( 32149, 1.2599209547042847 ), ( 27693, 0.6299610137939453 ) ),
        },
        'drums': {
            0: ( 75148, 0.31498000025749207 ), 1: ( 75148, 0.3337100148200989 ), 2: ( 75148, 0.35355299711227417 ), 3: ( 75148, 0.37457698583602905 ),
            4: ( 75148, 0.39684998989105225 ), 5: ( 75148, 0.4204480051994324 ), 6: ( 75148, 0.44544899463653564 ), 7: ( 75148, 0.47193700075149536 ),
            8: ( 75148, 0.5 ), 9: ( 75148, 0.5297319889068604 ), 10: ( 75148, 0.5612310171127319 ), 11: ( 75148, 0.5946040153503418 ),
            12: ( 75148, 0.6299610137939453 ), 13: ( 75148, 0.6674200296401978 ), 14: ( 75148, 0.7071070075035095 ), 15: ( 75148, 0.7491539716720581 ),
            16: ( 75148, 0.7937009930610657 ), 17: ( 75148, 0.8408970236778259 ), 18: ( 75148, 0.8908990025520325 ), 19: ( 75148, 0.9438750147819519 ),
            20: ( 75148, 1.0 ), 21: ( 75148, 1.0594630241394043 ), 22: ( 75148, 1.1224620342254639 ), 23: ( 75148, 1.1892069578170776 ),
            24: ( 75148, 1.2599209547042847 ), 25: ( 75148, 1.3348400592803955 ), 26: ( 75148, 1.414214015007019 ), 27: ( 75148, 1.4983069896697998 ),
            28: ( 75148, 1.587401032447815 ), 29: ( 75148, 1.681792974472046 ), 30: ( 75148, 1.781798005104065 ), 31: ( 75148, 1.8877489566802979 ),
            32: ( 75148, 2.0 ), 33: ( 75148, 2.1189260482788086 ), 34: ( 41408, 0.375 ), 35: ( 41408, 0.39729899168014526 ),
            36: ( 41408, 0.42092326283454895 ), 37: ( 41408, 0.44595301151275635 ), 38: ( 41408, 0.472470760345459 ), 39: ( 41408, 0.5005650520324707 ),
            40: ( 41408, 0.530330240726471 ), 41: ( 41408, 0.5618654489517212 ), 42: ( 41408, 0.5952757596969604 ), 43: ( 41408, 0.6306727528572083 ),
            44: ( 41408, 0.6681742668151855 ), 45: ( 41408, 0.7079062461853027 ), 46: ( 41408, 0.75 ), 47: ( 41408, 0.7945972681045532 ),
            48: ( 41408, 0.8418465256690979 ), 49: ( 41408, 0.8919051885604858 ), 50: ( 41408, 0.9449406862258911 ), 51: ( 41408, 1.0011301040649414 ),
            52: ( 41408, 1.060660481452942 ), 53: ( 41408, 1.123730182647705 ), 54: ( 41408, 1.1905508041381836 ), 55: ( 41408, 1.2613446712493896 ),
            56: ( 41408, 1.336348533630371 ), 57: ( 41408, 1.4158117771148682 ), 58: ( 41408, 1.5 ), 59: ( 41408, 1.5891945362091064 ),
            60: ( 41408, 1.6836930513381958 ), 61: ( 41408, 1.7838103771209717 ), 62: ( 41408, 1.8898813724517822 ), 63: ( 41408, 2.002260208129883 ),
        },
    },
    '0x1E': {
        'instruments': {
            0: ( 0, 50, None, ( 71862, 1.0 ), ( 29819, 0.5 ) ),
            1: ( 0, 50, None, ( 71862, 1.0 ), ( 29819, 0.5 ) ),
            2: ( 0, 50, None, ( 71862, 1.0 ), ( 29819, 0.5 ) ),
            4: ( 0, 127, None, ( 55209, 1.0 ), None ),
        },
        'drums': {
        },
    },
    '0x1F': {
        'instruments': {
            1: ( 0, 127, None, ( 35945, 1.0 ), None ),
            2: ( 39, 127, ( 25358, 1.4983069896697998 ), ( 48727, 0.25 ), None ),
            3: ( 35, 127, ( 38000, 0.9744818210601807 ), ( 41218, 0.6890624761581421 ), None ),
            4: ( 24, 44, ( 55394, 2.317720890045166 ), ( 69011, 1.0 ), ( 47587, 0.5 ) ),
            5: ( 22, 44, ( 55394, 2.317720890045166 ), ( 69011, 1.0 ), ( 47587, 0.5 ) ),
            7: ( 0, 127, None, ( 104977, 0.6890624761581421 ), None ),
        },
        'drums': {
        },
    },
    '0x20': {
        'instruments': {
            0: ( 0, 127, None, ( 32069, 0.3337100148200989 ), None ),
            1: ( 0, 45, None, ( 53120, 0.5162138938903809 ), ( 59237, 0.36501842737197876 ) ),
            2: ( 35, 127, ( 38000, 0.9744818210601807 ), ( 41218, 0.6890624761581421 ), None ),
            4: ( 0, 127, None, ( 55209, 1.0 ), None ),
            5: ( 0, 127, None, ( 25395, 0.5 ), None ),
            6: ( 0, 127, None, ( 34693, 0.6674200296401978 ), None ),
            7: ( 0, 127, None, ( 21545, 3.1748030185699463 ), None ),
            10: ( 30, 40, ( 36435, 4.0 ), ( 32149, 1.2599209547042847 ), ( 27693, 0.6299610137939453 ) ),
            11: ( 30, 40, ( 36435, 4.0 ), ( 32149, 1.2599209547042847 ), ( 27693, 0.6299610137939453 ) ),
            13: ( 24, 44, ( 55394, 2.317720890045166 ), ( 69011, 1.0 ), ( 47587, 0.5 ) ),
            15: ( 0, 50, None, ( 17548, 0.8908990025520325 ), ( 15237, 0.44544899463653564 ) ),
        },
        'drums': {
            0: ( 35313, 0.3858463168144226 ), 1: ( 35313, 0.40879026055336 ), 2: ( 35313, 0.4330981969833374 ), 3: ( 35313, 0.45885127782821655 ),
            4: ( 35313, 0.4861360788345337 ), 5: ( 35313, 0.5150433778762817 ), 6: ( 35313, 0.545669436454773 ), 7: ( 35313, 0.5781167149543762 ),
            8: ( 35313, 0.6124930381774902 ), 9: ( 35313, 0.648914098739624 ), 10: ( 35313, 0.6875 ), 11: ( 35313, 0.7283807992935181 ),
            12: ( 35313, 0.7716926336288452 ), 13: ( 35313, 0.8175798058509827 ), 14: ( 35313, 0.8661956787109375 ), 15: ( 35313, 0.9177025556564331 ),
            16: ( 18001, 1.0 ), 17: ( 18001, 1.0594630241394043 ), 18: ( 18001, 1.0594630241394043 ), 19: ( 18001, 1.1224620342254639 ),
            20: ( 18001, 1.1892069578170776 ), 21: ( 61617, 0.6674200296401978 ), 22: ( 61617, 0.7071070075035095 ), 23: ( 61617, 0.7491539716720581 ),
            24: ( 61617, 0.7937009930610657 ), 25: ( 61617, 0.8408970236778259 ), 26: ( 61617, 0.8908990025520325 ), 27: ( 61617, 0.9438750147819519 ),
            28: ( 61617, 1.0 ), 29: ( 61617, 1.0594630241394043 ), 30: ( 61617, 1.1224620342254639 ), 31: ( 61617, 1.1892069578170776 ),
            32: ( 61617, 1.2599209547042847 ), 33: ( 59996, 0.35355299711227417 ), 34: ( 59996, 0.37457698583602905 ), 35: ( 59996, 0.39684998989105225 ),
            36: ( 59996, 0.4204480051994324 ), 37: ( 59996, 0.44544899463653564 ), 38: ( 59996, 0.47193700075149536 ), 39: ( 59996, 0.5 ),
            40: ( 59996, 0.5297319889068604 ), 41: ( 59996, 0.5612310171127319 ), 42: ( 59996, 0.5946040153503418 ), 43: ( 59996, 0.6299610137939453 ),
            44: ( 59996, 0.6674200296401978 ), 45: ( 59996, 0.7071070075035095 ), 46: ( 59996, 0.7491539716720581 ), 47: ( 59996, 0.7937009930610657 ),
            48: ( 59996, 0.8408970236778259 ), 49: ( 59996, 0.8908990025520325 ), 50: ( 59996, 0.9438750147819519 ), 51: ( 59996, 1.0 ),
            52: ( 59996, 1.0594630241394043 ), 53: ( 59996, 1.1224620342254639 ), 54: ( 59996, 1.1892069578170776 ), 55: ( 59996, 1.2599209547042847 ),
            56: ( 59996, 1.3348400592803955 ), 57: ( 59996, 1.414214015007019 ), 58: ( 59996, 1.4983069896697998 ), 59: ( 59996, 1.587401032447815 ),
            60: ( 59996, 1.681792974472046 ), 61: ( 59996, 1.781798005104065 ), 62: ( 59996, 1.8877489566802979 ), 63: ( 59996, 2.0 ),
        },
    },
    '0x21': {
        'instruments': {
            0: ( 0, 127, None, ( 11988, 0.4340825080871582 ), None ),
            1: ( 0, 127, None, ( 11988, 0.4340825080871582 ), None ),
            2: ( 0, 127, None, ( 5408, 0.5 ), None ),
            4: ( 0, 127, None, ( 55209, 1.0 ), None ),
            5: ( 0, 127, None, ( 8456, 0.39684998989105225 ), None ),
            6: ( 0, 47, None, ( 27578, 0.75 ), ( 31472, 0.375 ) ),
            7: ( 0, 127, None, ( 29315, 0.5946040153503418 ), None ),
            8: ( 0, 127, None, ( 38000, 0.5297319889068604 ), None ),
            10: ( 30, 40, ( 36435, 4.0 ), ( 32149, 1.2599209547042847 ), ( 27693, 0.6299610137939453 ) ),
            11: ( 30, 40, ( 36435, 4.0 ), ( 32149, 1.2599209547042847 ), ( 27693, 0.6299610137939453 ) ),
            13: ( 0, 127, None, ( 34720, 0.6890624761581421 ), None ),
            14: ( 0, 47, None, ( 27578, 0.75 ), ( 31472, 0.375 ) ),
            15: ( 0, 45, None, ( 53120, 0.5162138938903809 ), ( 59237, 0.36501842737197876 ) ),
        },
        'drums': {
            0: ( 35313, 0.3858463168144226 ), 1: ( 35313, 0.40879026055336 ), 2: ( 35313, 0.4330981969833374 ), 3: ( 35313, 0.45885127782821655 ),
            4: ( 35313, 0.4861360788345337 ), 5: ( 35313, 0.5150433778762817 ), 6: ( 35313, 0.545669436454773 ), 7: ( 35313, 0.5781167149543762 ),
            8: ( 35313, 0.6124930381774902 ), 9: ( 35313, 0.648914098739624 ), 10: ( 35313, 0.6875 ), 11: ( 35313, 0.7283807992935181 ),
            12: ( 35313, 0.7716926336288452 ), 13: ( 35313, 0.8175798058509827 ), 14: ( 35313, 0.8661956787109375 ), 15: ( 35313, 0.9177025556564331 ),
            16: ( 18001, 1.0 ), 17: ( 18001, 1.0594630241394043 ), 18: ( 18001, 1.0594630241394043 ), 19: ( 18001, 1.1224620342254639 ),
            20: ( 18001, 1.1892069578170776 ), 21: ( 61617, 0.6674200296401978 ), 22: ( 61617, 0.7071070075035095 ), 23: ( 61617, 0.7491539716720581 ),
            24: ( 61617, 0.7937009930610657 ), 25: ( 61617, 0.8408970236778259 ), 26: ( 61617, 0.8908990025520325 ), 27: ( 61617, 0.9438750147819519 ),
            28: ( 61617, 1.0 ), 29: ( 61617, 1.0594630241394043 ), 30: ( 61617, 1.1224620342254639 ), 31: ( 61617, 1.1892069578170776 ),
            32: ( 61617, 1.2599209547042847 ), 33: ( 59996, 0.35355299711227417 ), 34: ( 59996, 0.37457698583602905 ), 35: ( 59996, 0.39684998989105225 ),
            36: ( 59996, 0.4204480051994324 ), 37: ( 59996, 0.44544899463653564 ), 38: ( 59996, 0.47193700075149536 ), 39: ( 59996, 0.5 ),
            40: ( 59996, 0.5297319889068604 ), 41: ( 59996, 0.5612310171127319 ), 42: ( 59996, 0.5946040153503418 ), 43: ( 59996, 0.6299610137939453 ),
            44: ( 59996, 0.6674200296401978 ), 45: ( 59996, 0.7071070075035095 ), 46: ( 59996, 0.7491539716720581 ), 47: ( 59996, 0.7937009930610657 ),
            48: ( 59996, 0.8408970236778259 ), 49: ( 59996, 0.8908990025520325 ), 50: ( 59996, 0.9438750147819519 ), 51: ( 59996, 1.0 ),
            52: ( 59996, 1.0594630241394043 ), 53: ( 59996, 1.1224620342254639 ), 54: ( 59996, 1.1892069578170776 ), 55: ( 59996, 1.2599209547042847 ),
            56: ( 59996, 1.3348400592803955 ), 57: ( 59996, 1.414214015007019 ), 58: ( 59996, 1.4983069896697998 ), 59: ( 59996, 1.587401032447815 ),
            60: ( 59996, 1.681792974472046 ), 61: ( 59996, 1.781798005104065 ), 62: ( 59996, 1.8877489566802979 ), 63: ( 59996, 2.0 ),
        },
    },
    '0x22': {
        'instruments': {
            0: ( 34, 127, ( 24925, 1.781798005104065 ), ( 33032, 0.8908990025520325 ), None ),
            1: ( 0, 127, None, ( 22948, 0.6299610137939453 ), None ),
            2: ( 0, 127, None, ( 9533, 2.3784139156341553 ), None ),
            3: ( 0, 127, None, ( 8456, 0.39684998989105225 ), None ),
            4: ( 0, 45, None, ( 53120, 0.5162138938903809 ), ( 59237, 0.36501842737197876 ) ),
            5: ( 27, 28, ( 15840, 2.1189260482788086 ), ( 4640, 2.0 ), ( 16913, 1.781798005104065 ) ),
            6: ( 0, 47, None, ( 27578, 0.75 ), ( 31472, 0.375 ) ),
            7: ( 0, 127, None, ( 38000, 0.5297319889068604 ), None ),
            8: ( 0, 127, None, ( 11988, 0.4340825080871582 ), None ),
            10: ( 30, 40, ( 36435, 4.0 ), ( 32149, 1.2599209547042847 ), ( 27693, 0.6299610137939453 ) ),
            11: ( 30, 40, ( 36435, 4.0 ), ( 32149, 1.2599209547042847 ), ( 27693, 0.6299610137939453 ) ),
            12: ( 0, 43, None, ( 23065, 2.1189260482788086 ), ( 23852, 0.5612310171127319 ) ),
            13: ( 0, 127, None, ( 55209, 1.0 ), None ),
            14: ( 35, 127, ( 38000, 0.9744818210601807 ), ( 41218, 0.6890624761581421 ), None ),
            15: ( 16, 127, ( 3921, 2.118926525115967 ), ( 4881, 2.6015539169311523 ), None ),
        },
        'drums': {
            0: ( 35313, 0.3858463168144226 ), 1: ( 35313, 0.40879026055336 ), 2: ( 35313, 0.4330981969833374 ), 3: ( 35313, 0.45885127782821655 ),
            4: ( 35313, 0.4861360788345337 ), 5: ( 35313, 0.5150433778762817 ), 6: ( 35313, 0.545669436454773 ), 7: ( 35313, 0.5781167149543762 ),
            8: ( 35313, 0.6124930381774902 ), 9: ( 35313, 0.648914098739624 ), 10: ( 35313, 0.6875 ), 11: ( 35313, 0.7283807992935181 ),
            12: ( 35313, 0.7716926336288452 ), 13: ( 35313, 0.8175798058509827 ), 14: ( 35313, 0.8661956787109375 ), 15: ( 35313, 0.9177025556564331 ),
            16: ( 18001, 1.0 ), 17: ( 18001, 1.0594630241394043 ), 18: ( 18001, 1.0594630241394043 ), 19: ( 18001, 1.1224620342254639 ),
            20: ( 18001, 1.1892069578170776 ), 21: ( 61617, 0.6674200296401978 ), 22: ( 61617, 0.7071070075035095 ), 23: ( 61617, 0.7491539716720581 ),
            24: ( 61617, 0.7937009930610657 ), 25: ( 61617, 0.8408970236778259 ), 26: ( 61617, 0.8908990025520325 ), 27: ( 61617, 0.9438750147819519 ),
            28: ( 61617, 1.0 ), 29: ( 61617, 1.0594630241394043 ), 30: ( 61617, 1.1224620342254639 ), 31: ( 61617, 1.1892069578170776 ),
            32: ( 61617, 1.2599209547042847 ), 33: ( 59996, 0.35355299711227417 ), 34: ( 59996, 0.37457698583602905 ), 35: ( 59996, 0.39684998989105225 ),
            36: ( 59996, 0.4204480051994324 ), 37: ( 59996, 0.44544899463653564 ), 38: ( 59996, 0.47193700075149536 ), 39: ( 59996, 0.5 ),
            40: ( 59996, 0.5297319889068604 ), 41: ( 59996, 0.5612310171127319 ), 42: ( 59996, 0.5946040153503418 ), 43: ( 59996, 0.6299610137939453 ),
            44: ( 59996, 0.6674200296401978 ), 45: ( 59996, 0.7071070075035095 ), 46: ( 59996, 0.7491539716720581 ), 47: ( 59996, 0.7937009930610657 ),
            48: ( 59996, 0.8408970236778259 ), 49: ( 59996, 0.8908990025520325 ), 50: ( 59996, 0.9438750147819519 ), 51: ( 59996, 1.0 ),
            52: ( 59996, 1.0594630241394043 ), 53: ( 59996, 1.1224620342254639 ), 54: ( 59996, 1.1892069578170776 ), 55: ( 59996, 1.2599209547042847 ),
            56: ( 59996, 1.3348400592803955 ), 57: ( 59996, 1.414214015007019 ), 58: ( 59996, 1.4983069896697998 ), 59: ( 59996, 1.587401032447815 ),
            60: ( 59996, 1.681792974472046 ), 61: ( 59996, 1.781798005104065 ), 62: ( 59996, 1.8877489566802979 ), 63: ( 59996, 2.0 ),
        },
    },
    '0x23': {
        'instruments': {
            5: ( 0, 127, None, ( 25395, 0.5 ), None ),
            6: ( 0, 127, None, ( 34693, 0.6674200296401978 ), None ),
            7: ( 0, 127, None, ( 21545, 3.1748030185699463 ), None ),
            8: ( 0, 127, None, ( 38000, 0.5297319889068604 ), None ),
            10: ( 30, 40, ( 36435, 4.0 ), ( 32149, 1.2599209547042847 ), ( 27693, 0.6299610137939453 ) ),
            11: ( 30, 40, ( 36435, 4.0 ), ( 32149, 1.2599209547042847 ), ( 27693, 0.6299610137939453 ) ),
            14: ( 0, 47, None, ( 27578, 0.75 ), ( 31472, 0.375 ) ),
        },
        'drums': {
            0: ( 35313, 0.3858463168144226 ), 1: ( 35313, 0.40879026055336 ), 2: ( 35313, 0.4330981969833374 ), 3: ( 35313, 0.45885127782821655 ),
            4: ( 35313, 0.4861360788345337 ), 5: ( 35313, 0.5150433778762817 ), 6: ( 35313, 0.545669436454773 ), 7: ( 35313, 0.5781167149543762 ),
            8: ( 35313, 0.6124930381774902 ), 9: ( 35313, 0.648914098739624 ), 10: ( 35313, 0.6875 ), 11: ( 35313, 0.7283807992935181 ),
            12: ( 35313, 0.7716926336288452 ), 13: ( 35313, 0.8175798058509827 ), 14: ( 35313, 0.8661956787109375 ), 15: ( 35313, 0.9177025556564331 ),
            16: ( 18001, 1.0 ), 17: ( 18001, 1.0594630241394043 ), 18: ( 18001, 1.0594630241394043 ), 19: ( 18001, 1.1224620342254639 ),
            20: ( 18001, 1.1892069578170776 ), 21: ( 61617, 0.6674200296401978 ), 22: ( 61617, 0.7071070075035095 ), 23: ( 61617, 0.7491539716720581 ),
            24: ( 61617, 0.7937009930610657 ), 25: ( 61617, 0.8408970236778259 ), 26: ( 61617, 0.8908990025520325 ), 27: ( 61617, 0.9438750147819519 ),
            28: ( 61617, 1.0 ), 29: ( 61617, 1.0594630241394043 ), 30: ( 61617, 1.1224620342254639 ), 31: ( 61617, 1.1892069578170776 ),
            32: ( 61617, 1.2599209547042847 ), 33: ( 59996, 0.35355299711227417 ), 34: ( 59996, 0.37457698583602905 ), 35: ( 59996, 0.39684998989105225 ),
            36: ( 59996, 0.4204480051994324 ), 37: ( 59996, 0.44544899463653564 ), 38: ( 59996, 0.47193700075149536 ), 39: ( 59996, 0.5 ),
            40: ( 59996, 0.5297319889068604 ), 41: ( 59996, 0.5612310171127319 ), 42: ( 59996, 0.5946040153503418 ), 43: ( 59996, 0.6299610137939453 ),
            44: ( 59996, 0.6674200296401978 ), 45: ( 59996, 0.7071070075035095 ), 46: ( 59996, 0.7491539716720581 ), 47: ( 59996, 0.7937009930610657 ),
            48: ( 59996, 0.8408970236778259 ), 49: ( 59996, 0.8908990025520325 ), 50: ( 59996, 0.9438750147819519 ), 51: ( 59996, 1.0 ),
            52: ( 59996, 1.0594630241394043 ), 53: ( 59996, 1.1224620342254639 ), 54: ( 59996, 1.1892069578170776 ), 55: ( 59996, 1.2599209547042847 ),
            56: ( 59996, 1.3348400592803955 ), 57: ( 59996, 1.414214015007019 ), 58: ( 59996, 1.4983069896697998 ), 59: ( 59996, 1.587401032447815 ),
            60: ( 59996, 1.681792974472046 ), 61: ( 59996, 1.781798005104065 ), 62: ( 59996, 1.8877489566802979 ), 63: ( 59996, 2.0 ),
        },
    },
    '0x24': {
        'instruments': {
            1: ( 0, 127, None, ( 8456, 0.39684998989105225 ), None ),
            3: ( 0, 127, None, ( 9533, 2.3784139156341553 ), None ),
            10: ( 30, 40, ( 36435, 4.0 ), ( 32149, 1.2599209547042847 ), ( 27693, 0.6299610137939453 ) ),
            11: ( 30, 40, ( 36435, 4.0 ), ( 32149, 1.2599209547042847 ), ( 27693, 0.6299610137939453 ) ),
            12: ( 0, 43, None, ( 23065, 2.1189260482788086 ), ( 23852, 0.5612310171127319 ) ),
            14: ( 0, 47, None, ( 27578, 0.75 ), ( 31472, 0.375 ) ),
        },
        'drums': {
        },
    },
}

import os
import shutil
import traceback
import sys
import re

import bcseq
import music_files
import n64_to_cseq

def find_unmappable_instruments( instruments, instrument_set ):
    """
    Returns a list of reasons a converted sequence does not have the right instruments on the 3DS. instruments is every
    instrument its channels selected while n64_to_cseq.py ran it. An empty list means every one has a 3DS equivalent.
    """

    use = { 'instruments': instruments }
    reasons = []

    synthesized = sorted( index for index in use[ 'instruments' ] if index >= 0x80 )
    if synthesized:
        reasons.append( 'it uses synthesized waves ' + str( [ hex( index ) for index in synthesized ] ) + ', which the 3DS does not have' )

    missing = sorted( index for index in use[ 'instruments' ] if index in instruments_missing_on_3ds.get( instrument_set, [] ) )
    if missing:
        reasons.append( 'instruments ' + str( missing ) + ' of instrument set ' + instrument_set + ' do not exist on the 3DS' )

    drums = drum_note_lookup.get( instrument_set )
    if 0x7F in use[ 'instruments' ] and ( drums is None or drums[ 'program' ] is None ):
        reasons.append( 'it uses drums, but instrument set ' + instrument_set + ' has no 3DS drum kit' )

    def has_mapping( index ):
        mapped = instrument_list_lookup.get( instrument_set, {} ).get( "0x{:02X}".format( index ) )
        # 0 is a valid index, so compare with "is" instead of "in ( None, False )"
        return mapped is not None and mapped is not False

    # 0x7F selects the drums
    unmapped = sorted( index for index in use[ 'instruments' ] if index < 0x7F and index not in missing and not has_mapping( index ) )
    if unmapped:
        reasons.append( 'instruments ' + str( unmapped ) + ' of instrument set ' + instrument_set + ' have no 3DS mapping' )

    return reasons

def is_cseq_note( command ):
    return re.fullmatch( r"[a-g][sn]m?\d+", command ) is not None

cseq_note_names = [ 'cn', 'cs', 'dn', 'ds', 'en', 'fn', 'fs', 'gn', 'gs', 'an', 'as', 'bn' ]

def cseq_note_to_key( command ):
    """
    Converts a .cseq note name to a MIDI key. "cn4" is key 60, and octaves below 0 use "m", so "cnm1" is key 0.
    """
    match = re.fullmatch( r"([a-g][sn])(m?)(\d+)", command )
    octave = -int( match.group(3) ) if match.group(2) else int( match.group(3) )
    return ( octave + 1 ) * 12 + cseq_note_names.index( match.group(1) )

def key_to_cseq_note( key ):
    octave = key // 12 - 1
    return cseq_note_names[ key % 12 ] + ( str( octave ) if octave >= 0 else 'm' + str( -octave ) )

def remap_cseq_instruments( cseq_path, instrument_set ):
    """
    Changes each "prg" from the N64 instrument index to the 3DS one, and moves each drum note to the 3DS drum kit key.

    On the N64, instrument 0x7F selects the drums, and drum N is played by note N. n64_to_cseq.py writes drum N as key N + 21.
    On the 3DS, the drum kit is the last instrument in the bank, and drum_note_lookup gives the key for each N64 drum.

    Returns a list of reasons the song cannot be converted. The file is only changed when the list is empty.
    """

    with open( cseq_path, 'r', encoding='utf-8' ) as file:
        lines = file.read().splitlines()

    instruments = instrument_list_lookup.get( instrument_set, {} )
    drums = drum_note_lookup.get( instrument_set )
    track_labels = set( re.findall( r"opentrack \d+, (\S+)", '\n'.join( lines ) ) )

    output = []
    problems = []
    unmapped_drums = set()
    n64_program = None

    for line in lines:

        stripped = line.strip()

        if stripped.endswith( ':' ) and stripped[:-1] in track_labels:
            n64_program = None
            output.append( line )
            continue

        command, _, arguments = stripped.partition( ' ' )

        if command == 'prg':

            n64_program = int( arguments )

            if n64_program == 0x7F:

                if drums is None or drums[ 'program' ] is None:
                    problems.append( 'instrument set ' + instrument_set + ' has drums, but its 3DS bank has no drum kit' )
                    continue

                output.append( '\tprg ' + str( drums[ 'program' ] ) )
                continue

            mapped = instruments.get( "0x{:02X}".format( n64_program ) )

            # 0 is a valid index, so compare with "is" instead of "not mapped"
            if mapped is None or mapped is False:
                problems.append( 'instrument ' + str( n64_program ) + ' of instrument set ' + instrument_set + ' has no 3DS mapping' )
                continue

            output.append( '\tprg ' + str( mapped ) )
            continue

        if n64_program == 0x7F and is_cseq_note( command ):

            drum = cseq_note_to_key( command ) - 21
            key = drums[ 'notes' ].get( drum ) if drums else None

            if key is None:
                unmapped_drums.add( drum )
                continue

            output.append( '\t' + key_to_cseq_note( key ) + ' ' + arguments )
            continue

        output.append( line )

    if unmapped_drums:
        problems.append( 'drums ' + str( sorted( unmapped_drums ) ) + ' of instrument set ' + instrument_set + ' have no 3DS drum kit key within 3 semitones' )

    if problems:
        return sorted( set( problems ) )

    with open( cseq_path, 'w', encoding='utf-8' ) as file:
        file.write( '\n'.join( output ) + '\n' )

    return []

def add_loop_to_cseq( cseq_path, loop_start, loop_end ):
    """
    n64_to_cseq.py writes every track as a straight run of commands that ends with "fin", so the song plays once and stops.

    This rewrites each track so that it plays up to loop_end and then jumps back to a label at loop_start. Commands
    that set a value (prg, volume, pan, tempo) and ran before loop_start are repeated after the label, so each pass
    through the loop starts with the same instrument, volume, pan and tempo as the first pass.

    Returns False and leaves the file unchanged if the file contains anything this does not handle.
    """

    if loop_end <= loop_start:
        return False

    with open( cseq_path, 'r', encoding='utf-8' ) as file:
        lines = file.read().splitlines()

    # Split into tracks. The main track has no label, every other track starts at the label given to its opentrack.
    header = []
    tracks = [] # [ label, [ command lines ] ]
    current = None

    for line in lines:

        stripped = line.strip()

        if not stripped or stripped.startswith( ';' ):
            if current is None:
                header.append( line )
            continue

        if stripped.endswith( ':' ):
            current = [ stripped[:-1], [] ]
            tracks.append( current )
            continue

        if current is None:
            current = [ None, [] ]
            tracks.append( current )

        current[1].append( stripped )

    setup_commands = ( 'alloctrack', 'opentrack', 'notewait_off' )

    output = list( header )

    for track_number, ( label, commands ) in enumerate( tracks ):

        loop_label = '_loop_track_' + str( track_number )

        setup = []
        events = [] # ( tick, command line )
        tick = 0

        for command_line in commands:

            command, _, arguments = command_line.partition( ' ' )

            if command == 'fin':
                break
            elif command == 'wait':
                tick += int( arguments )
            elif command in setup_commands:
                setup.append( command_line )
            elif command in ( 'notewait_on', 'jump', 'call', 'loop_start', 'loop_end', 'ret' ):
                # Notes advance time in notewait_on mode, and existing control flow would make the tick count wrong
                return False
            else:
                events.append( ( tick, command_line ) )

        if label is not None:
            output.append( '' )
            output.append( label + ':' )

        output.extend( '\t' + command_line for command_line in setup )

        state = {}
        tick = 0
        label_written = False

        def write_wait( until ):
            nonlocal tick
            if until > tick:
                output.append( '\twait ' + str( until - tick ) )
                tick = until

        def write_label():
            nonlocal label_written
            write_wait( loop_start )
            output.append( loop_label + ':' )
            output.extend( '\t' + command_line for command_line in state.values() )
            label_written = True

        for event_tick, command_line in events:

            if event_tick >= loop_end:
                break

            if not label_written and event_tick >= loop_start:
                write_label()

            command, _, arguments = command_line.partition( ' ' )

            if is_cseq_note( command ):
                # Shorten notes that would ring past the jump back to loop_start
                parts = arguments.split( ',' )
                parts[-1] = ' ' + str( min( int( parts[-1] ), loop_end - event_tick ) )
                command_line = command + ' ' + ','.join( parts ).strip()
            elif not label_written:
                state.pop( command, None )
                state[ command ] = command_line

            write_wait( event_tick )
            output.append( '\t' + command_line )

        if not label_written:
            write_label()

        write_wait( loop_end )
        output.append( '\tjump ' + loop_label )

    with open( cseq_path, 'w', encoding='utf-8' ) as file:
        file.write( '\n'.join( output ) + '\n' )

    return True

def convert_to_3d():

    if not os.path.exists( 'data/Music' ):
        print( 'No data/Music directory found' )
        return False

    os.makedirs( './tmp', exist_ok=True )
    os.makedirs( './Custom Music', exist_ok=True )

    songs = music_files.find_songs( 'data/Music' )

    failure_count = 0
    skipped_count = 0

    for song in songs:

        root = song.root
        seq_file = song.name + '.seq'

        if song.problem:
            print( song.path + ': ' + song.problem, file=sys.stderr )
            failure_count = failure_count + 1
            continue

        song_name, instrument_set, seq_type, seq_groups = song.meta()

        if instrument_set == '-':
            print( song.path + ': skipped, it brings its own instrument bank, and the 3DS can only use its own banks', file=sys.stderr )
            skipped_count = skipped_count + 1
            continue

        try:

            instrument_set = "0x{:02X}".format( int( instrument_set, 16 ) )

        except ValueError:

            print( song.path + ': the .meta file has no instrument set on its second line', file=sys.stderr )
            failure_count = failure_count + 1
            continue

        try:

            seq_path = song.seq_path( './tmp' )

        except Exception as e:

            print( song.path + ': could not read the .seq file: ' + repr( e ), file=sys.stderr )
            failure_count = failure_count + 1
            continue

        if instrument_set not in instrument_list_lookup:
            print( root + '/' + seq_file + ': instrument set ' + str( instrument_set ) + ' has no entry in instrument_list_lookup', file=sys.stderr )
            failure_count = failure_count + 1
            continue

        # Skip if already processed
        if not os.path.exists( './tmp/' + root + '/' + seq_file.replace( '.seq', '.bcseq' ) ) :

            os.makedirs( './tmp/' + root, exist_ok=True )

            cseq_path = './tmp/' + root + '/' + seq_file.replace( '.seq', '.cseq' )

            try:

                loop_ticks, unsupported, instruments = n64_to_cseq.convert( seq_path, cseq_path, sample_lookup.get( instrument_set ) )

            except Exception as e:
                print( root + '/' + seq_file + ': seq_to_cseq failure: ' + repr( e ), file=sys.stderr )
                failure_count = failure_count + 1
                continue

            if unsupported:
                print( root + '/' + seq_file + ': skipped, ' + unsupported, file=sys.stderr )
                skipped_count = skipped_count + 1
                continue

            unmappable = find_unmappable_instruments( instruments, instrument_set )

            if unmappable:
                print( root + '/' + seq_file + ': skipped, ' + '; '.join( unmappable ), file=sys.stderr )
                skipped_count = skipped_count + 1
                continue

            try:

                if loop_ticks and not add_loop_to_cseq( cseq_path, *loop_ticks ):
                    print( root + '/' + seq_file + ': could not add the loop, this song will play once', file=sys.stderr )

            except Exception as e:
                print( '.tmp/' + root + '/' + seq_file, file=sys.stderr )
                print( 'cseq loop failure', file=sys.stderr )
                print( e, file=sys.stderr )
                failure_count = failure_count + 1
                continue

            try:

                remap_problems = remap_cseq_instruments( './tmp/' + root + '/' + seq_file.replace( '.seq', '.cseq' ), instrument_set )

            except Exception as e:
                print( '.tmp/' + root + '/' + seq_file, file=sys.stderr )
                print( 'cseq instrument fix failure', file=sys.stderr )
                print( e, file=sys.stderr )
                failure_count = failure_count + 1
                continue

            if remap_problems:
                print( root + '/' + seq_file + ': skipped, ' + '; '.join( remap_problems ), file=sys.stderr )
                skipped_count = skipped_count + 1
                continue

            try:

                bcseq.assemble_file( cseq_path, './tmp/' + root + '/' + seq_file.replace( '.seq', '.bcseq' ) )

            except Exception as e:
                print( root + '/' + seq_file + ': cseq_to_bcseq failure: ' + repr( e ), file=sys.stderr )
                failure_count = failure_count + 1
                continue

        os.makedirs( './Converted/' + root, exist_ok=True )

        shutil.copy( './tmp/' + root + '/' + seq_file.replace( '.seq', '.bcseq' ), './Converted/' + root )

        sound_bank = instrument_set_lookup.get( instrument_set )

        # Bank 0 is valid, so only skip sets with no entry
        if sound_bank is not None:

            # The OoT3D Randomizer reads .cmeta as "key=value" text lines (source/custom_music/cmeta_interpreter.cpp)
            cmeta = open( './tmp/' + root + '/' + seq_file.replace( '.seq', '.cmeta' ), 'w', encoding='utf-8' )

            cmeta.write( 'banks=' + str( sound_bank ) + '\n' )

            cmeta.close()

            shutil.copy( './tmp/' + root + '/' + seq_file.replace( '.seq', '.cmeta' ), './Converted/' + root )

    print( "%d failed" % failure_count )
    print( "%d skipped" % skipped_count )

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
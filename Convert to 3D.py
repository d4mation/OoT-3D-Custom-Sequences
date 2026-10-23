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
3DS drum kit program and key for each N64 drum, generated by "Generate Drum Lookup.py" from the MQ debug ROM and the
3DS QueenSound.bcsar banks.

Each N64 drum maps to the 3DS key that plays the same sample at the nearest pitch, up to 3 semitones away. Many N64 drum
pitches do not exist on the 3DS, and the 3DS game's own sequences also play those drums 1 - 3 semitones off. See
PITCH_TOLERANCE in "Generate Drum Lookup.py" for the numbers behind this. None means no 3DS key is within 3 semitones,
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

import os
import subprocess
import shutil
import traceback
import sys
import re
import xml.etree.ElementTree as ElementTree

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

"""
Byte length (opcode included) of each command that can appear in an N64 sequence header, from abi/4b - Zelda community only.xml

0xFD (delay) is not listed because its length depends on its argument
"""
seq_header_command_lengths = {
    0xC4: 3, 0xC5: 3, 0xC6: 1, 0xC7: 4, 0xC8: 2, 0xC9: 2, 0xCC: 2, 0xCD: 3, 0xCE: 2,
    0xD0: 2, 0xD1: 3, 0xD2: 3, 0xD3: 2, 0xD4: 1, 0xD5: 2, 0xD6: 3, 0xD7: 3, 0xD9: 2,
    0xDA: 4, 0xDB: 2, 0xDC: 2, 0xDD: 2, 0xDE: 2, 0xDF: 2, 0xEF: 4, 0xF0: 1, 0xF1: 2,
    0xF2: 2, 0xF3: 2, 0xF4: 2, 0xF5: 3, 0xF6: 1, 0xF7: 1, 0xF8: 2, 0xF9: 3, 0xFA: 3,
    0xFB: 3, 0xFC: 3, 0xFE: 1, 0xFF: 1,
}

for opcode in range( 0x00, 0x10 ):
    seq_header_command_lengths[ opcode ] = 1 # testchan
for opcode in range( 0x40, 0x60 ):
    seq_header_command_lengths[ opcode ] = 1 # stopchan, subio
for opcode in range( 0x60, 0x70 ):
    seq_header_command_lengths[ opcode ] = 3 # loadbank
for opcode in range( 0x70, 0x90 ):
    seq_header_command_lengths[ opcode ] = 1 # stio, ldio
for opcode in range( 0x90, 0xB0 ):
    seq_header_command_lengths[ opcode ] = 3 # startchan, rstartchan
for opcode in range( 0xB0, 0xC0 ):
    seq_header_command_lengths[ opcode ] = 4 # loadseq

def find_loop_ticks( seq_path ):
    """
    An N64 sequence loops by ending its sequence header with a jump (0xFB) or relative jump (0xF4) back to an earlier
    offset in the header. The header starts each channel and then waits with delay commands, so the tick at which the
    jump target was first reached is the loop start, and the tick at which the jump runs is the loop end.

    seq64 ignores this jump when it exports a MIDI file, so the loop is lost unless it is added back afterwards.

    Returns ( loop_start, loop_end ) in ticks (48 per quarter note, the same as in the .cseq), or None if the
    sequence ends without looping.
    """

    with open( seq_path, 'rb' ) as file:
        data = file.read()

    position = 0
    tick = 0
    first_reached = {}
    stack = [] # ( 'call', return position ) or ( 'loop', loop body position, iterations left )

    for _ in range( 100000 ):

        if position >= len( data ):
            return None

        if not stack:
            first_reached.setdefault( position, tick )

        opcode = data[ position ]

        if opcode == 0xFD:
            length = 3 if data[ position + 1 ] & 0x80 else 2
        else:
            length = seq_header_command_lengths.get( opcode )

        if length is None:
            return None

        next_position = position + length

        if opcode == 0xFD: # delay
            if length == 3:
                tick += ( data[ position + 1 ] & 0x7F ) << 8 | data[ position + 2 ]
            else:
                tick += data[ position + 1 ]

        elif opcode == 0xFC: # call
            stack.append( ( 'call', next_position ) )
            next_position = data[ position + 1 ] << 8 | data[ position + 2 ]

        elif opcode == 0xF8: # loop, where a count of 0 means 256
            stack.append( ( 'loop', next_position, data[ position + 1 ] or 256 ) )

        elif opcode == 0xF7: # loopend
            if not stack or stack[-1][0] != 'loop':
                return None

            kind, loop_body, iterations_left = stack[-1]

            if iterations_left > 1:
                stack[-1] = ( kind, loop_body, iterations_left - 1 )
                next_position = loop_body
            else:
                stack.pop()

        elif opcode in ( 0xFB, 0xF4 ): # jump, rjump
            if opcode == 0xFB:
                target = data[ position + 1 ] << 8 | data[ position + 2 ]
            else:
                offset = data[ position + 1 ]
                target = next_position + ( offset - 256 if offset > 127 else offset )

            if not stack and target in first_reached:
                return first_reached[ target ], tick

            next_position = target

        elif opcode == 0xFF: # end, or return from a call
            if not stack:
                return None

            next_position = stack.pop()[1]

        # Conditional branches (0xF2, 0xF3, 0xF5, 0xF9, 0xFA) are treated as not taken, which is what seq64 does

        position = next_position

    return None

def signed_byte( value ):
    value &= 0xFF
    return value - 256 if value > 127 else value

def fill_with_no_ops( data, start, end ):
    """
    Overwrites data[ start:end ] with sequence header commands that do nothing, keeping every other address in place:
    stprel 0 (0xDE 0x00, 2 bytes), disablechan (0xD6, 3 bytes, a no-op in the game) and unreservenotes (0xF0, 1 byte).
    """
    length = end - start
    filler = b''
    if length % 2:
        filler = b'\xD6\x00\x00' if length >= 3 else b'\xF0'
    filler += b'\xDE\x00' * ( ( length - len( filler ) ) // 2 )
    data[ start:end ] = filler

def linearize_sequence_header( data ):
    """
    Some sequences (the Majora's Mask fanfares) run a small program in the sequence header before starting their
    channels: they read a game I/O value (ldio), branch on it, and write the result into their own commands (sts). seq64
    reads the header in a straight line and stops at the first jump, so it exports a MIDI file with no notes.

    This runs the header the way OoT does, where every I/O value starts at -1, and rewrites it into that straight line:
    sts writes are applied to the bytes they target, and the commands that only decide which path to take (I/O, Q
    register math, branches and forward jumps), plus the bytes a taken branch skips, are replaced with commands that do
    nothing. Addresses do not move. The jump back to an earlier position, which loops the song, is kept.

    Returns the rewritten sequence, the original data if the header has no such program, or None if it uses something
    this cannot follow (random values, channel tests, calls, loops, or writes outside the header path).
    """

    data = bytearray( data )
    io = [ -1 ] * 8
    q = 0
    position = 0
    executed = []
    dynamic = []
    skipped = []
    writes = {}

    for _ in range( 10000 ):

        if position >= len( data ):
            return None

        opcode = data[ position ]

        if opcode == 0xFD:
            length = 3 if data[ position + 1 ] & 0x80 else 2
        else:
            length = seq_header_command_lengths.get( opcode )

        if length is None:
            return None

        if any( start == position for start, _ in executed ):
            # Reached a command a second time without a jump back, which means the header loops through a branch
            return None

        executed.append( ( position, length ) )
        next_position = position + length
        argument = data[ position + 1 ] if length > 1 else 0

        if opcode in ( 0xCE, 0xFC, 0xF8, 0xF7, 0xCD ) or opcode <= 0x0F:
            # rand, call, loop, loopend, dyncall and testchan depend on state this does not track. A header that uses
            # them without any of the commands this rewrites is left as it is, which seq64 already reads correctly.
            return None if dynamic else bytes( data )

        if 0x80 <= opcode <= 0x8F: # ldio
            index = opcode & 0x0F
            q = io[ index ] if index < len( io ) else -1
            if index < 2:
                io[ index ] = -1
            dynamic.append( position )
        elif 0x70 <= opcode <= 0x7F: # stio
            if ( opcode & 0x0F ) < len( io ):
                io[ opcode & 0x0F ] = q
            dynamic.append( position )
        elif 0x50 <= opcode <= 0x5F: # subio
            q = signed_byte( q - ( io[ opcode & 0x0F ] if ( opcode & 0x0F ) < len( io ) else -1 ) )
            dynamic.append( position )
        elif opcode == 0xCC: # ldi
            q = signed_byte( argument )
            dynamic.append( position )
        elif opcode == 0xC8: # sub
            q = signed_byte( q - argument )
            dynamic.append( position )
        elif opcode == 0xC9: # and
            q = signed_byte( q & argument )
            dynamic.append( position )
        elif opcode == 0xC7: # sts: data[ address ] = Q + immediate
            address = data[ position + 2 ] << 8 | data[ position + 3 ]
            writes[ address ] = ( q + data[ position + 1 ] ) & 0xFF
            data[ address ] = writes[ address ]
            dynamic.append( position )
        elif opcode in ( 0xF2, 0xF3, 0xF4, 0xF5, 0xF9, 0xFA, 0xFB ):

            if opcode in ( 0xF2, 0xF3, 0xF4 ):
                target = next_position + signed_byte( argument )
            else:
                target = data[ position + 1 ] << 8 | data[ position + 2 ]

            taken = {
                0xF2: q < 0, 0xF3: q == 0, 0xF4: True,
                0xF5: q >= 0, 0xF9: q < 0, 0xFA: q == 0, 0xFB: True,
            }[ opcode ]

            if taken and target <= position:
                # The jump back that loops the song
                if opcode not in ( 0xF4, 0xFB ):
                    return None
                break

            dynamic.append( position )

            if taken:
                skipped.append( ( next_position, target ) )
                next_position = target

        elif opcode == 0xFF:
            break

        position = next_position

    else:
        return None

    if not dynamic:
        return bytes( data )

    kept = [ ( start, length ) for start, length in executed if start not in dynamic ]

    for address in writes:
        # A write must land inside a command that is kept, or it would be overwritten by the filler
        if not any( start < address < start + length for start, length in kept ):
            return None

    for start in dynamic:
        length = next( length for begin, length in executed if begin == start )
        fill_with_no_ops( data, start, start + length )

    for start, end in skipped:
        if any( start <= begin < end for begin, length in kept ):
            return None
        fill_with_no_ops( data, start, end )

    return bytes( data )

def load_abi_commands( abi_path ):
    """
    Reads the command lengths from a seq64 ABI file.

    Returns { stype: { opcode: ( name, action, first opcode, [ ( datasrc, datalen, meaning ) ] ) } }, where stype 0 is
    the sequence header, 1 is a channel and 2 is a note layer.
    """

    tables = { 0: {}, 1: {}, 2: {} }

    for command in ElementTree.parse( abi_path ).getroot().iter( 'command' ):

        first = int( command.get( 'cmd' ) )
        last = int( command.get( 'cmdend', first ) )
        parameters = [ ( p.get( 'datasrc' ), int( p.get( 'datalen' ) or 0 ), p.get( 'meaning' ) ) for p in command.findall( 'parameter' ) ]

        for stype, attribute in ( ( 0, 'validinseq' ), ( 1, 'validinchn' ), ( 2, 'validintrk' ) ):
            if command.get( attribute ) == '1':
                for opcode in range( first, last + 1 ):
                    tables[ stype ].setdefault( opcode, ( command.get( 'name' ), command.get( 'action' ), first, parameters ) )

    return tables

abi_commands = None

def find_used_instruments( seq_path ):
    """
    Follows the sequence header into every channel and note layer, and records the commands that pick an instrument:
    instr (0xC1) and bankinstr (0xEB) in channels, and linst (0xC6) in note layers.

    Returns a dict with:
    - instruments: instrument indices set by instr or bankinstr
    - banks: instrument sets switched to by bankinstr
    - layer_instruments: instrument indices set by linst, which seq64 does not export
    - complete: False if part of the sequence could not be followed (dynamic tables, short notes or unknown commands)
    """

    global abi_commands

    if abi_commands is None:
        abi_commands = load_abi_commands( './abi/4b - Zelda community only.xml' )

    with open( seq_path, 'rb' ) as file:
        data = file.read()

    result = { 'instruments': set(), 'banks': set(), 'layer_instruments': set(), 'complete': True }
    todo = [ ( 0, 0 ) ]
    seen = set()

    while todo:

        position, stype = todo.pop()

        while position < len( data ) and ( position, stype ) not in seen:

            seen.add( ( position, stype ) )

            command = abi_commands[ stype ].get( data[ position ] )

            if command is None:
                result[ 'complete' ] = False
                break

            name, action, first, parameters = command
            length = 1
            values = []

            for datasrc, datalen, meaning in parameters:
                if datasrc == 'fixed':
                    values.append( ( int.from_bytes( data[ position + length:position + length + datalen ], 'big' ), datalen, meaning ) )
                    length += datalen
                elif datasrc == 'variable':
                    if data[ position + length ] & 0x80:
                        values.append( ( ( data[ position + length ] & 0x7F ) << 8 | data[ position + length + 1 ], 2, meaning ) )
                        length += 2
                    else:
                        values.append( ( data[ position + length ], 1, meaning ) )
                        length += 1
                elif datasrc == 'offset':
                    values.append( ( data[ position ] - first, 0, meaning ) )

            next_position = position + length
            target = None

            for value, datalen, meaning in values:
                if meaning == 'Absolute Address':
                    target = value
                elif meaning == 'Relative Address':
                    target = next_position + ( value - ( 1 << ( 8 * datalen ) ) if value >= 1 << ( 8 * datalen - 1 ) else value )

            if stype == 1 and data[ position ] == 0xC1:
                result[ 'instruments' ].add( values[0][0] )
            elif stype == 1 and data[ position ] == 0xEB:
                result[ 'banks' ].add( values[0][0] )
                result[ 'instruments' ].add( values[1][0] )
            elif stype == 2 and data[ position ] == 0xC6:
                result[ 'layer_instruments' ].add( values[0][0] )

            if action in ( 'Set Short Notes', 'Set Dyntable', 'Channel from Dyntable', 'Layer from Dyntable', 'Dyntable from Dyntable', 'Seq Hdr Call Table' ):
                result[ 'complete' ] = False

            if action == 'Ptr Channel Header' and target is not None:
                todo.append( ( target, 1 ) )
            elif action == 'Ptr Note Layer' and target is not None:
                todo.append( ( target, 2 ) )
            elif action in ( 'Call', 'Branch' ) and target is not None:
                todo.append( ( target, stype ) )
            elif action == 'Jump' and target is not None:
                todo.append( ( target, stype ) )
                break
            elif action == 'End of Data':
                break

            position = next_position

    return result

def find_unmappable_instruments( seq_path, instrument_set ):
    """
    Returns a list of reasons this sequence cannot be converted with the right instruments. An empty list means every
    instrument it uses has a 3DS equivalent.
    """

    use = find_used_instruments( seq_path )
    reasons = []

    if not use[ 'complete' ]:
        reasons.append( 'part of the sequence could not be read to check its instruments' )

    other_banks = sorted( "0x{:02X}".format( bank ) for bank in use[ 'banks' ] if "0x{:02X}".format( bank ) != instrument_set )
    if other_banks:
        reasons.append( 'it switches to instrument sets ' + ', '.join( other_banks ) + ' with bankinstr' )

    if use[ 'layer_instruments' ]:
        reasons.append( 'it sets instruments ' + str( sorted( use[ 'layer_instruments' ] ) ) + ' in note layers, which seq64 does not export' )

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

    On the N64, instrument 0x7F selects the drums, and drum N is played by note N. seq64 writes drum N as MIDI key N + 21.
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

def end_cseq_tracks( cseq_path ):
    """
    Adds "fin" to the end of every track that has neither "fin" nor "jump".

    In some songs that do not loop, midi2sseq ends a track after its last command without "fin", so the 3DS would keep
    reading past the end of that track.
    """

    with open( cseq_path, 'r', encoding='utf-8' ) as file:
        lines = file.read().splitlines()

    track_labels = set( re.findall( r"opentrack \d+, (\S+)", '\n'.join( lines ) ) )
    output = []
    ended = True

    for line in lines:

        stripped = line.strip()

        if stripped.endswith( ':' ) and stripped[:-1] in track_labels:
            if not ended:
                output.append( '\tfin' )
            ended = False
            output.append( line )
            continue

        if stripped and not stripped.startswith( ';' ):
            command = stripped.split()[0]
            if command == 'fin' or command == 'jump':
                ended = True
            elif not stripped.endswith( ':' ):
                ended = False

        output.append( line )

    if not ended:
        output.append( '\tfin' )

    with open( cseq_path, 'w', encoding='utf-8' ) as file:
        file.write( '\n'.join( output ) + '\n' )

def add_loop_to_cseq( cseq_path, loop_start, loop_end ):
    """
    midi2sseq writes every track as a straight run of commands that ends with "fin", so the song plays once and stops.

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

"""
Seconds each conversion tool may run for one song. midi2sseq never finishes on some MIDI files, such as one with no
notes, and without a limit it stops the whole run.
"""
tool_timeout = 120

def convert_to_3d():

    if not os.path.exists( 'data/Music' ):
        print( 'No data/Music directory found' )
        return False

    os.makedirs( './tmp', exist_ok=True )
    os.makedirs( './Custom Music', exist_ok=True )

    songs = os.walk( 'data/Music' )

    failure_count = 0
    skipped_count = 0

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

                print( root + '/' + seq_file + ': could not read the .meta file: ' + str( e ), file=sys.stderr )
                failure_count = failure_count + 1
                continue

            if instrument_set not in instrument_list_lookup:
                print( root + '/' + seq_file + ': instrument set ' + str( instrument_set ) + ' has no entry in instrument_list_lookup', file=sys.stderr )
                failure_count = failure_count + 1
                continue

            try:

                unmappable = find_unmappable_instruments( './' + root + '/' + seq_file, instrument_set )

            except Exception as e:
                print( root + '/' + seq_file + ': could not check the instruments: ' + str( e ), file=sys.stderr )
                failure_count = failure_count + 1
                continue

            if unmappable:
                print( root + '/' + seq_file + ': skipped, ' + '; '.join( unmappable ), file=sys.stderr )
                skipped_count = skipped_count + 1
                continue

            # Skip if already processed
            if not os.path.exists( './tmp/' + root + '/' + seq_file.replace( '.seq', '.bcseq' ) ) :

                os.makedirs( './tmp/' + root, exist_ok=True )

                # seq64 and find_loop_ticks read this copy, with the sequence header rewritten into a straight line
                linear_seq_path = './tmp/' + root + '/' + seq_file

                with open( './' + root + '/' + seq_file, 'rb' ) as original:
                    linear_seq = linearize_sequence_header( original.read() )

                if linear_seq is None:
                    print( root + '/' + seq_file + ': skipped, its sequence header uses commands that cannot be rewritten for seq64', file=sys.stderr )
                    skipped_count = skipped_count + 1
                    continue

                with open( linear_seq_path, 'wb' ) as linear:
                    linear.write( linear_seq )

                try:

                    seq_to_midi = subprocess.run(
                        './seq64_console.exe --abi=4b --in="' + linear_seq_path + '" --out="./tmp/' + root + '/' + seq_file.replace( '.seq', '.mid' ) + '"',
                        check=True,
                        text=True,
                        capture_output=True,
                        timeout=tool_timeout
                    )

                except Exception as e:
                    print( root + '/' + seq_file )
                    print( 'seq_to_midi failure' )
                    # FileNotFoundError has no output attribute, and TimeoutExpired has output None
                    print( getattr( e, 'output', None ) or e )
                    failure_count = failure_count + 1
                    continue

                try:

                    midi_to_sseq = subprocess.run(
                        './midi2sseq.exe "./tmp/' + root + '/' + seq_file.replace( '.seq', '.mid' ) + '" "./tmp/' + root + '/' + seq_file.replace( '.seq', '.sseq' ) + '"',
                        check=True,
                        text=True,
                        capture_output=True,
                        timeout=tool_timeout
                    )

                except Exception as e:
                    print( '.tmp/' + root + '/' + seq_file )
                    print( 'midi_to_sseq failure' )
                    # FileNotFoundError has no output attribute, and TimeoutExpired has output None
                    print( getattr( e, 'output', None ) or e )
                    failure_count = failure_count + 1
                    continue

                try:

                    # We change the extension during this command to skip a step
                    sseq_to_cseq = subprocess.run(
                        './SequenceConvert.exe "./tmp/' + root + '/' + seq_file.replace( '.seq', '.sseq' ) + '" "./tmp/' + root + '/' + seq_file.replace( '.seq', '.cseq' ) + '"',
                        check=True,
                        text=True,
                        capture_output=True,
                        timeout=tool_timeout
                    )

                except Exception as e:
                    print( '.tmp/' + root + '/' + seq_file )
                    print( 'sseq_to_cseq failure' )
                    # FileNotFoundError has no output attribute, and TimeoutExpired has output None
                    print( getattr( e, 'output', None ) or e )
                    failure_count = failure_count + 1
                    continue

                try:

                    loop_ticks = find_loop_ticks( linear_seq_path )

                    if loop_ticks and not add_loop_to_cseq( './tmp/' + root + '/' + seq_file.replace( '.seq', '.cseq' ), *loop_ticks ):
                        print( root + '/' + seq_file + ': could not add the loop, this song will play once', file=sys.stderr )
                        loop_ticks = None

                    if not loop_ticks:
                        end_cseq_tracks( './tmp/' + root + '/' + seq_file.replace( '.seq', '.cseq' ) )

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

                    cseq_to_bcseq = subprocess.run(
                        './SequenceConvert.exe "./tmp/' + root + '/' + seq_file.replace( '.seq', '.cseq' ) + '" "./tmp/' + root + '/' + seq_file.replace( '.seq', '.bcseq' ) + '"',
                        check=True,
                        text=True,
                        capture_output=True,
                        timeout=tool_timeout
                    )

                except Exception as e:
                    print( '.tmp/' + root + '/' + seq_file )
                    print( 'cseq_to_bcseq failure' )
                    # FileNotFoundError has no output attribute, and TimeoutExpired has output None
                    print( getattr( e, 'output', None ) or e )
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
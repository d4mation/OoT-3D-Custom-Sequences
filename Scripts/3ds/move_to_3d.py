"""
OoT3D and OoT64 Randomizers handle this a bit differently, so we'll use this to try to convert between the two
"""
location_lookup = {
    'low': {
        'Overworld': [
            'Background Music/Area Themes/Overworld',
        ],
        'Dungeon': [
            'Background Music/Area Themes/Dungeons'
        ],
        'Fight': [
            'Background Music/Battle Themes',
        ],
        'CharacterTheme': [
            'Background Music/Event Music/Title Screen',
            "Background Music/Event Music/Zelda's Theme",
            "Background Music/Event Music/Sheik's Theme",
            'Background Music/Event Music/Deku Tree Storytime',
            "Background Music/Event Music/Owl's Theme",
            'Background Music/Event Music/Navi Intro',
            "Background Music/Event Music/Ganondorf's Theme",
            "Background Music/Event Music/Kotake & Koume",
            "Background Music/Event Music/Ingo's Theme",
        ],
        'EventFanfare': [
            "Melodies/Fanfares/Item Jingles/Item Get",
            "Melodies/Fanfares/Item Jingles/Heart Container Get",
            "Melodies/Fanfares/Item Jingles/Spiritual Stone Get",
            "Melodies/Fanfares/Item Jingles/Small Item Get",
            "Melodies/Fanfares/Item Jingles/Medallion Get",
            "Melodies/Fanfares/Item Jingles/Song Learned",
            "Melodies/Fanfares/Misc Fanfares/Boss Clear",
            "Melodies/Fanfares/Misc Fanfares/Horse Goal",
            "Melodies/Fanfares/Misc Fanfares/Event Clear",
            "Melodies/Fanfares/Misc Fanfares/Appearance",
            "Melodies/Fanfares/Item Jingles/Treasure Chest Opening",
            "Melodies/Fanfares/Misc Fanfares/Master Sword",
            "Melodies/Fanfares/Misc Fanfares/Door of Time Opened",
            "Melodies/Fanfares/Misc Fanfares/Ganon Appears",
            "Melodies/Fanfares/Misc Fanfares/Game Over"
        ],
        'SongFanfare': [
            "Melodies/Ocarina Songs/Warp Songs/Prelude of Light",
            "Melodies/Ocarina Songs/Warp Songs/Bolero of Fire",
            "Melodies/Ocarina Songs/Warp Songs/Minuet of Forest",
            "Melodies/Ocarina Songs/Warp Songs/Serenade of Water",
            "Melodies/Ocarina Songs/Warp Songs/Requiem of Spirit",
            "Melodies/Ocarina Songs/Warp Songs/Nocture of Shadow", # The OoT3D Randomizer spells this folder "Nocture" in source/music.cpp
            "Melodies/Ocarina Songs/Child Songs/Saria's Song",
            "Melodies/Ocarina Songs/Child Songs/Epona's Song",
            "Melodies/Ocarina Songs/Child Songs/Zelda's Lullaby",
            "Melodies/Ocarina Songs/Child Songs/Song of Time",
            "Melodies/Ocarina Songs/Child Songs/Song of Storms",
            # No Sun's Song: the OoT3D Randomizer comments out its "Sun's Song" folder in source/music.cpp ("Still unshuffled because of bugs")
        ]
    },
    'medium': {
        'Outdoors': [
            'Background Music/Area Themes/Overworld/Hyrule Field',
            'Background Music/Area Themes/Overworld/Lost Woods',
            'Background Music/Area Themes/Overworld/Gerudo Valley',
            'Background Music/Area Themes/Overworld/Market',
            'Background Music/Area Themes/Overworld/Kakariko Child',
            'Background Music/Area Themes/Overworld/Kakariko Adult',
            'Background Music/Area Themes/Overworld/Lon Lon Ranch',
            'Background Music/Area Themes/Overworld/Kokiri Forest',
            'Background Music/Area Themes/Overworld/Goron City',
            "Background Music/Area Themes/Overworld/Zora's Domain",
        ],
        'Indoors': [
            'Background Music/Event Music/Minigame Theme 2',
            'Background Music/Event Music/File Select',
            'Background Music/Area Themes/Interiors/Fairy Fountain',
            'Background Music/Area Themes/Interiors/Temple of Time',
            'Background Music/Event Music/Goddess Theme',
            'Background Music/Area Themes/Interiors/House Theme',
            'Background Music/Area Themes/Interiors/Shop Theme',
            'Background Music/Area Themes/Interiors/Drugstore',
            'Background Music/Area Themes/Interiors/Windmill',
        ],
        'ChildDungeon': [
            'Background Music/Area Themes/Dungeons/Deku Tree',
            'Background Music/Area Themes/Dungeons/Misc Dungeon',
            'Background Music/Area Themes/Dungeons/Jabu Jabu',
        ],
        'AdultDungeon': [
            'Background Music/Area Themes/Dungeons/Forest Temple',
            'Background Music/Area Themes/Dungeons/Fire Temple',
            'Background Music/Area Themes/Dungeons/Water Temple',
            'Background Music/Area Themes/Dungeons/Spirit Temple',
            'Background Music/Area Themes/Dungeons/Shadow Temple',
            "Background Music/Area Themes/Dungeons/Ganon's Castle",
            'Background Music/Event Music/Tower Escape',
        ],
        'SmallFight': [
            'Background Music/Battle Themes/Enemy Theme',
            'Background Music/Battle Themes/Mini Boss',
        ],
        'BigFight': [
            'Background Music/Battle Themes/Boss Themes/Boss Theme 1',
            'Background Music/Battle Themes/Boss Themes/Boss Theme 2',
            'Background Music/Battle Themes/Ganondorf Battle',
            'Background Music/Battle Themes/Ganon Battle',
        ],
        'HeroTheme': [
            'Background Music/Event Music/Title Screen',
            "Background Music/Event Music/Zelda's Theme",
            "Background Music/Event Music/Sheik's Theme",
            'Background Music/Event Music/Deku Tree Storytime',
            "Background Music/Event Music/Owl's Theme",
            'Background Music/Event Music/Navi Intro',
        ],
        'VillainTheme': [
            "Background Music/Event Music/Ganondorf's Theme",
            "Background Music/Event Music/Kotake & Koume",
            "Background Music/Event Music/Ingo's Theme",
        ],
        'ItemFanfare': [
            "Melodies/Fanfares/Item Jingles/Item Get",
            "Melodies/Fanfares/Item Jingles/Heart Container Get",
            "Melodies/Fanfares/Item Jingles/Spiritual Stone Get",
            "Melodies/Fanfares/Item Jingles/Small Item Get",
            "Melodies/Fanfares/Item Jingles/Medallion Get",
            "Melodies/Fanfares/Item Jingles/Song Learned",
        ],
        'SuccessFanfare': [
            "Melodies/Fanfares/Misc Fanfares/Boss Clear",
            "Melodies/Fanfares/Misc Fanfares/Horse Goal",
            "Melodies/Fanfares/Misc Fanfares/Event Clear",
            "Melodies/Fanfares/Misc Fanfares/Appearance",
        ],
        'BigFanfare': [
            "Melodies/Fanfares/Item Jingles/Treasure Chest Opening",
            "Melodies/Fanfares/Misc Fanfares/Master Sword",
            "Melodies/Fanfares/Misc Fanfares/Door of Time Opened",
            "Melodies/Fanfares/Misc Fanfares/Ganon Appears",
        ],
        'GameOver': [
            "Melodies/Fanfares/Misc Fanfares/Game Over",
        ],
        'WarpSong': [
            "Melodies/Ocarina Songs/Warp Songs/Prelude of Light",
            "Melodies/Ocarina Songs/Warp Songs/Bolero of Fire",
            "Melodies/Ocarina Songs/Warp Songs/Minuet of Forest",
            "Melodies/Ocarina Songs/Warp Songs/Serenade of Water",
            "Melodies/Ocarina Songs/Warp Songs/Requiem of Spirit",
            "Melodies/Ocarina Songs/Warp Songs/Nocture of Shadow", # The OoT3D Randomizer spells this folder "Nocture" in source/music.cpp
        ],
        'UtilitySong': [
            "Melodies/Ocarina Songs/Child Songs/Saria's Song",
            "Melodies/Ocarina Songs/Child Songs/Epona's Song",
            "Melodies/Ocarina Songs/Child Songs/Zelda's Lullaby",
            "Melodies/Ocarina Songs/Child Songs/Song of Time",
            "Melodies/Ocarina Songs/Child Songs/Song of Storms",
            # No Sun's Song: the OoT3D Randomizer comments out its "Sun's Song" folder in source/music.cpp ("Still unshuffled because of bugs")
        ]
    },
    'high': {
        'Fields': [
            'Background Music/Area Themes/Overworld/Hyrule Field',
            'Background Music/Area Themes/Overworld/Lost Woods',
            'Background Music/Area Themes/Overworld/Gerudo Valley',
        ],
        'Town': [
            'Background Music/Area Themes/Overworld/Market',
            'Background Music/Area Themes/Overworld/Kakariko Child',
            'Background Music/Area Themes/Overworld/Kakariko Adult',
            'Background Music/Area Themes/Overworld/Lon Lon Ranch',
            'Background Music/Area Themes/Overworld/Kokiri Forest',
            'Background Music/Area Themes/Overworld/Goron City',
            "Background Music/Area Themes/Overworld/Zora's Domain",
            'Background Music/Event Music/Castle Courtyard',
        ],
        'Fun': [
            'Background Music/Event Music/Horse Race',
            'Background Music/Event Music/Minigame Theme 1',
            'Background Music/Event Music/Minigame Theme 2',
        ],
        'MagicalPlace': [
            'Background Music/Event Music/File Select',
            'Background Music/Area Themes/Interiors/Fairy Fountain',
            'Background Music/Area Themes/Interiors/Temple of Time',
            'Background Music/Event Music/Goddess Theme',
        ],
        'House': [
            'Background Music/Area Themes/Interiors/House Theme',
        ],
        'SalesArea': [
            'Background Music/Area Themes/Interiors/Shop Theme',
            'Background Music/Area Themes/Interiors/Drugstore',
        ],
        'WindmillHut': [
            'Background Music/Area Themes/Interiors/Windmill',
        ],
        'AncientDungeon': [
            'Background Music/Area Themes/Dungeons/Forest Temple',
            'Background Music/Area Themes/Dungeons/Fire Temple',
        ],
        'MysticalDungeon': [
            'Background Music/Area Themes/Dungeons/Ice Cavern',
            'Background Music/Area Themes/Dungeons/Water Temple',
            'Background Music/Area Themes/Dungeons/Spirit Temple',
        ],
        'SpookyDungeon': [
            'Background Music/Area Themes/Dungeons/Shadow Temple',
            "Background Music/Area Themes/Dungeons/Ganon's Castle",
            'Background Music/Event Music/Tower Escape',
        ],
        'BossFight': [
            'Background Music/Battle Themes/Boss Themes/Boss Theme 1',
            'Background Music/Battle Themes/Boss Themes/Boss Theme 2',
        ],
        'FinalFight': [
            'Background Music/Battle Themes/Ganondorf Battle',
            'Background Music/Battle Themes/Ganon Battle',
        ]
    },
    'exact': {
        'HyruleField': 'Background Music/Area Themes/Overworld/Hyrule Field',
        'LostWoods': 'Background Music/Area Themes/Overworld/Lost Woods',
        'GerudoValley': 'Background Music/Area Themes/Overworld/Gerudo Valley',
        'Market': 'Background Music/Area Themes/Overworld/Market',
        'KakarikoChild': 'Background Music/Area Themes/Overworld/Kakariko Child',
        'KakarikoAdult': 'Background Music/Area Themes/Overworld/Kakariko Adult',
        'LonLonRanch': 'Background Music/Area Themes/Overworld/Lon Lon Ranch',
        'KokiriForest': 'Background Music/Area Themes/Overworld/Kokiri Forest',
        'GoronCity': 'Background Music/Area Themes/Overworld/Goron City',
        'ZorasDomain': "Background Music/Area Themes/Overworld/Zora's Domain",
        'CastleCourtyard': 'Background Music/Event Music/Castle Courtyard',
        'HorseRace': 'Background Music/Event Music/Horse Race',
        'Mini-game': 'Background Music/Event Music/Minigame Theme 1',
        'ShootingGallery': 'Background Music/Event Music/Minigame Theme 2',
        # On N64, NA_BGM_FILE_SELECT points to the NA_BGM_GREAT_FAIRY sequence. The 3DS has a separate file for each.
        'FairyFountain': [
            'Background Music/Area Themes/Interiors/Fairy Fountain',
            'Background Music/Event Music/File Select',
        ],
        'TempleOfTime': 'Background Music/Area Themes/Interiors/Temple of Time',
        'ChamberOfTheSages': 'Background Music/Event Music/Goddess Theme',
        'House': 'Background Music/Area Themes/Interiors/House Theme',
        'Shop': 'Background Music/Area Themes/Interiors/Shop Theme',
        'PotionShop': 'Background Music/Area Themes/Interiors/Drugstore',
        'WindmillHut': 'Background Music/Area Themes/Interiors/Windmill',
        'InsideDekuTree': 'Background Music/Area Themes/Dungeons/Deku Tree',
        'DodongosCavern': 'Background Music/Area Themes/Dungeons/Misc Dungeon',
        'JabuJabu': 'Background Music/Area Themes/Dungeons/Jabu Jabu',
        'ForestTemple': 'Background Music/Area Themes/Dungeons/Forest Temple',
        'FireTemple': 'Background Music/Area Themes/Dungeons/Fire Temple',
        'IceCavern': 'Background Music/Area Themes/Dungeons/Ice Cavern',
        'WaterTemple': 'Background Music/Area Themes/Dungeons/Water Temple',
        'SpiritTemple': 'Background Music/Area Themes/Dungeons/Spirit Temple',
        'ShadowTemple': 'Background Music/Area Themes/Dungeons/Shadow Temple',
        'CastleUnderground': "Background Music/Area Themes/Dungeons/Ganon's Castle",
        'CastleEscape': 'Background Music/Event Music/Tower Escape',
        'Battle': 'Background Music/Battle Themes/Enemy Theme',
        'MinibossBattle': 'Background Music/Battle Themes/Mini Boss',
        'BossBattle': 'Background Music/Battle Themes/Boss Themes/Boss Theme 1',
        'FireBoss': 'Background Music/Battle Themes/Boss Themes/Boss Theme 2',
        'GanondorfBattle': 'Background Music/Battle Themes/Ganondorf Battle',
        'GanonBattle': 'Background Music/Battle Themes/Ganon Battle',
        'TitleTheme': 'Background Music/Event Music/Title Screen',
        'ZeldaTheme': "Background Music/Event Music/Zelda's Theme",
        'SheikTheme': "Background Music/Event Music/Sheik's Theme",
        'DekuTree': 'Background Music/Event Music/Deku Tree Storytime',
        'KaeporaGaebora': "Background Music/Event Music/Owl's Theme",
        'FairyFlying': 'Background Music/Event Music/Navi Intro',
        'GanondorfTheme': "Background Music/Event Music/Ganondorf's Theme",
        'KotakeAndKoume': "Background Music/Event Music/Kotake & Koume",
        'IngoTheme': "Background Music/Event Music/Ingo's Theme",
        'ItemGet': "Melodies/Fanfares/Item Jingles/Item Get",
        'HeartContainerGet': "Melodies/Fanfares/Item Jingles/Heart Container Get",
        'SpiritStoneGet': "Melodies/Fanfares/Item Jingles/Spiritual Stone Get",
        'HeartPieceGet': "Melodies/Fanfares/Item Jingles/Small Item Get",
        'MedallionGet': "Melodies/Fanfares/Item Jingles/Medallion Get",
        'LearnSong': "Melodies/Fanfares/Item Jingles/Song Learned",
        'BossDefeated': "Melodies/Fanfares/Misc Fanfares/Boss Clear",
        'EponaRaceGoal': "Melodies/Fanfares/Misc Fanfares/Horse Goal",
        'EscapeFromRanch': "Melodies/Fanfares/Misc Fanfares/Event Clear",
        'ZeldaTurnsAround': "Melodies/Fanfares/Misc Fanfares/Appearance",
        'TreasureChest': "Melodies/Fanfares/Item Jingles/Treasure Chest Opening",
        'MasterSword': "Melodies/Fanfares/Misc Fanfares/Master Sword",
        'DoorOfTime': "Melodies/Fanfares/Misc Fanfares/Door of Time Opened",
        'GanondorfAppears': "Melodies/Fanfares/Misc Fanfares/Ganon Appears",
        'GameOver': "Melodies/Fanfares/Misc Fanfares/Game Over",
        'PreludeOfLight': "Melodies/Ocarina Songs/Warp Songs/Prelude of Light",
        'BoleroOfFire': "Melodies/Ocarina Songs/Warp Songs/Bolero of Fire",
        'MinuetOfForest': "Melodies/Ocarina Songs/Warp Songs/Minuet of Forest",
        'SerenadeOfWater': "Melodies/Ocarina Songs/Warp Songs/Serenade of Water",
        'RequiemOfSpirit': "Melodies/Ocarina Songs/Warp Songs/Requiem of Spirit",
        'NocturneOfShadow': "Melodies/Ocarina Songs/Warp Songs/Nocture of Shadow", # The OoT3D Randomizer spells this folder "Nocture" in source/music.cpp
        'SariasSong': "Melodies/Ocarina Songs/Child Songs/Saria's Song",
        'EponasSong': "Melodies/Ocarina Songs/Child Songs/Epona's Song",
        'ZeldasLullaby': "Melodies/Ocarina Songs/Child Songs/Zelda's Lullaby",
        'SongOfTime': "Melodies/Ocarina Songs/Child Songs/Song of Time",
        'SongOfStorms': "Melodies/Ocarina Songs/Child Songs/Song of Storms",
        'SunsSong': None, # The OoT3D Randomizer comments out its "Sun's Song" folder in source/music.cpp ("Still unshuffled because of bugs")
    }
}

# The levels of location_lookup, from the most specific to the broadest
levels = [ 'exact', 'high', 'medium', 'low' ]

import argparse
import os
import re
import shutil
import sys
import unicodedata

import music_files

def node_path( directory ):
    """
    The OoT3D Randomizer only reads a folder as a music category when its name starts with "!"
    (MusicCategoryNode::GetFullPath in source/custom_music/sequence_data.cpp), so
    "Background Music/Area Themes" becomes "!Background Music/!Area Themes"
    """
    return '/'.join( '!' + part for part in directory.split( '/' ) )

def ascii_folder_name( song_name ):
    """
    Returns the song name as an ASCII folder name. The OoT3D Randomizer opens sequence files with
    fsMakePath( PATH_ASCII, ... ) (source/custom_music/ctr_binary_data.cpp), so a path with other characters would
    not be found. Accents are dropped, slashes become "-", and other characters a folder name cannot have are removed.
    """
    text = unicodedata.normalize( 'NFKD', song_name )
    text = ''.join( character for character in text if not unicodedata.combining( character ) )
    text = re.sub( r'[/\\∕]', '-', text )
    text = ''.join( character for character in text if character.isascii() and character.isprintable() and character not in ':*?"<>|' )
    # FAT does not allow a folder name to end with a dot or a space
    return re.sub( r'\s+', ' ', text ).strip().rstrip( '. ' ) or 'Song'

def assign_folder_names( converted ):
    """
    Returns { converted .bcseq path: folder name }. Songs from different games often share a file name (such as Main
    Theme.bcseq), so each song's folder is named by its key, the first line of its .meta file. Songs whose keys give
    the same folder name get " 2", " 3", ... in path order.
    """
    names = {}
    used = set()
    for path, song_name in sorted( converted ):
        base = ascii_folder_name( song_name )
        name = base
        number = 2
        while name.lower() in used:
            name = base + ' ' + str( number )
            number += 1
        used.add( name.lower() )
        names[ path ] = name
    return names

def copy_song( bcseq_path, folder_name, directory ):
    """
    Copies the song into its own folder, named folder_name, inside the category folder, as track.bcseq and track.cmeta,
    so the songs of a category are listed by name.

    The OoT3D Randomizer reads the folders inside a category folder whose names do not start with "!" and adds their
    songs to that category (MusicCategoryNode::AddExternalSeqDatas in source/custom_music/sequence_data.cpp). It only
    uses the file names to pair each .bcseq with the .cmeta of the same name, so the files have the same short name in
    every folder.

    This does not make the randomizer faster. For each .bcseq, it lists the folder again to find the .cmeta, but
    libctru reads 32 directory entries per file system call, so the old layout of one folder per category made about
    as many calls (about 41,000 for 6177 copies) as this one (about 44,000), where each song adds two folder opens.
    """

    # A folder whose name starts with "!" is read as a category instead
    destination = './Custom Music/' + node_path( directory ) + '/' + folder_name.lstrip( '!' )

    os.makedirs( destination, exist_ok=True )

    shutil.copy( bcseq_path, destination + '/track.bcseq' )

    cmeta_path = bcseq_path[:-len( '.bcseq' )] + '.cmeta'

    if os.path.exists( cmeta_path ) :

        shutil.copy( cmeta_path, destination + '/track.cmeta' )

def read_song_list( path ):
    """
    Returns the song keys in a song list written by Scripts/Generate Song List.py, where each song is a line
    "key: <song name>" and the song name is the first line of the song's .meta file. Lines that are not keys (the folder
    names) are ignored.
    """

    keys = set()

    with open( path, 'r', encoding='utf-8-sig' ) as song_list_file:
        for line in song_list_file:
            line = line.strip()
            if line.startswith( 'key:' ):
                # Generate Song List.py keeps the byte order mark that starts some .meta files in their key
                keys.add( line[ len( 'key:' ): ].strip().lstrip( '\ufeff' ) )

    return keys

def song_directories( groups, broadest_level='exact' ):
    """
    Returns the Custom Music folders for a song's groups.

    The folders come from the song's most specific level: its exact groups if it has any, otherwise its high groups,
    then its medium groups, then its low groups. A group whose folders the 3DS does not have, such as SunsSong, does not
    count. With broadest_level, the folders of the levels from that most specific level through broadest_level are
    used together, so 'low' uses every level. A song whose most specific level is broader than broadest_level uses
    only that level.
    """

    directories_by_level = []

    for level in levels:

        directories = []

        for group in groups:

            group_directories = location_lookup[ level ].get( group )

            if isinstance( group_directories, str ):
                group_directories = [ group_directories ]

            for directory in group_directories or []:

                if directory not in directories:
                    directories.append( directory )

        directories_by_level.append( directories )

    most_specific = next( ( index for index, directories in enumerate( directories_by_level ) if directories ), None )

    if most_specific is None:
        return []

    broadest = max( most_specific, levels.index( broadest_level ) )
    result = []

    for directories in directories_by_level[ most_specific:broadest + 1 ]:

        for directory in directories:

            if directory not in result:
                result.append( directory )

    return result

def move_to_3d( song_list_path=None, broadest_level='exact' ):
    """
    Copies the converted songs into the Custom Music folders of their groups. With song_list_path, only the songs whose
    keys are in that song list are copied. broadest_level is passed to song_directories().
    """

    if not os.path.exists( 'Converted/data/Music' ):
        print( 'No Converted/data/Music directory found' )
        return False

    keys = None

    if song_list_path is not None:

        if not os.path.exists( song_list_path ):
            print( 'No song list found at ' + song_list_path )
            return False

        keys = read_song_list( song_list_path )
        found_keys = set()

    # The .meta file of each converted song, from its .seq and .meta files or its .ootrs archive in data/Music
    songs_by_path = { song.path: song for song in music_files.find_songs( 'data/Music' ) }

    # Each song to copy: ( .bcseq path, song name, type, groups )
    to_copy = []

    songs = os.walk( 'Converted/data/Music' )

    for root, dirs, files in songs: 

        root = root.replace( os.sep, '/' )

        for seq_file in files:

            if not seq_file.endswith( '.bcseq' ):
                continue

            song = songs_by_path.get( root.replace( 'Converted/', '', 1 ) + '/' + seq_file[:-len( '.bcseq' )] )

            if song is None or song.problem:
                print( root + '/' + seq_file + ': could not read the .meta file of this song in data/Music', file=sys.stderr )
                continue

            song_name, instrument_set, seq_type, seq_groups = song.meta()

            if keys is not None:

                if song_name not in keys:
                    continue

                found_keys.add( song_name )

            to_copy.append( ( root + '/' + seq_file, song_name, seq_type, seq_groups ) )

    folder_names = assign_folder_names( [ ( bcseq_path, song_name ) for bcseq_path, song_name, seq_type, seq_groups in to_copy ] )

    # Songs with no groups that were not copied because broadest_level is not 'low'
    skipped_without_groups = 0

    for bcseq_path, song_name, seq_type, seq_groups in to_copy:

        # A song with no groups gets a low group as its default, so it is only copied when the low level is used
        if not seq_groups:

            if broadest_level != 'low':

                skipped_without_groups += 1
                continue

            if seq_type == 'bgm':

                seq_groups = [ 'Overworld' ]

            else:

                seq_groups = [ 'EventFanfare' ]

        for group in seq_groups:

            if not any( group in level for level in location_lookup.values() ):
                print( bcseq_path + ': unknown group ' + group, file=sys.stderr )

        directories = song_directories( seq_groups, broadest_level )

        if not directories:
            print( bcseq_path + ': no 3DS folder for the groups ' + ','.join( seq_groups ), file=sys.stderr )

        # Copy the generated files into the correct locations
        for directory in directories:

            copy_song( bcseq_path, folder_names[ bcseq_path ], directory )

    if skipped_without_groups:
        print( str( skipped_without_groups ) + ' songs with no groups were not copied. Use --level low to copy them.' )

    if keys is not None:

        # These songs were skipped or failed in convert_to_3d.py, or their key is spelled differently in the list
        for key in sorted( keys - found_keys ):
            print( song_list_path + ': no converted song has the key ' + key, file=sys.stderr )

        print( str( len( found_keys ) ) + ' of the ' + str( len( keys ) ) + ' songs in ' + song_list_path + ' have been organized' )

    return True

def main():

    # Usage, from the repository root: python Scripts/3ds/move_to_3d.py [--level exact|high|medium|low] [song list]
    parser = argparse.ArgumentParser( description='Copies the converted songs into the Custom Music folders of their groups.' )
    parser.add_argument( 'song_list', nargs='?', help='a song list from Generate Song List.py. Only the songs with a key line in it are copied.' )
    parser.add_argument( '--level', choices=levels, default='exact',
                         help="the broadest group level to use. The default, exact, uses only each song's most specific groups. low uses all of them, and also copies the songs with no groups." )
    arguments = parser.parse_args()

    moved_to_3d = move_to_3d( arguments.song_list, arguments.level )

    if moved_to_3d:
        print("All songs have been organized for Oot3D Rando")
        print("")
    else:
        print("An error occured moving songs")
    input("Press enter to quit.")


if __name__ == '__main__':
    main()
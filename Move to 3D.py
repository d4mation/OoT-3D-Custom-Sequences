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
            "Melodies/Fanfares/Item Jingles/Spritual Stone Get",
            "Melodies/Fanfares/Item Jingles/Item Get",
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
            "Melodies/Ocarina Songs/Warp Songs/Nocture of Shadow", # Typo? The directory is "Nocture" instead of "Nocturne"
            "Melodies/Ocarina Songs/Child Songs/Saria's Song",
            "Melodies/Ocarina Songs/Child Songs/Epona's Song",
            "Melodies/Ocarina Songs/Child Songs/Zelda's Lullaby",
            "Melodies/Ocarina Songs/Child Songs/Sun's Song", # This directory is actually missing? Assuming it is a bug with the CIA creating the directories
            "Melodies/Ocarina Songs/Child Songs/Song of Time",
            "Melodies/Ocarina Songs/Child Songs/Song of Storms",
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
            "Background Music/Area Themes/Dungeons/Ganon's Tower",
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
            "Melodies/Fanfares/Item Jingles/Spritual Stone Get",
            "Melodies/Fanfares/Item Jingles/Item Get",
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
            "Melodies/Ocarina Songs/Warp Songs/Nocture of Shadow", # Typo? The directory is "Nocture" instead of "Nocturne"
        ],
        'UtilitySong': [
            "Melodies/Ocarina Songs/Child Songs/Saria's Song",
            "Melodies/Ocarina Songs/Child Songs/Epona's Song",
            "Melodies/Ocarina Songs/Child Songs/Zelda's Lullaby",
            "Melodies/Ocarina Songs/Child Songs/Sun's Song", # This directory is actually missing? Assuming it is a bug with the CIA creating the directories
            "Melodies/Ocarina Songs/Child Songs/Song of Time",
            "Melodies/Ocarina Songs/Child Songs/Song of Storms",
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
            "Background Music/Area Themes/Dungeons/Ganon's Tower",
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
        'FairyFountain': 'Background Music/Event Music/File Select',
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
        'CastleUnderground': "Background Music/Area Themes/Dungeons/Ganon's Tower",
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
        'SpritStoneGet': "Melodies/Fanfares/Item Jingles/Spritual Stone Get",
        'HeartPieceGet': "Melodies/Fanfares/Item Jingles/Item Get",
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
        'NocturneOfShadow': "Melodies/Ocarina Songs/Warp Songs/Nocture of Shadow", # Typo? The directory is "Nocture" instead of "Nocturne"
        'SariasSong': "Melodies/Ocarina Songs/Child Songs/Saria's Song",
        'EponasSong': "Melodies/Ocarina Songs/Child Songs/Epona's Song",
        'ZeldasLullaby': "Melodies/Ocarina Songs/Child Songs/Zelda's Lullaby",
        'SunsSong': "Melodies/Ocarina Songs/Child Songs/Sun's Song", # This directory is actually missing? Assuming it is a bug with the CIA creating the directories
        'SongOfTime': "Melodies/Ocarina Songs/Child Songs/Song of Time",
        'SongOfStorms': "Melodies/Ocarina Songs/Child Songs/Song of Storms",
    }
}

import os
import shutil

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

def move_to_3d():

    if not os.path.exists( 'Converted/data/Music' ):
        print( 'No Converted/data/Music directory found' )
        return False

    songs = os.walk( 'Converted/data/Music' )

    for root, dirs, files in songs: 

        for seq_file in files:

            if seq_file.endswith( '.cmeta' ):
                continue

            seq_type = 'bgm'
            seq_groups = []

            try:

                song_name, instrument_set, seq_type, seq_groups = parse_meta_file( root.replace( 'Converted/', '' ), seq_file.replace( '.bcseq', '.meta' ) )
            
            except Exception as e:
                print( e.output )

            # Try to set some defaults, just in case
            if not seq_groups: 

                if seq_type == 'bgm':

                    seq_groups = [ 'Overworld' ]

                else:

                    seq_groups = [ 'EventFanfare' ]

            # Copy the generated files into the correct locations
            for group in seq_groups:

                low = location_lookup.get( 'low' ).get( group )
                medium = location_lookup.get( 'medium' ).get( group )
                high = location_lookup.get( 'high' ).get( group )
                exact = location_lookup.get( 'exact' ).get( group )

                if low:

                    for directory in low:

                        os.makedirs( './Custom Music/' + directory, exist_ok=True )

                        shutil.copy( './' + root + '/' + seq_file, './Custom Music/' + directory )

                        if os.path.exists( './' + root + '/' + seq_file.replace( '.bcseq', '.cmeta' ) ) :

                            shutil.copy( './' + root + '/' + seq_file.replace( '.bcseq', '.cmeta' ), './Custom Music/' + directory )

                if medium:

                    for directory in medium:

                        os.makedirs( './Custom Music/' + directory, exist_ok=True )

                        shutil.copy( './' + root + '/' + seq_file, './Custom Music/' + directory )

                        if os.path.exists( './' + root + '/' + seq_file.replace( '.bcseq', '.cmeta' ) ) :

                            shutil.copy( './' + root + '/' + seq_file.replace( '.bcseq', '.cmeta' ), './Custom Music/' + directory )

                if high:

                    for directory in high:

                        os.makedirs( './Custom Music/' + directory, exist_ok=True )

                        shutil.copy( './' + root + '/' + seq_file, './Custom Music/' + directory )

                        if os.path.exists( './' + root + '/' + seq_file.replace( '.bcseq', '.cmeta' ) ) :

                            shutil.copy( './' + root + '/' + seq_file.replace( '.bcseq', '.cmeta' ), './Custom Music/' + directory )

                if exact:

                    os.makedirs( './Custom Music/' + exact, exist_ok=True )

                    shutil.copy( './' + root + '/' + seq_file, './Custom Music/' + exact )

                    if os.path.exists( './' + root + '/' + seq_file.replace( '.bcseq', '.cmeta' ) ) :

                        shutil.copy( './' + root + '/' + seq_file.replace( '.bcseq', '.cmeta' ), './Custom Music/' + exact )

    return True

def main():

    moved_to_3d = move_to_3d()

    if moved_to_3d:
        print("All songs have been organized for Oot3D Rando")
        print("")
    else:
        print("An error occured moving songs")
    input("Press enter to quit.")


if __name__ == '__main__':
    main()
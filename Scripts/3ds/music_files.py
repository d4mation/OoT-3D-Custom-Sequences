"""
Finds the songs in a music folder, in either of the two formats in data/Music:
- a .seq file with a .meta file of the same name
- an .ootrs file, a zip archive with one .seq file and one .meta file, and for songs with their own instrument bank also
  .zbank, .bankmeta and .zsound files

The .meta file has one value per line:
1. the song name
2. the N64 instrument set, such as 0x03, or - for a song that brings its own instrument bank
3. the type, bgm or fanfare (in any letter case)
4. optional: the comma-separated music groups, or - for none
Lines after these (such as the ZSOUND lines of a custom bank) are not used here.
"""

import os
import zipfile


class Song:
    """
    One song. root is its folder (such as data/Music/Banjo-Kazooie Series/Banjo-Kazooie) and name is its file name
    without the extension, which is also the name of its converted .bcseq.
    """

    def __init__( self, root, name, source ):
        self.root = root
        self.name = name
        # The .seq file, or the .ootrs archive that holds it
        self.source = source
        self.problem = None
        self.meta_lines = []
        self._seq_member = None

    @property
    def path( self ):
        return self.root + '/' + self.name

    def seq_path( self, tmp_folder ):
        """
        Returns a path to the song's .seq file. A .seq file in an .ootrs archive is extracted into tmp_folder first.
        """
        if self._seq_member is None:
            return self.source
        os.makedirs( tmp_folder + '/' + self.root, exist_ok=True )
        path = tmp_folder + '/' + self.root + '/' + self.name + '.seq'
        with zipfile.ZipFile( self.source ) as archive:
            with open( path, 'wb' ) as file:
                file.write( archive.read( self._seq_member ) )
        return path

    def meta( self ):
        """
        Returns ( song name, instrument set, type, groups ), where the instrument set is a string such as '0x03' or '-',
        the type is lowercase, and groups is a list
        """
        lines = [ line.strip() for line in self.meta_lines ]
        song_name = lines[0] if lines else self.name
        instrument_set = lines[1] if len( lines ) >= 2 else ''
        seq_type = lines[2].lower() if len( lines ) >= 3 and lines[2] else 'bgm'
        groups = []
        if len( lines ) >= 4 and lines[3] != '-':
            groups = [ group.strip() for group in lines[3].split( ',' ) if group.strip() ]
        return song_name, instrument_set, seq_type, groups


def decode_meta( data ):
    # Some .meta files start with a UTF-8 byte order mark
    return data.decode( 'utf-8-sig' ).splitlines()


def find_songs( music_folder ):
    """
    Returns every song under music_folder, sorted by path. A song whose files cannot be read has problem set.
    """

    songs = []

    for root, dirs, files in os.walk( music_folder ):

        root = root.replace( os.sep, '/' )

        for file in files:

            base, extension = os.path.splitext( file )
            extension = extension.lower()

            if extension == '.seq':

                song = Song( root, base, root + '/' + file )
                # Some .meta files differ from their .seq file only in letter case, which Windows ignores and Linux
                # does not
                meta = next( ( name for name in files if name.lower() == base.lower() + '.meta' ), None )
                if meta is None:
                    song.problem = 'it has no .meta file'
                else:
                    with open( root + '/' + meta, 'rb' ) as meta_file:
                        song.meta_lines = decode_meta( meta_file.read() )
                songs.append( song )

            elif extension == '.ootrs':

                song = Song( root, base, root + '/' + file )
                try:
                    with zipfile.ZipFile( song.source ) as archive:
                        members = [ name for name in archive.namelist() if not name.endswith( '/' ) ]
                        seqs = [ name for name in members if name.lower().endswith( '.seq' ) ]
                        metas = [ name for name in members if name.lower().endswith( '.meta' ) ]
                        if len( seqs ) != 1 or len( metas ) != 1:
                            song.problem = 'the .ootrs archive has ' + str( len( seqs ) ) + ' .seq and ' + str( len( metas ) ) + ' .meta files instead of one of each'
                        else:
                            song._seq_member = seqs[0]
                            song.meta_lines = decode_meta( archive.read( metas[0] ) )
                except zipfile.BadZipFile:
                    song.problem = 'the .ootrs file is not a zip archive'
                songs.append( song )

    return sorted( songs, key=lambda song: song.path )

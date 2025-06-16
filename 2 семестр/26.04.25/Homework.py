class Artist:
    def __init__(self, name):
        self.name = name
        self.albums = []

    def add_album(self, album):
        self.albums.append(album)


class Album:
    def __init__(self, name, year, artist: Artist):
        self.album_name = name
        self.year = year
        self.artist = artist
        self.songs = []

        self.artist.add_album(self)

    def add_song(self, song):
        self.songs.append(song)


class Song:
    def __init__(self, name, seconds, album: Album):
        self.song_name = name
        self.seconds = seconds
        self.album = album
        self.album.add_song(self)


class Playlist:
    def __init__(self, name):
        self.name = name
        self.songs = []

    def add_song(self, song):
        self.songs.append(song)

import ipdb

class Song:

    count = 0 
    genres = []
    genre_count = {}  # Initialize genre_count with each genre set to 0
    artists = []
    artist_count = {}
        
    def __init__(self, name='', artist='', genre=''):
        self.name = name
        self.artist = artist
        self.genre = genre
        Song.add_song_to_count()
        Song.add_to_genres(genre)
        Song.add_to_artists(artist)
        Song.add_to_genre_count(genre)
        Song.add_to_artist_count(artist)

        
    @classmethod
    def add_song_to_count(cls):
        Song.count += 1

    @classmethod
    def add_to_genres(cls,genre):
        if genre not in cls.genres:
            cls.genres.append(genre)

    @classmethod
    def add_to_artists(cls, artist):
        if artist not in cls.artists:
            cls.artists.append(artist)

    @classmethod
    def add_to_genre_count(cls, genre):
        # Increment the count for the genre
        if genre in cls.genre_count:
            cls.genre_count[genre] += 1
        else:
            cls.genre_count[genre] = 1

    @classmethod
    def add_to_artist_count(cls, artist):
           # Increment the count for the artist
        if artist in cls.artist_count:
            cls.artist_count[artist] += 1
        else:
            cls.artist_count[artist] = 1

        
        # Example usage
        # song1 = Song(name='99 Problems', artist='Jay Z', genre='Rap')
        # song2 = Song(name='Halo', artist='Beyonce', genre='Pop')
        # song3 = Song(name='Smells Like Teen Spirit', artist='Nirvana', genre='Rock')

        
        
 



    # ipdb.set_trace()
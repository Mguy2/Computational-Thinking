from typing import Dict, List
from categories import *
import csv
import random


# *********************************************************************
# The next lines are about:
# CLASSES:
# - Song()
# - Playlist()
# - User()
# *********************************************************************


class Song():
    # NOTE: adjust the constructor method with the required song parameters
    def __init__(self, title, artist, genre, year, song_bpm,
                song_energy, song_d_ability, song_db, song_liveness,
                song_valence, song_length, song_accoustic, song_speech):
        self.id = id(self)
        self.title = title
        self.artist = artist
        self.genre = genre
        self.cat_genre = ""
        self.year = int(year)
        self.bpm = int(song_bpm)
        self.energy = int(song_energy)
        self.danceability = int(song_d_ability)
        self.db = int(song_db)
        self.liveness = int(song_liveness)
        self.valence = int(song_valence)
        self.length = int(song_length)
        self.accoustic = int(song_accoustic)
        self.speech = int(song_speech)

    def list_attributes(self) -> Dict[str, any]:
        return vars(self)

    def set_rock(self) -> None:
        self.cat_genre = "rock"
    
    def set_pop(self) -> None:
        self.cat_genre = "pop"
        
    def set_techno(self) -> None:
        self.cat_genre = "techno"

    def __repr__(self):
        return f"TITLE: {self.title}"
    # Control what info is displayed when we execute "print(Song)"
    def __str__(self):
        return f"TITLE: {self.title}" #| ARTIST: {self.artist} | GENRE: {self.genre} | YEAR: {self.year}"


class Playlist():
    def __init__(self, name: str, song_list: List[Song] = []):
        self.name = name
        self.listed_songs = song_list

    # Control what info is displayed when we execute "print(Playlist)"
    def __str__(self):
        return f"<{self.name.upper()}> contains {len(self.listed_songs)} songs."


class User():
    def __init__(self, songs_listened: List[Song] = []):
        self.id = id(self)
        self.songs_listened = songs_listened
        self.songs_recommended = []
        self.pop = 0
        self.rock = 0
        self.techno = 0
        
    def extend_recommendation(self, rec_list :List[Song]):
        self.songs_recommended.extend(rec_list)
        
    def change_preferences(self, preferences :tuple):
        self.pop = preferences[0]
        self.rock = preferences[1]
        self.techno = preferences[2]
        
    def attributes(self):
        return [self.id, self.pop, self.rock, self.techno] + self.songs_listened + self.songs_recommended
        
    def listened_to_recommend(self, success_rate :float) -> None:
        nr = int((len(self.songs_recommended) * 0.5))
        self.songs_listened.extend(random.sample(self.songs_recommended, nr))


# *********************************************************************
# The next lines are about:
# FUNCTIONS:
# - create_songs: to create 603 song objects from the spotify songs csv file
# - create_playlists: create 100 playlists with 50 songs each
# - recommend_songs: selects five songs to recommend to the user
# *********************************************************************


# Function to create songs from a csv file
def create_songs():
    """
    Creates a list of song objects from a songs csv file
    :return:
    """
    # Change the path to the desired csv file
    path = "Data/spotify-dataset.csv"

    source_file_list = []  # Here we will add all lines from the csv file
    song_list = []  # Here we will add all song objects

    # Reads the csv file and adds its rows to a list
    with open(path, newline='', encoding='utf-8-sig') as f:
        reader = csv.reader(f)
        for row in reader:
            source_file_list.append(row)

    # Loop over all songs and collect the song info from the list 
    # Why not loop? this is solely for readability purposes. :)
    for song in source_file_list[1:]:
        song_title = song[0]
        song_artist = song[1]
        song_genre = song[2]
        song_year = song[3]
        song_bpm = song[4]
        song_energy = song[5]
        song_d_ability = song[6]
        song_db = song[7]
        song_liveness = song[8]
        song_valence = song[9]
        song_length = song[10]
        song_accoustic = song[11]
        song_speech = song[12]
    
        # Create a new song object with the parameters defined in the song class constructor method
        new_song = Song(song_title, song_artist, song_genre, song_year, song_bpm,
                        song_energy, song_d_ability, song_db, song_liveness,
                        song_valence, song_length, song_accoustic, song_speech)

        # Add the song to the overall song list (the song database)
        song_list.append(new_song)

    # Return the song list
    return song_list


# Function to create playlists
def create_random_playlists(songs :List[Song]) -> List[Song]:
    """
    Creates a new playlist with 50 randomly chosen songs from our songs-database
    :return:
    """
    list_of_playlists = []  # Here we will add all the created playlist objects
    # Create a new playlist containing the list of 50 random songs from above
    for i in range(1,101):
        # Create a  list of 50 songs randomly chosen from our list of all songs
        song_list = random.sample(songs, 50)
        new_playlist = Playlist(f"Playlist #{i}", song_list)
        # Add the new playlist to the list of all playlists
        list_of_playlists.append(new_playlist)
    # Return the list containing all playlists
    return list_of_playlists


def create_genre_playlists(songs :List[Song]) -> List[Playlist]:
    genre_playlists = {}
    output = []
    for song in songs:
        genre_playlists[song.genre] = genre_playlists.get(song.genre, []) + [song]
    for playlist in genre_playlists.keys():
        output.append(Playlist(playlist, genre_playlists[playlist]))
    return output


def create_cat_playlist(songs :List[Song]) -> List[Playlist]:
    cat_genre_playlists = {}
    output = []
    for song in songs:
        cat_genre_playlists[song.cat_genre] = cat_genre_playlists.get(song.cat_genre, []) + [song]
    for playlist in cat_genre_playlists.keys():
        output.append(Playlist(playlist, cat_genre_playlists[playlist]))
    return output


def find_categories(songs :List[Song]) -> List[str]:
    list_of_categories = []
    for song in songs:
        if song.genre not in list_of_categories:
            list_of_categories.append(str(song.genre))
    return list_of_categories


def categorize_genre(songs :List[Song]) -> None:
    for song in songs:
        if song.genre in rock:
            song.set_rock()
        if song.genre in pop:
            song.set_pop()
        if song.genre in techno:
            song.set_techno()
            
            
# def custom_playlist(play_list_name :str, playlist_max_song :int, songs :List[Song],
#                     artist :str = "", genre :str = "", year :tuple = (0, 3000),
#                     bpm :tuple = (0, 0), energy :tuple = (0, 0), danceability :tuple = (0, 0), db :tuple = (0, 0),
#                     liveness :tuple = (0, 0), valence :tuple = (0, 0), length :tuple = (0, 0), accoustic :tuple = (0, 0),
#                     speech :tuple = (0, 0)):
#     min_song = Song("min_song", artist, genre, year[0], bpm[0], energy[0], danceability[0],
#                     db[0], liveness[0], valence[0], length[0], accoustic[0], speech[0])
#     max_song = Song("min_song", artist, genre, year[1], bpm[1], energy[1], danceability[1],
#                     db[1], liveness[1], valence[1], length[1], accoustic[1], speech[1])
#     output_list = []
#     min_attr = min_song.list_attributes()
#     max_attr = max_song.list_attributes()
#     for song in songs:
#         song_attr = song.list_attributes()
#         shared_items = {shared: min_attr[shared] for shared in min_attr if shared in song_attr and min_attr[shared] == song_attr[shared]}
#         print(shared_items)
#     return Playlist(play_list_name, output_list)



###################################################################
# Creating a hard-coded test user
# This user gets a number of fixed songs from the all_songs list


def test_user(songs :List[Song], song_nr :int) -> User:
    user_A_songs = songs[0:song_nr]
    user_A = User(user_A_songs)
    #print(user_A.songs_listened[1].title)
    # Test to see if the songs stay the same and we can access info for each song
   # for song in user_A.songs_listened:
        #print("TITLE:", song.title, "| GENRE:", song.genre)
    return user_A


def create_users(songs :List[Song] = create_songs(), user_nr :int = 100, listened_to_nr :int = 5) -> List[User]:
    user_list = []
    # Create 100 users and add them to a list containing all user objects
    for _ in range(user_nr + 1):
        new_user_songs = random.sample(songs, listened_to_nr)
        new_user = User(new_user_songs)
        user_list.append(new_user)
    # Return the list containing all users
    return user_list


###################################################################


# *********************************************************************
# The next lines are about:
# SIMULATING A USER's LISTENING BEHAVIOR
# - We will need to populate each user's "has_listened_to" list attribute
#   with some songs, in order to have something for the algorithm to work with
# *********************************************************************


# *********************************************************************
# The next lines are about:
# EXECUTING TASKS 1-3
# - Run the necessary functions and methods to solve each task of the project
# - e.g.
# *********************************************************************


# *********************************************************************
# The next lines are about:
# TESTING THE CODE
# (...)
# *********************************************************************







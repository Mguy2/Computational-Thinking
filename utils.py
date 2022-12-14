from typing import Dict, List
from classes import *
import csv
import random

# **************************************************************************
# This file contains the code for various general functions.

# NOTE: functions that only relate to the task of a specific week
# (i.e. week 1-3) are listed in the separate week1, week2, week3 modules.
# **************************************************************************



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

        # Define the mood of this song based on the song's attributes (e.g. energy, valence)
        new_song.define_mood()

        # Add the song to the overall song list (the song database)
        song_list.append(new_song)

    # Return the song list
    return song_list


# Function to create users
def create_users(songs: List[Song] = create_songs(), user_nr: int = 100, listened_to_nr: int = 5) -> List[User]:
    user_list = []
    # Create 100 users and add them to a list containing all user objects
    for _ in range(user_nr + 1):
        new_user_songs = random.sample(songs, listened_to_nr)
        new_user = User(new_user_songs)
        user_list.append(new_user)
    # Return the list containing all users
    return user_list


# Function to create playlists
def create_random_playlists(songs: List[Song]) -> List[Song]:
    """
    Creates a new playlist with 50 randomly chosen songs from our songs-database
    :return:
    """
    list_of_playlists = []  # Here we will add all the created playlist objects
    # Create a new playlist containing the list of 50 random songs from above
    for i in range(1, 101):
        # Create a  list of 50 songs randomly chosen from our list of all songs
        song_list = random.sample(songs, 50)
        new_playlist = Playlist(f"Playlist #{i}", song_list)
        # Add the new playlist to the list of all playlists
        list_of_playlists.append(new_playlist)
    # Return the list containing all playlists
    return list_of_playlists


# Function to create playlists categorized by a genre
def create_genre_playlists(songs: List[Song]) -> List[Playlist]:
    genre_playlists = {}
    output = []
    for song in songs:
        genre_playlists[song.genre] = genre_playlists.get(song.genre, []) + [song]
    for playlist in genre_playlists.keys():
        output.append(Playlist(playlist, genre_playlists[playlist]))
    return output


# Function to create playlists categorized by a genre
def create_cat_playlist(songs: List[Song]) -> List[Playlist]:
    cat_genre_playlists = {}
    output = []
    for song in songs:
        cat_genre_playlists[song.cat_genre] = cat_genre_playlists.get(song.cat_genre, []) + [song]
    for playlist in cat_genre_playlists.keys():
        output.append(Playlist(playlist, cat_genre_playlists[playlist]))
    return output


# Check the content of the playlists
def check_playlist(playlists):
    for playlist in playlists:
        print(playlist.listed_songs)



# Function to find the categories of a list of songs
def find_categories(songs: List[Song]) -> List[str]:
    list_of_categories = []
    for song in songs:
        if song.genre not in list_of_categories:
            list_of_categories.append(str(song.genre))
    return list_of_categories


# Function to categorize songs from a list of songs into one of three categories (rock, pop, techno)
def categorize_genre(songs: List[Song]) -> None:
    for song in songs:
        if song.genre in rock:
            song.set_rock()
        if song.genre in pop:
            song.set_pop()
        if song.genre in techno:
            song.set_techno()


# Takes the recommended songs to the listened_to attribute
# EXPLANATION: we assume that a user actually listens to a certain % of recommended songs,
# ...so those songs are added to the user.songs_listened list of song listened to
def took_recomendation(user_list: List[User], succes_rate: float) -> None:
    for user in user_list:
        user.listened_to_recommend(succes_rate)


#########################################################################################
# CREATING A HARD-CODED TEST USER

# This user gets a number of fixed songs from the all_songs list
# That way we can check whether our code is working (since the user's songs dont change)
##########################################################################################
def test_user(songs: List[Song], num_songs: int) -> User:
    user_A_songs = songs[0:num_songs]
    user_A = User(user_A_songs)
    return user_A



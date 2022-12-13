from typing import Dict, List
from classes import *

# **************************************************************************
# This file contains the code to create the recommendations for week 3
# **************************************************************************

def find_mood(user :User) -> tuple:
    mood = {"happy": 0, "party": 0, "calming": 0, "lounge": 0}
    for song in user.songs_listened:
        if song.energy > 50 and song.valence >50:
            mood['happy'] += 1
        if song.danceability > 70 and song.db > -5:
            mood['party'] += 1
        if song.energy < 50 and song.valence > 50:
            mood['calming'] += 1
        if song.energy < 70 and song.bpm < 100:
            mood['lounge'] += 1
    total = sum(mood.values())
    if mood['happy'] > 0:
        mood['happy'] = mood['happy'] / total * 100
    if mood['party'] > 0:
        mood['party'] = mood['party'] / total * 100
    if mood['calming'] > 0:
        mood['calming'] = mood['calming'] / total * 100
    if mood['lounge'] > 0:
        mood['lounge'] = mood['lounge'] / total * 100
    return (mood['happy'], mood['party'], mood['calming'], mood['lounge'])


# Function to create a custom playlist with recommended songs for week 3
def custom_playlist(play_list_name: str, playlist_max_song: int, songs: List[Song],
                    artist: str = "", genre: str = "", year: tuple = (0, 3000),
                    bpm: tuple = (0, 0), energy: tuple = (0, 0), danceability: tuple = (0, 0), db: tuple = (0, 0),
                    liveness: tuple = (0, 0), valence: tuple = (0, 0), length: tuple = (0, 0), accoustic: tuple = (0, 0),
                    speech: tuple = (0, 0)):

    min_song = Song("min_song", artist, genre, year[0], bpm[0], energy[0], danceability[0],
                    db[0], liveness[0], valence[0], length[0], accoustic[0], speech[0])

    max_song = Song("min_song", artist, genre, year[1], bpm[1], energy[1], danceability[1],
                    db[1], liveness[1], valence[1], length[1], accoustic[1], speech[1])

    output_list = []

    min_attr = min_song.list_attributes()
    max_attr = max_song.list_attributes()

    for song in songs:
        song_attr = song.list_attributes()
        shared_items = {shared: min_attr[shared] for shared in min_attr if shared in song_attr and min_attr[shared] == song_attr[shared]}
        print(shared_items)

    return Playlist(play_list_name, output_list)
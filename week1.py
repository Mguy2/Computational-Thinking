from typing import Dict, List
from classes import *

# **************************************************************************
# This file contains the code to create the recommendations for week 1
# **************************************************************************

def discover_week_1(user: User, playlists: List[Playlist], rec: int) -> List[Song]:
    listened_to = user.songs_listened
    for playlist in playlists:
        pos_counter = 0
        neg_counter = 0
        song_set = playlist.listed_songs
        for song in song_set:
            if song in listened_to:
                pos_counter += 1
            else:
                neg_counter += 1
            if pos_counter >= 3 and neg_counter >= 3:
                return random.sample(playlist.listed_songs, rec)


def give_recommendations_week_1(users :List[User], playlists :List[Playlist], rec :int) -> tuple:
    received_recommendation = list()
    no_recommendation = list()
    for user in users:
        rec_list = discover_week_1(user, playlists, rec)
        if rec_list != None:
            user.extend_recommendation(rec_list)
            received_recommendation.append(user)
        else:
            no_recommendation.append(user)
    return received_recommendation, no_recommendation


from typing import Dict, List
from classes import *

# **************************************************************************
# This file contains the code to create the recommendations for week 1
# **************************************************************************


def discover_week_1(user: User, playlists: List[Playlist], rec: int) -> List[Song]:
    """Generates a recommendation for User based on previously listened to songs.

    Args:
        user (User): User
        playlists (List[Playlist]): Pre-made playlists
        rec (int): How many recommendations

    Returns:
        List[Song]: List of recommendation
    """    
    listened_to = user.songs_listened
    for playlist in playlists:
        pos_counter = 0
        neg_counter = 0
        song_set = playlist.listed_songs
        for song in song_set:
            if song in listened_to: # if song is listened to, +1
                pos_counter += 1
            else:
                neg_counter += 1
            if pos_counter >= 3 and neg_counter >= 3:
                return random.sample(playlist.listed_songs, rec)


def give_recommendations_week_1(users :List[User], playlists :List[Playlist], rec :int) -> tuple:
    """Gives [rec] number of recommendations to all users in the list.

    Args:
        user (User): Users
        playlists (List[Playlist]): Pre-made playlists
        rec (int): How many recommendations

    Returns:
        tuple: [0]: users who received a rec, [1] users who received no rec.
    """    
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


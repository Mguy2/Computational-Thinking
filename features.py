from typing import Dict, List
from objects import *


# Week 1 Assignments
#=====================================================================#
#=====================================================================#
#=====================================================================#


def discover_week_1(user :User, playlists :List[Playlist], rec :int) -> List[Song]:
    listened_to = set(user.songs_listened)
    for playlist in playlists:
        pos_counter = 0
        neg_counter = 0
        song_set = set(playlist.listed_songs)
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
        user.extend_recommendation(rec_list)
        if rec_list != None:
            received_recommendation.append(user)
        else:
            no_recommendation.append(user)
    return received_recommendation, no_recommendation


# Week 2 Assignments
#=====================================================================#
#=====================================================================#
#=====================================================================#


def find_preferences(user :User) -> tuple:
    cat = {"pop": 0, "techno": 0, "rock": 0}
    for songs in user.songs_listened:
        genre = songs.genre
        if genre == 'pop':
           cat['pop'] += 1
        if genre == 'techno':
            cat['techno'] += 1
        if genre == 'rock':
            cat['rock'] += 1
    total = sum(cat.values())
    if cat['pop'] > 0:
        cat['pop'] = cat['pop'] / total * 100
    if cat['techno'] > 0:
        cat['techno'] = cat['techno'] / total * 100
    if cat['rock'] > 0:
        cat['rock'] = cat['rock'] / total * 100
    return (cat['pop'], cat['rock'], cat['techno'])


def users_find_preferences(users :User) -> None:
    for user in users:
        user.change_preferences(find_preferences(user))
 




#
# def give_recommendations_week_2(users :List[User], playlists :List[Playlist], rec :int):


# Week 3 Assignments
#=====================================================================#
#=====================================================================#
#=====================================================================#


# Extra Utils for testing
#=====================================================================#
#=====================================================================#
#=====================================================================#



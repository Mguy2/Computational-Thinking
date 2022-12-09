from typing import Dict, List
from objects import *


# Week 1 Assignments
#=====================================================================#
#=====================================================================#
#=====================================================================#


def discover_week_1(user :User, playlists :List[Playlist], rec :int) -> List[Song]:
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


# Week 2 Assignments
#=====================================================================#
#=====================================================================#
#=====================================================================#


def find_preferences(user :User) -> tuple:
    cat = {"pop": 0, "techno": 0, "rock": 0}
    for songs in user.songs_listened:
        genre = songs.cat_genre
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
 
 
def discover_week_2(user :User, playlists :List[Playlist], rec :int):
    nr_pop = user.pop /100 * rec
    nr_rock = user.rock /100 * rec
    nr_techno = user.techno / 100 * rec
    for playlist in playlists:
        if playlist.name == 'pop':
            pop_list = playlist.listed_songs
        if playlist.name == 'rock':
            rock_list = playlist.listed_songs
        if playlist.name == 'techno':
            techno_list = playlist.listed_songs
    if nr_pop > 0 or nr_rock > 0 or nr_techno > 0:
        rec_list = (random.sample(list(pop_list), int(nr_pop)) +
                    random.sample(rock_list, int(nr_rock)) +
                    random.sample(techno_list, int(nr_techno)))
        user.extend_recommendation(rec_list)
        return rec_list
    return -1


def give_recommendations_week_2(users :List[User], playlists :List[Playlist], rec :int):
    rec_given = []
    rec_not_given = []
    for user in users:
        rec_list = discover_week_2(user, playlists, rec)
        if rec_list == -1:
            rec_not_given.append(user)
        else:
            rec_given.append(user)
    return rec_given, rec_not_given
            

# Week 3 Assignments
#=====================================================================#
#=====================================================================#
#=====================================================================#


# Extra Utils for testing
#=====================================================================#
#=====================================================================#
#=====================================================================#



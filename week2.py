from typing import Dict, List
from classes import *

# **************************************************************************
# This file contains the code to create the recommendations for week 2
# **************************************************************************


def find_preferences(user: User) -> tuple:
    """Find preferences of User.

    Args:
        user (User): User whose preferences need be checked.

    Returns:
        tuple: User preferences
    """
    cat = {"pop": 0, "techno": 0, "rock": 0}
    for song in user.songs_listened:
        genre = song.cat_genre
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


def users_find_preferences(users: User) -> None:
    """Finds preferences for a list of users.

    Args:
        users (User): List of Users
    """
    for user in users:
        user.change_preferences(find_preferences(user))
 
 
def discover_week_2(user: User, playlists: List[Playlist], rec: int):
    """Gives recommendations based on apparant preference for a music-category.

    Args:
        user (User): User
        playlists (List[Playlist]): List of playlists
        rec (int): number of recommendations

    Returns:
        _type_: List of recommended songs.
    """    
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


def give_recommendations_week_2(users: List[User], playlists: List[Playlist], rec: int) -> tuple:
    """Gives recommendations to a list of users based on apparent music-category-
        preferences.

    Args:
        users (List[User]): List of Users
        playlists (List[Playlist]): List of playlists
        rec (int): Number of recommendations per user.

    Returns:
        Tuple: List of people who received a recommendation and a list of people who did not.
    """    
    rec_given = []
    rec_not_given = []
    for user in users:
        rec_list = discover_week_2(user, playlists, rec)
        if rec_list == -1:
            rec_not_given.append(user)
        else:
            rec_given.append(user)
    return rec_given, rec_not_given
            




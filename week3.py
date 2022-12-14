from typing import Dict, List
from classes import *
import math

# **************************************************************************
# This file contains the code to create the recommendations for week 3
# **************************************************************************

def find_mood(user: User) -> tuple:
    user_mood = {"happy": 0, "party": 0, "calming": 0, "lounge": 0}
    for song in user.songs_listened:
        if song.mood['happy'] == True:
            user_mood['happy'] += 1
        if song.mood['party'] == True:
            user_mood['party'] += 1
        if song.mood['calming'] == True:
            user_mood['calming'] += 1
        if song.mood['lounge'] == True:
            user_mood['lounge'] += 1
    # Get the total sum of all mood counts
    total = sum(user_mood.values())

    # Calculate the relative frequency of each mood for the user
    user_mood['happy'] = user_mood['happy'] / total
    user_mood['party'] = user_mood['party'] / total
    user_mood['calming'] = user_mood['calming'] / total
    user_mood['lounge'] = user_mood['lounge'] / total

    # Return a tuple with the relative frequency values of each mood
    return (user_mood['happy'], user_mood['party'], user_mood['calming'], user_mood['lounge'])

def users_find_mood(users: User) -> None:
    for user in users:
        user.update_mood(find_mood(user))


def discover_week_3(user: User, songs: List[Song], rec: int):
    happy_list = []
    party_list = []
    calming_list = []
    lounge_list = []
    num_rec_songs = {"happy": 0, "party": 0, "calming": 0, "lounge": 0}
    dominant_mood = max(user.mood)

    # Calculate for each mood the number of recommended songs
    # NOTE: we round down the number of songs to the nearest integer
    num_rec_songs["happy"] = math.trunc(user.mood['happy'] * rec)
    num_rec_songs["party"] = math.trunc(user.mood['party'] * rec)
    num_rec_songs["calming"] = math.trunc(user.mood['calming'] * rec)
    num_rec_songs["lounge"] = math.trunc(user.mood['lounge'] * rec)

    # If the number of recommended songs does not match the required number (i.e. rec), we add more songs
    # of the dominant mood
    while sum(num_rec_songs.values()) < rec:
        num_rec_songs[dominant_mood] += 1

    for song in songs:
        if song.mood['happy'] == True:
            happy_list.append(song)
        if song.mood['party'] == True:
            party_list.append(song)
        if song.mood['calming'] == True:
            calming_list.append(song)
        if song.mood['lounge'] == True:
            lounge_list.append(song)

    # Create a list of recommended songs based on the user's mood
    rec_list = []
    rec_list.append(random.sample(happy_list, num_rec_songs["happy"]))
    rec_list.append(random.sample(party_list, num_rec_songs["party"]))
    rec_list.append(random.sample(calming_list, num_rec_songs["calming"]))
    rec_list.append(random.sample(lounge_list, num_rec_songs["lounge"]))

    # Add the list of recommended songs to the user's songs_recommended list
    user.extend_recommendation(rec_list)

    return rec_list


def give_recommendations_week_3(users: List[User], songs: List[Song], rec: int):
    for user in users:
        discover_week_3(user, songs, rec)


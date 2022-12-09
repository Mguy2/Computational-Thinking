from typing import Dict, List
from objects import *
import csv
import random

# Takes the recommended songs to the listened_to attribute
def took_recomendation(user_list :List[User], succes_rate :float) -> None:
    for user in user_list:
        user.listened_to_recommend(succes_rate)
        

# Check the content of the playlists
def check_playlist(playlists):
    for playlist in playlists:
        print(playlist.listed_songs)
from typing import Dict, List
from categories import *
import csv
import random
import statistics as stat


# **************************************************************************
# This file contains the code to create the classes SONG, PLAYLIST and USER
# **************************************************************************

# The SONG class
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
        self.mood = {'happy': True, 'party': False, 'calming': False, 'lounge': False}

    def list_attributes(self) -> Dict[str, any]:
        return vars(self)

    def set_rock(self) -> None:
        self.cat_genre = "rock"
    
    def set_pop(self) -> None:
        self.cat_genre = "pop"
        
    def set_techno(self) -> None:
        self.cat_genre = "techno"

    def define_mood(self) -> None:
        energy = self.energy / 100  # Will give a value between 0 - 0.98
        danceability = self.danceability / 100  # Will give a value between 0 - 0.98
        valence = self.valence / 100  # Will give a value between 0 - 0.98
        bpm = self.bpm
        db = self.db

        # Set the 'party' mood (energy and danceability in dataset ranging from 0 - 98)
        party_factor = stat.mean([energy, danceability])
        if party_factor >= 0.5:
            self.mood['party'] = True
            if valence >= 0.5:
                self.mood['happy'] = True
            return  # We exit the method since a party song can never be a calming or lounge song

        # Set the 'lounge' mood
        if bpm <= 120:
            self.mood['lounge'] = True
            # Set the 'calming' mood
            if db <= -5:
                self.mood['calming'] = True
            if valence >= 0.5:
                self.mood['happy'] = True
            return  # We exit the method since we found at least one main mood (lounge)

        # Set the 'calming' mood
        if db <= -5:
            self.mood['calming'] = True
            if valence >= 0.5:
                self.mood['happy'] = True
            return  # We exit the method since we found a main mood (calming)

        # If none of the three moods 'party', 'lounge' or 'calming' apply, set the mood 'happy' to True
        self.mood['happy'] = True


    def __repr__(self):
        return f"TITLE: {self.title}"
    # Control what info is displayed when we execute "print(Song)"

    def __str__(self):
        return f"TITLE: {self.title}" #| ARTIST: {self.artist} | GENRE: {self.genre} | YEAR: {self.year}"


# The PLAYLIST class
class Playlist():
    def __init__(self, name: str, song_list: List[Song] = []):
        self.name = name
        self.listed_songs = song_list

    # Control what info is displayed when we execute "print(Playlist)"
    def __str__(self):
        return f"<{self.name.upper()}> contains {len(self.listed_songs)} songs."



# The USER class
class User():
    def __init__(self, songs_listened: List[Song] = []):
        self.id = id(self)
        self.songs_listened = songs_listened
        self.songs_recommended = []
        self.pop = 0
        self.rock = 0
        self.techno = 0
        self.mood = {'happy': 0, 'party': 0, 'calming': 0, 'lounge': 0}
        
    def extend_recommendation(self, rec_list: List[Song]):
        self.songs_recommended.extend(rec_list)
        
    def change_preferences(self, preferences: tuple):
        self.pop = preferences[0]
        self.rock = preferences[1]
        self.techno = preferences[2]

    def update_mood(self, mood_share: tuple):
        self.mood['happy'] = mood_share[0]
        self.mood['party'] = mood_share[1]
        self.mood['calming'] = mood_share[2]
        self.mood['lounge'] = mood_share[3]
        
    def attributes(self):
        return [self.id, self.pop, self.rock, self.techno] + self.songs_listened + self.songs_recommended
        
    def listened_to_recommend(self, success_rate: float) -> None:
        nr = int((len(self.songs_recommended) * 0.5))
        self.songs_listened.extend(random.sample(self.songs_recommended, nr))










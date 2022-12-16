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
    """Song Class generates a song object for a song with all attributes.
    """
    # NOTE: adjust the constructor method with the required song parameters
    def __init__(self, title, artist, genre, year, song_bpm,
                song_energy, song_d_ability, song_db, song_liveness,
                song_valence, song_length, song_accoustic, song_speech):
        """Constructor method of song class, initialises all properties.

        Args:
            title (_type_): Song Title
            artist (_type_): Song Artis
            genre (_type_): Song Genre
            year (_type_): Year of Song release
            song_bpm (_type_): song BPM
            song_energy (_type_): Song Energy
            song_d_ability (_type_): Song danceability
            song_db (_type_): Song Decibel
            song_liveness (_type_): Song Liveness
            song_valence (_type_): Song Valence
            song_length (_type_): Length of the Song
            song_accoustic (_type_): Song accousticness
            song_speech (_type_): Amount of speech.
        """        
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
        self.mood = song_moods

    def list_attributes(self) -> Dict[str, any]:
        """List all attributes of song object

        Returns:
            Dict[str, any]: name of attr. and corresponding value.
        """        
        return vars(self)

    def set_rock(self) -> None:
        """Set song genre cat to rock.
        """        
        self.cat_genre = "rock"
    
    def set_pop(self) -> None:
        """Set song genre cat to pop.
        """      
        self.cat_genre = "pop"
        
    def set_techno(self) -> None:
        """Set song genre cat to techno.
        """      
        self.cat_genre = "techno"

    def define_mood(self) -> None:
        """Defines the mood of the song.
        """        
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
    """Creates a Playlist object containing a list of song objects.
    """
    def __init__(self, name: str, song_list: List[Song] = []):
        self.name = name
        self.listed_songs = song_list

    # Control what info is displayed when we execute "print(Playlist)"
    def __str__(self):
        return f"<{self.name.upper()}> contains {len(self.listed_songs)} songs."



# The USER class
class User():
    """User Class creates object containing the datapoints of a single user.
    """    
    def __init__(self, songs_listened: List[Song] = []):
        self.id = id(self)
        self.name = "USERNAME = "+str(self.id)
        self.songs_listened = songs_listened
        self.songs_recommended = []
        self.pop = 0
        self.rock = 0
        self.techno = 0
        self.mood = {'happy': 0, 'party': 0, 'calming': 0, 'lounge': 0}
        self.age = str(random.sample(population_age_distribution, 1))
        self.location = str(random.sample(geographical_areas, 1))
        self.friend_list = []
        self.friend_count = 0
        
    def __str__(self) -> str:
        """Overrides standard printing behaviour when object print.

        Returns:
            str: Name of User.
        """    
        return f"{self.name}"
        
    def extend_recommendation(self, rec_list: List[Song]):
        """Add recommendation to user recommendation list.

        Args:
            rec_list (List[Song]): List of songs to be recommended.
        """    
        self.songs_recommended.extend(rec_list)
        
    def change_preferences(self, preferences: tuple):
        """Change the preferences of the user.

        Args:
            preferences (tuple): preferences found
        """        
        self.pop = preferences[0]
        self.rock = preferences[1]
        self.techno = preferences[2]

    def update_mood(self, mood_share: tuple):
        """Update the user's mood

        Args:
            mood_share (tuple): _description_
        """    
        self.mood['happy'] = mood_share[0]
        self.mood['party'] = mood_share[1]
        self.mood['calming'] = mood_share[2]
        self.mood['lounge'] = mood_share[3]
        
    def attributes(self):
        """Makes the simulator more use friendly - (Dir() replacement)

        Returns:
            _type_: Object properties
        """        
        return [self.id, self.age, self.location, self.friend_count,
                self.pop, self.rock, self.techno, self.mood] + self.songs_listened + self.songs_recommended
        
    def listened_to_recommend(self, success_rate: float) -> None:
        """Songs move from recommended to listened

        Args:
            success_rate (float): Percentage of songs to be added to listened
        """        
        nr = int((len(self.songs_recommended) * success_rate))
        self.songs_listened.extend(random.sample(self.songs_recommended, nr))
        
    def create_network(self, user_list :List[any]):
        """Add friends to friendlist

        Args:
            user_list (List[any]): List of Users to be added
        """    
        self.friend_list.extend(user_list)
        self.friend_count = len(self.friend_list)
        










from classes import *
from time import gmtime, strftime
from week1 import *
from week2 import *
from week3 import *
from utils import *
from save_state import *


# __  __        _             
#|  \/  | __ _ (_) _ _
#| |\/| |/ _` || || ' \       
#|_|  |_|\__/_||_||_||_|   
#=====================================================================#
#=====================================================================#
#=====================================================================#


def main():
        # Create environment
        #=========================================================#
        clock_time = str(strftime("%Y-%m-%d %H-%M-%S", gmtime()))
        songs = create_songs()
        all_categories = find_categories(songs)
        categorize_genre(songs)
        playlists = create_random_playlists(songs)
        cat_playlists = create_cat_playlist(songs)
        genre_playlists = create_genre_playlists(songs)
        # Create 100 users that listened to 10 songs
        user_list = create_users(songs, 100, 5) 
        test_subject = test_user(songs, 50)

        # Give recommendations
        # Week 1
        #=========================================================#
        week1 = give_recommendations_week_1(user_list, playlists, 5)
        # Output current state to CSV file (Week 1)
        save_state(user_list, 1, clock_time)

        # Week 2
        #=========================================================#
        # The previously recommended songs are now listened to:
        # Here the example succes rate is 50%
        took_recomendation(user_list, 0.5)
        # Find user preferences based on songs listened to
        users_find_preferences(user_list)
        # Give recommendations based on listening history
        # Returns tuple with users given recommendations[0] and not on [1]
        week2 = give_recommendations_week_2(user_list, cat_playlists, 5)
        # Output current state to CSV file (Week 2)
        save_state(user_list, 2, clock_time)
        
        # Week 3
        #=========================================================#
        # The previously recommended songs are now listened to:
        # Here the example success rate is 50%
        took_recomendation(user_list, 0.5)
        # Find user preferences based on songs listened to
        users_find_preferences(user_list)
        # Find user moods based on songs listened to
        users_find_mood(user_list)
        # Give recommendations based on listening history
        # Returns tuple with users given recommendations[0] and not on [1]
        week3 = give_recommendations_week_3(user_list, songs, 5)
        # Output current state to CSV file (Week 3)
        save_state(user_list, 3, clock_time)
        
        # Week 4
        #=========================================================#
        # The previously recommended songs are now listened to:
        # Here the example success rate is 50%
        took_recomendation(user_list, 0.5)  
        # Find user preferences based on songs listened to
        users_find_preferences(user_list)
        # Find user moods based on songs listened to
        users_find_mood(user_list)
        # Output current state to CSV file (Week 4)
        save_state(user_list, 4, clock_time)
        

if __name__ == "__main__":
    main()
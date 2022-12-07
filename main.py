from objects import *
from features import *
from utils import *


def main():
        # Create environment
        songs = create_songs()
        all_categories = find_categories(songs)
        playlists = create_playlists(songs)
        # Create 100 users that listened to 10 songs
        user_list = create_users(songs, 100, 10) 
        test_subject = test_user(songs, 50)

        # Give recommendations
        # Week 1
        week1 = give_recommendations_week_1(user_list, playlists, 5)

        # Week 2
        # The previously recommended songs are now listened to:
        for users in user_list:
            print(users.songs_recommended)

        # Find all user's preferences and add them to the class
        users_find_preferences(user_list)
        
        # Week 3




        

if __name__ == "__main__":
    main()
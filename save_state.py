from classes import *
import csv
import os


# ___                 
#/ __| __ _ __ __ ___ 
#\__ \/ _` |\ V // -_)
#|___/\__/_| \_/ \___|
#=====================================================================#
#=====================================================================#
#=====================================================================#


def save_state(users :List[User], step :any, clock_time :str) -> None:
    """Saves current user properties to a CSV file.

    Args:
        users (List[User]): List of Users
        step (any): Message
        clock_time (str): Clock Time
    """    
    headers = ['USER ID', 'AGE', 'LOCATION', 'FRIEND_COUNT', 'POP_RATE', 'ROCK_RATE', 'TECHNO_RATE', 'USER MOOD', 'SONGS_LISTENED', 'SONGS_RECOMMENDED']
    directory = os.path.join("Simulations", "Out "+str(clock_time))
    if not os.path.exists(directory):
        os.makedirs(directory)   
    path = os.path.join(directory, "saved_state_"+str(clock_time)+"Step "+str(step)+".csv")
    with open(path, "w", encoding='UTF8', newline='') as location:
        write_to_file = csv.writer(location)    
        write_to_file.writerow(headers)
        for user in users:
            write_to_file.writerow(user.attributes())
    print("Saved Step:", step, "to: ", directory)
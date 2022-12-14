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


def save_state(users :List[User], step :int, clock_time :str) -> None:
    headers = ['USER ID', 'POP_rate', 'ROCK_rate', 'TECHNO_rate', 'USER MOOD', 'SONGS_LISTENED', 'SONGS_RECOMMENDED']
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
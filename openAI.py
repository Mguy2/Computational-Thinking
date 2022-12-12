import os
import openai
import csv
import os
import time


def openAI_generate_user():
  openai.api_key = "[Deleted API KEY]"

  response = openai.Completion.create(
    model="text-davinci-003",
    prompt="generate a random Spotify user profile with the following attributes: Username, Age, Location, music preference by genre, favourite music genre and 15 favourite songs with artist separated. Only popular music\n\nUsername:\nAge:\nLocation:\nMusic Preference by Genre:\nFavourite Music Genre:\n\nFavourite Songs: \n1.\n2.\n3.\n4.\n5.\n6.\n7.\n8.\n9.\n10.\n11.\n12.\n13.\n14.\n15. ",
    temperature=0.7,
    max_tokens=256,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
  )
  return response


def save_user(response, clock_time :str) -> None:
    directory = os.path.join("User Profiles")
    if not os.path.exists(directory):
        os.makedirs(directory)   
    path = os.path.join(directory,"User_Profiles.csv")
    with open(path, "a", encoding='UTF8', newline='') as location:
        write_to_file = csv.writer(location)   
        write_to_file.writerow(response.split('\n'))
    print("Saved User Information to: ", directory)
    

def create_users(x :int):
  while x > 0:
    response = openAI_generate_user()
    save_user(str(response["choices"][0]["text"]), "None")
    x -= 1
  print("OpenAI User Generation Complete")
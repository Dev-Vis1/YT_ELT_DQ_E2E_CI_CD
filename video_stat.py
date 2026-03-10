import requests
import json 
import os
from dotenv import load_dotenv

load_dotenv(dotenv_path="./.env")

API_KEY = os.getenv("API_KEY")
channel_id = "MrBeast"

def get_playlist_id():

    try:
        
        url = f"https://youtube.googleapis.com/youtube/v3/channels?part=contentDetails&forHandle={channel_id}&key={API_KEY}"
        response = requests.get(url)
        response.raise_for_status()  # Check if the request was successful

        data = response.json()
        #print(json.dumps(data, indent=4))

        channel_playlistID = data["items"][0]["contentDetails"]["relatedPlaylists"]["uploads"]

        print(channel_playlistID)
        return channel_playlistID

    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None
    
if __name__ == "__main__":
    print("The function get_playlist_id is executed")
    get_playlist_id()

else:
    print("The function get_playlist_id is imported and not executed")
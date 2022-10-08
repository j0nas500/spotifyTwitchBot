from pprint import pprint
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import env

scope = ["user-modify-playback-state", "user-read-playback-state"]
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))

res = sp.devices()
devices = res['devices']

# In order for Spotify to output your device ID, 
# you have to play something on Spotify before and 
# during the execution of this file. 
# Copy the correct ID from the output and 
# put it into bot.py / botExample.py in line 11. 
pprint(devices)

# Creates bot2.py File
import os
from pprint import pprint
from string import Template

import spotipy
from spotipy import SpotifyOAuth

print("You need a Spotify Developer App. You can create the app here: https://developer.spotify.com/dashboard/")
print("In \"edit Setting\" add the redirect URI \"http://localhost:8090\" and click on save")
input("Press Enter to continue...")

print("Now add the Client ID and Client Secret here:")
client_id = input("CLIENT ID: ")
client_secret = input("CLIENT SECRET: ")

print()
print("Now start Spotify and play music. Wait a few seconds")
print("If you press enter now your browser will open")
print("and you will need to log in with your Spotify account.")
print("After that your device id will appear in the console")
input("Press Enter to continue...")

os.environ["SPOTIPY_CLIENT_ID"] = client_id
os.environ["SPOTIPY_CLIENT_SECRET"] = client_secret
os.environ["SPOTIPY_REDIRECT_URI"] = "http://localhost:8090"

scope = ["user-modify-playback-state", "user-read-playback-state"]
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))

res = sp.devices()
devices = res['devices']
pprint(devices)

device_id = input("Now enter your device id (id) here: ")

file_data = Template('''\
import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth

scope = ["user-modify-playback-state", "user-read-playback-state"]
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))

# CHANGE THIS TO REAL VALUES
os.environ["SPOTIPY_CLIENT_ID"] = "$client_id"
os.environ["SPOTIPY_CLIENT_SECRET"] = "$client_secret"
os.environ["SPOTIPY_REDIRECT_URI"] = "http://localhost:8090"
device_id = "$device_id"

with open('input.txt') as f:
    response = f.readlines()
print(response)
if response[0].startswith('https://open.spotify.com/track/'):
    try:
        sp.add_to_queue(response[0], device_id)
        res = sp.track(response[0])
        song = res['artists']
        artist = song[0]['name']
        track = res['name']
        with open('output.txt', 'w', encoding='utf-8') as f:
            f.write(f'You have requested the song {track} by {artist}.')
        print(f'You have requested the song {track} by {artist}')
    except Exception:
        print("Error")
        with open('output.txt', 'w', encoding='utf-8') as f:
            f.write(f'ERROR')
else:
    try:
        res = sp.search(q='track' + response[0], type='track', limit=1)
        url = res['tracks']['items'][0]['external_urls']['spotify']
        artist = res['tracks']['items'][0]['artists'][0]['name']
        track = res['tracks']['items'][0]['name']
        sp.add_to_queue(url, device_id)
        with open('output.txt', 'w', encoding='utf-8') as f:
            f.write(f'You have requested the song {track} by {artist}.')
        print(f'You have requested the song {track} by {artist}')
    except Exception:
        print("Error")
        with open('output.txt', 'w', encoding='utf-8') as f:
            f.write(f'ERROR')
''')
file_data = file_data.substitute({ 'client_id': client_id, 'client_secret': client_secret, 'device_id': device_id })

with open("testExample.py", 'w') as f:
    f.write(file_data)

print("File bot2.py succesfully created")
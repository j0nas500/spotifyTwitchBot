import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth

scope = ["user-modify-playback-state", "user-read-playback-state"]
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))

# CHANGE THIS TO REAL VALUES
os.environ["SPOTIPY_CLIENT_ID"] = "GET IT HERE: https://developer.spotify.com/dashboard/applications"
os.environ["SPOTIPY_CLIENT_SECRET"] = "GET IT HERE: https://developer.spotify.com/dashboard/applications"
os.environ["SPOTIPY_REDIRECT_URI"] = "http://localhost:8090"
device_id = "GET IT HERE: getDevice.py"

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

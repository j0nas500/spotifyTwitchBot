import os
import time

import spotipy
from spotipy import SpotifyException
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv
from urllib.error import HTTPError

load_dotenv()
client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")
redirect_uri = os.getenv("REDIRECT_URI")

if client_id is None or client_secret is None or redirect_uri is None:
    with open('../output.txt', 'w', encoding='utf-8') as f:
        f.write(f'.env File is not set correctly')
    print(f'.env File is not set correctly')
    exit(0)

scope = ["user-modify-playback-state", "user-read-playback-state"]
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(client_id=client_id, client_secret=client_secret, redirect_uri=redirect_uri, scope=scope))


try:
    sp.next_track()
    time.sleep(1)
    res_next = sp.currently_playing()
    track = res_next['item']['name']
    artist = res_next['item']['artists'][0]['name']
    with open('../output.txt', 'w', encoding='utf-8') as f:
        f.write(f'🔊 {track} by {artist}')
    print(f'🔊 {track} by {artist}')
except SpotifyException as err:
    print(err)
    with open('../output.txt', 'w', encoding='utf-8') as f:
        f.write(f'ERROR: {err.msg}')

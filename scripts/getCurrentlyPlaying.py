import os

import spotipy
from spotipy import SpotifyException
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv

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
    res_next = sp.currently_playing()
    if res_next is None:
        exit(0)
    track = res_next['item']['name']
    artist = res_next['item']['artists'][0]['name']
    url = res_next['item']['external_urls']['spotify']
    with open('../output.txt', 'w', encoding='utf-8') as f:
        f.write(f'{track} by {artist} | {url}')
    print(f'🔊 {track} by {artist} | {url}')
except SpotifyException as err:
    print(err)
    with open('../output.txt', 'w', encoding='utf-8') as f:
        f.write(f'ERROR: {err.msg}')

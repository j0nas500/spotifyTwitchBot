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

with open('../input.txt') as f:
    response = f.readlines()

try:
    response = int(response[0])
    if response < 0 or response > 100:
        raise ValueError("Volume must be between 0 and 100, inclusive")
    sp.volume(response)
    with open('../output.txt', 'w', encoding='utf-8') as f:
        f.write(f'{response}')
    print(f'🔊 {response}%')
except SpotifyException as err:
    print(err)
    with open('../output.txt', 'w', encoding='utf-8') as f:
        f.write(f'ERROR: {err.msg}')
except (TypeError, ValueError):
    print("Volume must be an integer between 0 and 100")
    with open('../output.txt', 'w', encoding='utf-8') as f:
        f.write(f'ERROR: Volume must be an integer')


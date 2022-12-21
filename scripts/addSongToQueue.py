import os
import string

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
print(response)

if response[0].startswith('https://open.spotify.com/track/'):
    try:
        sp.add_to_queue(response[0], None)
        res = sp.track(response[0])
        song = res['artists']
        artist = song[0]['name']
        track = res['name']
        with open('../output.txt', 'w', encoding='utf-8') as f:
            f.write(f'{track} by {artist}')
        print(f'➕ {track} by {artist}')

    except SpotifyException as err:
        print(err)
        with open('../output.txt', 'w', encoding='utf-8') as f:
            f.write(f'ERROR: {err.msg}')
else:
    try:
        if not response[0].__contains__('-'):
            raise ValueError

        split: string = response[0].split('-')
        track: string = split[0].strip()
        artist: string = split[1].strip()
        res = sp.search(q=f'track:{track} artist:{artist}', type='track', limit=1)

        if len(res['tracks']['items']) == 0:
            track = split[1].strip()
            artist = split[0].strip()
            res = sp.search(q=f'track:{track} artist:{artist}', type='track', limit=1)

        url = res['tracks']['items'][0]['external_urls']['spotify']
        artist = res['tracks']['items'][0]['artists'][0]['name']
        track = res['tracks']['items'][0]['name']

        sp.add_to_queue(url, None)
        with open('../output.txt', 'w', encoding='utf-8') as f:
            f.write(f'{track} by {artist}')
        print(f'➕ {track} by {artist}')

    except ValueError:
        print('Wrong Format')
        with open('../output.txt', 'w', encoding='utf-8') as f:
            f.write(f'ERROR: Please write your song in the following format: artist - song. Your points have been refunded.')

    except SpotifyException as err:
        print(err)
        with open('../output.txt', 'w', encoding='utf-8') as f:
            f.write(f'ERROR: {err.msg}')

    except IndexError:
        print("Song not found")
        with open('../output.txt', 'w', encoding='utf-8') as f:
            f.write(f'ERROR: Song was not found. Your points have been refunded!')

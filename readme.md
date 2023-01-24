# Spotify Twitch Bot Integration
Python Script using the Package [spotipy](https://github.com/plamere/spotipy) to add songs requested by Twitch viewers to the queue. This is possible by using  [Streamer.Bot](https://streamer.bot/)

## Requirements
- Have [Streamer.Bot](https://streamer.bot/) set up
- [Python](https://www.python.org/)
- [Spotify Account](https://www.spotify.com/) (Premium if you want use the Songrequest Feature)

## Features
- Spotify Songrequests [with Spotify Premium only]
- current Spotify Song
- skip Spotify Song
- previous Spotify Song
- change Volume of Spotify


## How to install
Clone the repository or [download the ZIP](https://github.com/j0nas500/spotifyTwitchBot/archive/refs/heads/master.zip) and unzip it

### Spotify Developer Application
1. Create an App at the [Spotify Developer Application](https://developer.spotify.com/dashboard/login)
2. Copy the client ID and the client secret from the application.
3. In "edit Setting" add the redirect URI "http://localhost:8090" and click on save
4. Duplicate the `.env.example` and name it `.env`
5. Set in the `.env` file your client id and client secret of your Spotify application

### Set up Python
1. Install spotipy with pip: `pip install spotipy`
2. Install dotenv with pip: `pip install python-dotenv`

### Set up Streamer.Bot
1. Copy the string of the [streamerbotImportString](https://raw.githubusercontent.com/j0nas500/spotifyTwitchBot/master/streamerbotImportString) File and import it into Streamer.Bot
2. In the "Setup" Action you must set the path of the `scripts` folder of this repository
3. In the "Input" Action you must set the path of the `input.txt` of this repository
4. In the "Output" Action you must set the path of the `output.txt` of this repository
5. Use the commands or create a custom reward

Now as soon as who use your command or redeems the reward and sends in a song name or Spotify link, this song should have been added to your queue. 


## Disclaimer
I want to make this extremely clear, it is down to yourself to seek permission with the relevant providers (Spotify and Twitch) for more information and to determine whether you have the relevant licenses and/or permissions to play Spotify music on your stream. I accept no reliability or responsibility for any action either vendor may take,  you do so at your own risk.
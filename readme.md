# Spotify Twitch Bot Integration
Python Script using the Package [spotipy](https://github.com/plamere/spotipy) to add songs requested by Twitch viewers to the queue. This is possible by using  [Streamer.Bot](https://streamer.bot/)

## Requirements
- Have Streamer.Bot set up
- [Python](https://www.python.org/)
- Spotify Account

## How to install
Clone the repository or [download the ZIP](https://github.com/j0nas500/spotifyTwitchBot/archive/refs/heads/master.zip) and unzip it

### Spotify Developer Application
1. Create an App at the [Spotify Developer Application](https://developer.spotify.com/dashboard/login)
2. Copy the client ID and the client secret from the application.
3. In "edit Setting" add the redirect URI "http://localhost:8090" and click on save

### Set up Python
1. Install spotipy with Pip: `pip install spotipy`
2. Start the music on Spotify on your computer to get the device ID
3. Run `setup.py` (`python setup.py`) to set everything up
4. If everything worked, you get the following output: "File bot.py succesfully created"

### Set up Streamer.Bot
In the actions folder, there are several actions for Streamer.Bot. The only necessary action is `addSongToQueue`. All others are optional.

1. Copy the string of the [addSongToQueue](https://raw.githubusercontent.com/j0nas500/spotifyTwitchBot/master/actions/addSongToQueue/addSongToQueue?token=GHSAT0AAAAAABYHXQWEO3R726TZE6DTF4OYY2BRARQ) File and import it into Streamer.Bot
2. In the action "CP: Add Song to Queue" change the paths from the sub-actions "Write to File" and "Read Lines" to the files input.txt and output.txt, which are contained here
3. Create a Channel Point reward in Streamer Bot with "User Input Required" and set the action "CP: Add Song to Queue" there.

Now as soon as who redeems the reward and sends in a song name or Spotify link, this song should have been added to your queue. 


## Disclaimer
I want to make this extremely clear, it is down to yourself to seek permission with the relevant providers (Spotify and Twitch) for more information and to determine whether you have the relevant licenses and/or permissions to play Spotify music on your stream. I accept no reliability or responsibility for any action either vendor may take,  you do so at your own risk.
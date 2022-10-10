# Add Spotify Song to Queue
When a Channel Point reward is redeemed and either a Spotify link or the song name with artist is provided, it is added to the Spotify queue and automatically marked as completed.
If the song was not found, the reward will be rejected.

## How to install
### Spotify Developer Application
1. Create an App at the [Spotify Developer Application](https://developer.spotify.com/dashboard/login)
2. Copy the client ID and the client secret from the application.
3. In "edit Setting" add the redirect URI "http://localhost:8090" and click on save

### Set up Python
1. Install spotipy with Pip: `pip install spotipy`
2. Start the music on Spotify on your computer to get the device ID
3. Run `setup.py` (`python setup.py`) to set everything up
4. If everything worked, a new file `bot.py` should now exist and you get the following output: "File bot.py succesfully created"

### Set up Streamer.Bot
1. Copy the string of the [addSongToQueue](https://raw.githubusercontent.com/j0nas500/spotifyTwitchBot/master/actions/addSongToQueue/addSongToQueue?token=GHSAT0AAAAAABYHXQWEO3R726TZE6DTF4OYY2BRARQ) File and import it into Streamer.Bot
2. In the action "CP: Add Song to Queue" change the paths from the sub-actions "Write to File" and "Read Lines" to the files input.txt and output.txt, which are contained here
3. Also change in the action the source code from the exeuction code the following line:
`startInfo.Arguments = @"/c cd /d D:\nextcloud\coding\python\spotifyTwitchBot && python bot.py";`
4. Change there the path `D:\nextcloud\coding\python\spotifyTwitchBot` to the path where the `setup.py` and the `bot.py` file is located
5. click on "Find Refs" and "Compile". If the output is the following, everything should be correct. You can click on "Ok
```
Building out needed information...
Compiled successfully!
```
6. Create a Channel Point reward in Streamer Bot with "User Input Required" and set the action "CP: Add Song to Queue" there.
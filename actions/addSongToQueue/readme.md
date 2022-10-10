# Add Spotify Song to Queue
When a Channel Point reward is redeemed and either a Spotify link or the song name with artist is provided, it is added to the Spotify queue and automatically marked as completed.
If the song was not found, the reward will be rejected.

## How to install
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
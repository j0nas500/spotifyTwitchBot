using System;
using System.Runtime.InteropServices;
using System.Windows.Forms;
using System.Diagnostics;
using System.Management;
using System.Linq;

public class CPHInline
{
	public string GetSpotifyTrackInfo()
    {
        var proc = Process.GetProcessesByName("Spotify").FirstOrDefault(p =>!string.IsNullOrWhiteSpace(p.MainWindowTitle));

        if (proc == null)
        {
            return "Spotify is not running!";
        }

        if (string.Equals(proc.MainWindowTitle, "Spotify Premium", StringComparison.InvariantCultureIgnoreCase) || string.Equals(proc.MainWindowTitle, "Spotify Free", StringComparison.InvariantCultureIgnoreCase))
        {
            return "Paused";
        }
        return proc.MainWindowTitle;
    }
	
	public bool Execute()
	{
		//string song = GetSpotifyTrackInfo();
		CPH.SetArgument("spotifySong", GetSpotifyTrackInfo());
		return true;
	}
}

using System;
using System.Runtime.InteropServices;
using System.Windows.Forms;
using System.Diagnostics;
using System.Management;
using System.IO;

public class CPHInline
{
	public bool Execute()
	{
		Process p = new Process();
		ProcessStartInfo startInfo = new ProcessStartInfo();
		startInfo.UseShellExecute = false;
		startInfo.CreateNoWindow = true;
		startInfo.FileName = "cmd.exe";
		startInfo.Arguments = @"/c cd /d D:\nextcloud\coding\python\spotifyTwitchBot && python bot.py"; // CHANGE IT
		p.StartInfo = startInfo;
		p.Start();
		p.WaitForExit();
		return true;
	}
}

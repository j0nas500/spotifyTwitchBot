using System;
using System.Diagnostics;

public class CPHInline
{


	public bool AddSongToQueue()
	{
		Process p = new Process();
		ProcessStartInfo startInfo = new ProcessStartInfo();
		startInfo.UseShellExecute = false;
		startInfo.CreateNoWindow = true;
		startInfo.FileName = "cmd.exe";
		string scriptPath = args["spotifyScriptPath"].ToString();
		startInfo.Arguments = @"/c cd /d " + scriptPath + " && python addSongToQueue.py";
		p.StartInfo = startInfo;
		p.Start();
		p.WaitForExit();
		return true;
	}

	public bool GetCurrentlyPlaying()
	{
		Process p = new Process();
		ProcessStartInfo startInfo = new ProcessStartInfo();
		startInfo.UseShellExecute = false;
		startInfo.CreateNoWindow = true;
		startInfo.FileName = "cmd.exe";
		string scriptPath = args["spotifyScriptPath"].ToString();
		startInfo.Arguments = @"/c cd /d " + scriptPath + " && python getCurrentlyPlaying.py";
		p.StartInfo = startInfo;
		p.Start();
		p.WaitForExit();
		return true;
	}

	public bool SetPlaybackVolume()
	{
		Process p = new Process();
		ProcessStartInfo startInfo = new ProcessStartInfo();
		startInfo.UseShellExecute = false;
		startInfo.CreateNoWindow = true;
		startInfo.FileName = "cmd.exe";
		string scriptPath = args["spotifyScriptPath"].ToString();
		startInfo.Arguments = @"/c cd /d " + scriptPath + " && python setPlaybackVolume.py";
		p.StartInfo = startInfo;
		p.Start();
		p.WaitForExit();
		return true;
	}

	public bool SkipToNext()
	{
		Process p = new Process();
		ProcessStartInfo startInfo = new ProcessStartInfo();
		startInfo.UseShellExecute = false;
		startInfo.CreateNoWindow = true;
		startInfo.FileName = "cmd.exe";
		string scriptPath = args["spotifyScriptPath"].ToString();
		startInfo.Arguments = @"/c cd /d " + scriptPath + " && python skipToNext.py";
		p.StartInfo = startInfo;
		p.Start();
		p.WaitForExit();
		return true;
	}

	public bool SkipToPrevious()
	{
		Process p = new Process();
		ProcessStartInfo startInfo = new ProcessStartInfo();
		startInfo.UseShellExecute = false;
		startInfo.CreateNoWindow = true;
		startInfo.FileName = "cmd.exe";
		string scriptPath = args["spotifyScriptPath"].ToString();
		startInfo.Arguments = @"/c cd /d " + scriptPath + " && python skipToPrevious.py";
		p.StartInfo = startInfo;
		p.Start();
		p.WaitForExit();
		return true;
	}

}

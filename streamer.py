import subprocess

PLAYERS = ["mpv", "vlc", "airplay", "chromecast", "dlna", "mplayer", "omx", "iina", "smplayer",
    "xmbc", "stdout"]

def stream_me_matey(magnet: str) -> None:
    
    #TODO Add player selection
    player = "mpv"
    # launches the webtorrent-cli to play the torrent
    subprocess.run(["webtorrent", magnet, f"--{player}"])
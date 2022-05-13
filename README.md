<h2 align='center'>Basedflix</h2>
<p align='center'><i>"Netflix for the based"</i></p>

<div align='center'>

![2 million bobs](.github/big-bob.jpg)
</div>

## Contributors

<div align='center'>
<a href="https://github.com/northoc/cliflix/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=northoc/cliflix" />
</a>
</div>

## Description

Select from the current top 100 movies HD section from The Pirate Bay in your Command Line Interface (Terminal) and stream it in seconds using a supported media player. If there are no subtitles, you can find some on the web and upload the .srt file to the media player.

## Dependencies:

1. Python3 & pip (also Python3.10-dev)

2. npm and nodejs using the apt package manager:
```bash
sudo apt-get install npm #installs both npm and nodejs
```

3. webtorrent-cli:
```bash
sudo npm install webtorrent-cli -g
```

## Supported Video players

| Player (CLI command) | Player name | Install via apt package manager |
|----------------------|-------------|---------------------------------|
| airplay              | Apple TV    |                                 |
| chromecast           | Chromecast  |                                 |
| dlna                 | DLNA        |                                 |
| mplayer              | mplayer     | `sudo apt install mplayer`      |
| mpv                  | MPV         | `sudo apt install mpv`          |
| omx                  | OMX         |                                 |
| vlc                  | VLC         | `sudo apt install vlc`          |
| iina                 | IINA        |                                 |
| smplayer             | SMPlayer    | `sudo apt install smplayer`     |
| xbmc                 | XBMC        |                                 |

## Quick install

```bash
git clone https://github.com/NorthOC/basedflix
cd basedflix
./install.sh
```
What this will do is simple:
1. Create a virtual Python environment `venv`
2. Install pip modules form `requirements.txt` to the virtual environment
3. Find the location of the `main.py` file on your computer
4. Add that location to `basedflix.sh`
5. Check and create (if not found) `~/.local/bin` directory
6. Add a PATH variable (for `~/.local/bin`) to ~/.bashrc
7. Copy the file `basedflix.sh` to `~/.local/bin` as `basedflix`

That is it! You can launch the program now by typing `basedflix` in your terminal.

![pirate pepe](.github/pepe-pirate.png)

## Manual installation

You can modify `install.sh` to not include the PATH addition to `.bashrc` and change the directory to where `basedflix` should be copied (I left some helpful comments ^_^ )

The instructions for manual installation (if you choose not to install via `install.sh`) can be found inside the file `basedflix.sh` 

## Important Note

*Use a vpn if your country has very strict laws on torrenting!*

## How it works

The JSON data is received from thepiratebay API. It is then parsed into an easily manageable array. Then the movies are displayed to the console. After that you select the movie and a supported media player. The webtorrent-cli then receives a info hash (imagine it as a shorter magnet link) and streams the torrent, on a chosen video player.

## Roadmap

- Create JSON parser (done)
- Create Streamer (done)
- Watch top 100 movies (done)
- Install script (done)
- Minimum viable product (done)
- Video demo
- Uninstall script
- Install script options
- Watch any movie
- Rewrite in C/C++ to loose dependecies
- UI
- Search by category
- Cross-platform

import subprocess
import urllib.parse as urlparse

def select_movie(movie_array):
    picked_movie = -1
    
    while picked_movie < 0 or picked_movie > 100:
        picked_movie = int(input("Select a movie(from 1 to 100. type 0 to exit): "))
    
    if picked_movie == 0:
            print("Have a nice day, matey!")
            exit()

    movie_details = movie_array[picked_movie - 1].split(", ")
    movie_name = movie_details[2]
    movie_name_encoded = urlparse.quote(movie_name)
    info_hash = movie_details[1]

    # template for tpb magnet links
    magnet_link = f"magnet:?xt=urn:btih:{info_hash}&dn={movie_name_encoded}&"\
        f"tr=udp%3A%2F%2Ftracker.coppersurfer.tk%3A6969%2Fannounce&tr=udp%3A%2F%2F"\
        f"tracker.openbittorrent.com%3A6969%2Fannounce&tr=udp%3A%2F%2F9.rarbg.to%3A2710%2F"\
        f"announce&tr=udp%3A%2F%2F9.rarbg.me%3A2780%2Fannounce&tr=udp%3A%2F%2F9.rarbg.to%3A2730%2F"\
        f"announce&tr=udp%3A%2F%2Ftracker.opentrackr.org%3A1337&tr=http%3A%2F%2Fp4p.arenabg.com%3A1337%2F"\
        f"announce&tr=udp%3A%2F%2Ftracker.torrent.eu.org%3A451%2Fannounce&tr=udp%3A%2F%2F"\
        f"tracker.tiny-vps.com%3A6969%2Fannounce&tr=udp%3A%2F%2Fopen.stealth.si%3A80%2Fannounce"
    print("\nSelected movie:",f"{movie_name}")
    return magnet_link


# select media player from supported ones
def select_player():
    PLAYERS = ["mpv", "vlc", "airplay", "chromecast", "dlna", "mplayer", "omx", "iina", "smplayer",
    "xmbc", "stdout"]
    selected_player = None

    print("\nSupported media players:")
    print(*PLAYERS, sep=", ")
    print()
        
    while (selected_player not in PLAYERS):
        selected_player = input("Select a player (mpv, vlc, etc.): ")
    
    return selected_player


# stream the video matey
def stream_me_matey(magnet, player) -> None:

    # checks if you have the player
    try:
        subprocess.run([f"{player}", "--version"],check=True)
    except FileNotFoundError:
        print("\nThe player {} was not found on your system.".format(player))
        print("You could try installing it with: sudo apt install {}".format(player))
        return

    subprocess.run(["webtorrent", f"{magnet}", f"--{player}"] )
import subprocess

def select_movie(movie_array):
    picked_movie = -1
    
    while picked_movie < 0 or picked_movie > 100:
        picked_movie = int(input("Select a movie(from 1 to 100. type 0 to exit):"))
    
    if picked_movie == 0:
            print("Have a nice day, matey!")
            exit()

    movie_details = movie_array[picked_movie - 1].split(", ")
    movie_name = movie_details[2]
    info_hash = movie_details[1]

    print("\nSelected movie:",f"{movie_name}")

    return info_hash



# select media player from supported ones
def select_player():
    PLAYERS = ["mpv", "vlc", "airplay", "chromecast", "dlna", "mplayer", "omx", "iina", "smplayer",
    "xmbc", "stdout"]
    selected_player = None

    print("\nSupported media players:")
    print(*PLAYERS, "\n")
        
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
    
    subprocess.run(["webtorrent", magnet, f"--{player}"] )
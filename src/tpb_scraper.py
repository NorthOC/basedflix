import requests
import json

# scrape json api 
def parse_me_matey(query):
    while True:
        if not query:
            r = requests.get('https://apibay.org/precompiled/data_top100_207.json')
        else:
            r = requests.get(f"https://apibay.org/q.php?q={query}&cat=200")

        content = r.content
        parsed = json.loads(content)

        if parsed[0]["id"] == "0":
            print("No movie was found. Maybe there was a typo?")
            query = input("Enter the movie title: ")
        else:
            return parsed


# output easily manageable array
def info_to_arr(parsed):
    movies = []

    for torrent in parsed:
        torrent_id = torrent["id"]
        magnet = torrent["info_hash"]
        name = torrent["name"]
        size_bytes = torrent["size"]
        seeders = torrent["seeders"]
        leechers = torrent["leechers"]

        # format size of movie
        if int(size_bytes) > 1000000000:
            prefixer = "GiB" 
            size_xib = int(size_bytes) / 1024 / 1024 / 1024
        else:
            prefixer = "MiB"
            size_xib = int(size_bytes) / 1024 / 1024

        # movie is stored to array as id | magnet hash | name | size | seeders | leechers
        item = str(torrent_id) + ", " + magnet + ", " + name + ", "\
             + str("%.2f" % size_xib) + f" {prefixer}" + ", " + "Seeders: " + str(seeders) + ", " + "Leechers: " + str(leechers)

        movies.append(item)
    
    # print out movies
    counter = len(movies)
    movies.reverse()
    for item in movies:
        item = item.split(", ")
        print((str(counter) + ".").ljust(4), item[2], item[3], item[4], item[5])
        counter -= 1

    print()
    movies.reverse()
    return movies

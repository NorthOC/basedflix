import requests
import json

# scrape json api

def parse_me_matey(query):
    if not query:
        r = requests.get('https://apibay.org/precompiled/data_top100_207.json')
    else:
        r = requests.get(f"https://apibay.org/q.php?q={query}&cat=200")

    content = r.content
    parsed = json.loads(content)
    return parsed


# output easily manageable array
def info_to_arr(parsed):
    movies = []
    counter = 1

    for torrent in reversed(parsed):
        torrent_id = torrent["id"]
        magnet = torrent["info_hash"]
        name = torrent["name"]
        size_bytes = torrent["size"]
        seeders = torrent["seeders"]
        leechers = torrent["leechers"]

        # format size of movie
        if size_bytes > 1000000000:
            prefixer = "GiB" 
            size_xib = size_bytes / 1024 / 1024 / 1024
        else:
            prefixer = "MiB"
            size_xib = size_bytes / 1024 / 1024

        print((str(counter) + ".").ljust(4), name, str("%.2f" % size_xib) + " " + prefixer, seeders, leechers)
        counter += 1

        # movie is stored to array as id | magnet hash | name | size | seeders | leechers
        item = str(torrent_id) + ", " + magnet + ", " + name + ", "\
             + str(size_bytes) + ", " + str(seeders) + ", " + str(leechers)

        movies.append(item)
    
    print()

    return movies

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

        for torrent in parsed:
            #torrent_id = torrent["id"]
            #magnet = torrent["info_hash"]
            #name = torrent["name"]
            size_bytes = torrent["size"]
            #seeders = torrent["seeders"]
            #leechers = torrent["leechers"]

            # format size of movie
            if int(size_bytes) > 1000000000:
                prefixer = "GiB" 
                size_bytes = round((int(size_bytes) / 1024 / 1024 / 1024), 2)
            else:
                prefixer = "MiB"
                size_bytes = round((int(size_bytes) / 1024 / 1024), 1)

            torrent["size"] = str(size_bytes) + " " + prefixer

        return parsed
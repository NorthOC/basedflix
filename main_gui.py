import src.scraper as scrape
from src.streamer import stream_me_matey
from tkinter import *
import tkinter as tk
from tkinter import ttk
import subprocess
import urllib.parse as urlparse


HEIGHT = 800
WIDTH = 600
# Supported players
PLAYERS = ["-", "mpv", "vlc"]

# Focus on Ok button
def clickButton(event):
    widget = root.focus_get()
    if widget != root:
        widget.invoke()

def searcher(event):
    search_btn.invoke()


def stream_movie(event):

    tree = event.widget

    if tree.identify("region", event.x, event.y) != "heading":
        movie = {}
        p = w.get()
        print(p)

        for item in tree.selection():
            movie = top_parsed[int(item)]
            print("selected items:", movie)

            if movie["info_hash"] == '0000000000000000000000000000000000000000':
                return
            streaming = stream_me_matey(movie["info_hash"], p, True)
        
        # urlparse encodes the movie title with url syntax
        magnet = f"magnet:?xt=urn:btih:{movie['info_hash']}&dn={urlparse.quote(movie['name'])}&"\
            f"tr=udp%3A%2F%2Ftracker.coppersurfer.tk%3A6969%2Fannounce&tr=udp%3A%2F%2F"\
            f"tracker.openbittorrent.com%3A6969%2Fannounce&tr=udp%3A%2F%2F9.rarbg.to%3A2710%2F"\
            f"announce&tr=udp%3A%2F%2F9.rarbg.me%3A2780%2Fannounce&tr=udp%3A%2F%2F9.rarbg.to%3A2730%2F"\
            f"announce&tr=udp%3A%2F%2Ftracker.opentrackr.org%3A1337&tr=http%3A%2F%2Fp4p.arenabg.com%3A1337%2F"\
            f"announce&tr=udp%3A%2F%2Ftracker.torrent.eu.org%3A451%2Fannounce&tr=udp%3A%2F%2F"\
            f"tracker.tiny-vps.com%3A6969%2Fannounce&tr=udp%3A%2F%2Fopen.stealth.si%3A80%2Fannounce"
        
        # pop up window
        pop_up = tk.Toplevel()
        pop_up.geometry("400x300")

        # if media player found
        if streaming:
            try:
                subprocess.run(["webtorrent", "--version"] )
                pop_up.title("Success!")
                label_txt = "Loading stream...\nYou may close this window"

                # runs the streaming client
                subprocess.Popen(["webtorrent", f"{magnet}", f"--{p}"])
            except FileNotFoundError:

                label_txt = "Error, please install webtorrent-cli using Node."
                pop_up.title("webtorrentError")
        else:
            pop_up.title("MediaPlayerError")
            
            if p == "-":
                label_txt = "Please select a media player"
            else:
                label_txt = f"{p} player not detected.\nYou can try installing it, or using another player."

        la = tk.Label(pop_up, text=label_txt)
        la.pack(pady=10, padx=10)

        btn = tk.Button(pop_up, text="Ok", command=pop_up.destroy)
        btn.pack(padx=10, pady=10)

        pop_up.bind("<Return>", clickButton)

        pop_up.focus()
        btn.focus()
        
        pop_up.mainloop()


def get_movies(title="", clear=False):

    # clear search bar
    if clear:
        entry.delete(0, 'end')

    # search query
    parsed_json = scrape.parse_me_matey(str(title))
    return parsed_json

# Creates the gui list of movies
def display_movies(movie_list, parsed_json):

    global top_parsed
    top_parsed = parsed_json

    movie_list.delete(*movie_list.get_children())

    counter = 1

    for torrent in parsed_json:

        name = torrent["name"]
        size_bytes = torrent["size"]
        seeders = torrent["seeders"]
        leechers = torrent["leechers"]

        movie_list.insert(parent='',index='end',iid=f"{counter-1}",text='',
            values=(str(counter),name, size_bytes, seeders, leechers))
        counter += 1
    
    # for arrow key and double click functionality
    movie_list.focus_set()
    movie_list.selection_set(0)
    movie_list.focus(0)
    movie_list.bind("<Double-1>", stream_movie)
    movie_list.bind("<Return>", stream_movie)

# main window
root = tk.Tk()
root.minsize(800,600)
root.title("Basedflix")
root.configure(bg="#202124")


# styling list
style = ttk.Style()
style.configure("TCombobox", borderwidth=0, highlightthickness=0, arrowcolor="white")
style.map("TCombobox", 
                relief="flat",
                selectbackground= [('readonly','#303134')],
                selectforeground= [('readonly',"#bdc1c6")],
                selectborderwidth= [('readonly',0)],
                foreground= [('readonly',"#bdc1c6")],
                fieldbackground= [('readonly','#303134')],
                borderthickness= [('readonly',0)],
                highlightthickness= [('readonly',0)],
                background= [('readonly','#303134')])

style.configure("Treeview", background="#303134", highlightthickness=0,
 foreground="#bdc1c6", fieldbackground="#303134", borderwidth=0)
style.configure("Treeview.Heading", background="#303134", foreground="#bdc1c6", borderwidth=1, relief="solid")
style.map("Treeview.Heading",
                background = [('pressed', '!focus',"#303134" ),
                              ('active', "#303134"),
                              ('disabled', '#303134')],
                foreground = [('pressed', '!focus',"#bdc1c6" ),
                              ('active', "#bdc1c6"),
                              ('disabled', '#bdc1c6')])
style.map('Treeview', background=[('selected', '#3c4043')])

style.layout('arrowless.Vertical.TScrollbar', 
         [('Vertical.Scrollbar.trough',
           {'children': [('Vertical.Scrollbar.thumb', 
                          {'expand': '1', 'sticky': 'nswe'})],
            'sticky': 'ns'})])
style.configure('TScrollbar', troughcolor="#202124", borderwidth=0, highlightthickness=0, arrowcolor="green") 
style.configure('CustomScroll.Horizontal.TScrollbar',background='blue')

# upper bar for search and buttons
frame_top = tk.Frame(root, bg="#202124")

frame_top.place(relheight=0.05, relwidth=0.8, relx=0.5, rely=0.1, anchor="n")

# for movie list
frame_bottom = tk.Frame(root, bg="#202124", highlightthickness=0)
frame_bottom.place(relheight=0.8, relwidth=0.8, relx=0.5, rely=0.16, anchor="n")

movie_list = ttk.Treeview(frame_bottom)

movie_list['columns'] = ('movie_id', 'movie_title', 'movie_size', 'movie_seeders', 'movie_leechers')

movie_list.heading("#0",text="",anchor="center")
movie_list.heading("movie_id",text="Id",anchor="center")
movie_list.heading("movie_title",text="Title",anchor="center")
movie_list.heading("movie_size",text="Size",anchor="center")
movie_list.heading("movie_seeders",text="Seeders",anchor="center")
movie_list.heading("movie_leechers",text="Leechers",anchor="center")

movie_list.column("#0", width=0,  stretch=False)
movie_list.column("movie_id",anchor="center", width=50, stretch=False)
movie_list.column("movie_title",anchor="w", width=200)
movie_list.column("movie_size",anchor="center", width=100, stretch=False)
movie_list.column("movie_seeders",anchor="center", width=100, stretch=False)
movie_list.column("movie_leechers",anchor="center", width=115, stretch=False)

movie_list.place(relheight=1, relwidth=1)

# Scroll bar
scroll_bar = ttk.Scrollbar(movie_list, orient="vertical", command=movie_list.yview, style='arrowless.Vertical.TScrollbar')
scroll_bar.pack(side='right', fill='y')
movie_list.configure(yscrollcommand=scroll_bar.set)

# Search and Media player labels
s_label = tk.Label(root, text="Search:", background="#202124", foreground="#e8eaed")
p_label = tk.Label(root, text="Player:", background="#202124", foreground="#e8eaed")

s_label.place(relx=0.1, rely=0.06)
p_label.place(relx=0.76, rely=0.06)

search_btn = tk.Button(frame_top, text="Search", bg="#303134", fg="#e8eaed", borderwidth=0, activebackground="#404144",activeforeground="#e8eaed",highlightbackground="#5f6063", highlightcolor="#7a7c80",
                    command=lambda:display_movies(movie_list, get_movies(entry.get())))

search_btn.place(relheight=0.7, relwidth=0.15, relx=0.51)

top_btn = tk.Button(frame_top, text="Top 100", bg="#303134", fg="#e8eaed", borderwidth=0, activebackground="#404144",activeforeground="#e8eaed",highlightbackground="#5f6063", highlightcolor="#7a7c80",
                    command=lambda:display_movies(movie_list, get_movies(clear=True)))
top_btn.place(relheight=0.7, relwidth=0.15, relx=0.67)

#search bar
entry = tk.Entry(frame_top, bg="#303134", foreground="#e8eaed" ,borderwidth=0, highlightthickness=1, highlightbackground="#5f6063",highlightcolor="#7a7c80", insertbackground="#e8eaed")
entry.place(relheight=0.7, relwidth=0.5, relx=0)
entry.bind("<Return>", searcher)

# debug
#def ok(event):
#    print ("value is:" + w.get())

# media player select box
w = ttk.Combobox(frame_top, state="readonly")
w['values'] = tuple(PLAYERS)
w.set(PLAYERS[0])
w.current(0)
w.place(relheight=0.7, relwidth=0.1, relx=0.83)
#w.bind("<<ComboboxSelected>>", ok)

root.mainloop()
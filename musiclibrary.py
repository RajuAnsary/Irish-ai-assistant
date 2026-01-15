import webbrowser

musics ={
    "the floor": "https://www.youtube.com/watch?v=t4H_Zoh7G5A",
    "shakira": "https://www.youtube.com/watch?v=pRpeEdMmmQ0",
    "let me love you": "https://www.youtube.com/watch?v=euCqAq6BRa4",
    "espresso": "https://www.youtube.com/watch?v=eVli-tstM5E",
    "despacito": "https://www.youtube.com/watch?v=kJQP7kiw5Fk",
    "believer": "https://www.youtube.com/watch?v=7wtfhZwyrcc",
    "shape of you": "https://www.youtube.com/watch?v=JGwWNGJdvx8",  
    "perfect": "https://www.youtube.com/watch?v=2Vv-BfVoq4g",
    "kesariya": "https://www.youtube.com/watch?v=BddP6PYo2gs",
    "dilbar": "https://www.youtube.com/watch?v=ryP-Lh_LAJU&list=RDryP-Lh_LAJU&start_radio=1",
    "aadat": "https://www.youtube.com/watch?v=lcw4TDMBjZA"

}

def clean_text(text):
    text = text.lower()
    for word in ["play", "song", "music", "please"]:
        text = text.replace(word, "")
    return text.strip()

# import webbrowser

def play_song(command):
    command = clean_text(command)

    # 1️⃣ Try local library first
    for song in musics:
        if song in command or command in song:
            webbrowser.open(musics[song])
            return song, True

    # 2️⃣ If not found → search on YouTube
    search_url = "https://www.youtube.com/results?search_query=" + command.replace(" ", "+")
    webbrowser.open(search_url)
    return command, False

import app
import speech_recognition as sr
# import pyttsx3
import time
import webbrowser
import musiclibrary
import requests
import os
import uuid
from local_ai import ask_local_ai
from gtts import gTTS
import pygame



r = sr.Recognizer()

news_api_key = "8182c76eef124ef3b224159c5955075c"

pygame.mixer.init()
def speak(text):
    tts = gTTS(text)
    tts.save('temp.mp3')

    # Initialize Pygame mixer
    # pygame.mixer.init()

    # Load the MP3 file
    pygame.mixer.music.load('temp.mp3')

    # Play the MP3 file
    pygame.mixer.music.play()

    # Keep the program running until the music stops playing
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

    pygame.mixer.music.unload()
    os.remove('temp.mp3')



# ---------- COMMAND HANDLER ----------
def processCommand(command):
    command = command.lower()
    print("Processing:", command)

    if "google" in command:
        speak("Opening Google")
        webbrowser.open("https://www.google.com")

    elif "youtube" in command:
        speak("Opening YouTube")
        webbrowser.open("https://www.youtube.com")

    elif "instagram" in command:
        speak("Opening Instagram")
        webbrowser.open("https://www.instagram.com")

    elif "facebook" in command:
        speak("Opening Facebook")
        webbrowser.open("https://www.facebook.com")

    elif "linkedin" in command:
        speak("Opening LinkedIn")
        webbrowser.open("https://www.linkedin.com")


    elif command.lower().startswith("play"):
        speak("Playing music")

        song, found = musiclibrary.play_song(command)

        if found:
            speak(f"Playing {song}")
        else:
            speak(f"I couldn't find it in my library. Playing {song} on YouTube")




    elif "news" in command:
       
        speak("Opening news")
        r= requests.get(f"https://newsapi.org/v2/top-headlines?sources=bbc-news&apiKey={news_api_key}")
        data = r.json()

        articles =data.get("articles", [])
        for article in articles:
            title = article.get("title")
            if title:
                  speak(title)

        

    else:
        answer = ask_local_ai(command)
        speak(answer)
        
# ---------- MAIN LOOP ----------


def start_iris(iris_event):
    print("Iris thread started")
    speak("Hello, I am Irish")



    while iris_event.is_set():

        try:
            with sr.Microphone() as source:
                r.adjust_for_ambient_noise(source, duration=0.8)
                print("🎤 MIC OPENED - LISTENING")
                audio = r.listen(source, phrase_time_limit=5)

            word = r.recognize_google(audio, language="en-IN")
            print("Heard:", word)

        except sr.UnknownValueError:
            continue

        if "iris" not in word.lower():
            continue
       
        speak("Yes, I'm listening")

        try:
            with sr.Microphone() as source:
                r.adjust_for_ambient_noise(source, duration=0.6)
                audio = r.listen(source, phrase_time_limit=6)

            command = r.recognize_google(audio, language="en-IN")
            
            processCommand(command)

        except sr.UnknownValueError:
            speak("I did not understand")

        time.sleep(1)
app.current_status = "Idle"
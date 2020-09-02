import pyttsx3 # pip install pyttsx3
import datetime 
import speech_recognition as sr # pip install speechrecogniton
import pyaudio # pip install win and  pipwin install pyaudio
import wikipedia # pip install wikipedia
import webbrowser
import os

import socket # for microfon eror
socket.getaddrinfo('localhost', 8080)

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
    
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")
    
    else:
        speak("Good Evening")
    
    speak("I am jarvis sir. Please tell me how may I help you")

def takeCommand():
    """it takes command """
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listning...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said:{query}\n")
    
    except Exception :
        # print(e)
        print("Say that again please...")
        return "none"
    return query

if __name__=="__main__":
    wishMe()
    while True:
        query = takeCommand().lower()
        
        # Logic for exicuting tasks based on query
        if 'wikipedia' in query:
            speak('Searching wikipedia...')
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences=1)
            speak("According to wikipedia")
            print(results)
            speak(results)
        
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'play music' in query:
            music_dir = "C:\\Users\\asp\\Desktop\\Py projects\\music"
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))
        
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")
        
        elif 'open vs code'in query:
            codePath = "C:\\Users\\asp\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'open sublime' in query:
            codePath = "C:\\Program Files\\Sublime Text 3\\sublime_text.exe"
            os.startfile(codePath)
        
        elif 'bbd file' in query:
            filePath = "C:\\Users\\asp\\Desktop\\BBD"
            os.startfile(filePath)

        elif 'polytechnic file' in query:
            filePath = "C:\\Users\\asp\\Desktop\\Polytechnic"
            os.startfile(filePath)
        

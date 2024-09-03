import speech_recognition as sr
import os
import win32com.client
import webbrowser
import datetime
from AppOpener import open, close
import subprocess

speaker = win32com.client.Dispatch("SAPI.SpVoice")


def say(text):
    while 1:
        a = text
        speaker.Speak(a)
        break


def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 0.5
        audio = r.listen(source)
        try:
            query = r.recognize_google(audio, language="en-in")
            print(f"User said: {query}")
            return query
        except Exception as e:
            return "Some Error Occurred. Sorry from Jarvis"


def open_camera():
    try:
        subprocess.run('start microsoft.windows.camera:', shell=True)
    except Exception as e:
        say(f"An error occurred: {e}")


def close_camera():
    try:
        subprocess.run('taskkill /IM WindowsCamera.exe /F', shell=True)
        print("Camera app closed successfully.")
    except Exception as e:
        print(f"An error occurred while closing the camera: {e}")


if __name__ == '__main__':
    say("Hello I am Jarvis how can i help you")
    while True:
        print("Listening...")
        query = take_command()
        # todo:Add more sites
        sites = [["Youtube", "https://youtube.com"], ["Wikipedia", "https://wikipedia.com"],
                 ["Google", "https://google.com"], ["Instagram", "https://instagram.com"],]
        for site in sites:
            if f"Open {site[0]}".lower() in query.lower():
                say(f"Opening {site[0]} as you requested")
                webbrowser.open(site[1])

        if "open music" in query:
            MusicPath = "/Users/Joaquim/Downloads/Alarm.mp3"
            os.system(MusicPath)

        if "the time" in query:
            strfTime = datetime.datetime.now().strftime("%H:%M:%S")
            say(f"Sir the time is {strfTime}")

        # todo:Add more apps
        Apps = ["discord", "spotify"]
        for app in Apps:
            if f"open {app}" in query:
                say(f"opening {app}")
                open(f"{app}")

            if f"close {app}" in query:
                say(f"closing {app}")
                close(app)

        if f"open camera" in query:
            open_camera()
        if f"close camera" in query:
            close_camera()

import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib
import random

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice','voices[0].id')
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
        speak("Good Evening!")
    print("Hello Mohak, I am Jarvis. Please tell me how can i help you")
    speak("Hello Mohak, I am Jarvis. Please tell me how can i help you")

def takeCommand():
     r = sr.Recognizer()
     with sr.Microphone() as source:
         print("Listening....")
         r.pause_threshold = 1
         audio = r.listen(source)
     try:
         print("Recognizing....")
         query = r.recognize_google(audio,language='en-in')
         print(f"User said: {query}\n")
     except Exception as e:
         print("Say that again please....")
         return "None"
     return query

def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('aniketrana776@gmail.com','password')
    server.sendmail('aniketrana776@gmail.com',to,content)
    server.close()

if __name__=="__main__":
    wishMe()
    while True:
        query = takeCommand().lower()
        if 'wikipedia' in query:
            speak('Searching Wikipedia....')
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'what can you do' in query:
            print("I can play a song, show your photos, search any wikipedia and many more")
            speak("I can play a song, show your photos, search any wikipedia and many more")
        elif 'who are you' in query:
            print("I am your personal assistant")
            speak("I am your personal assistant")
        elif 'what is jarvis' in query:
            print("Jarvis is a Artificial Intelligence discovery")
            speak("Jarvis is a Artificial Intelligence discovery")
        elif 'you are bad' in query:
            print("Sorry for the bad experience")
            speak("Sorry for the bad experience")
        elif 'you are good' in query:
            print("Thanks, Glad you like me")
            speak("Thanks, Glad you like me")
        elif 'thanks' in query:
            print("No problem")
            speak("No problem")
        elif 'how are you' in query:
            print("I am good Mohak")
            speak("I am good Mohak, How about you")
        elif 'i am good' in query:
            print("That sounds good")
            speak("That sounds good")
        elif 'weather' in query:
            webbrowser.open("accuweather.com")
        elif 'open google' in query:
            webbrowser.open("google.com")
        elif 'open gmail' in query:
            webbrowser.open("gmail.com")
        elif 'open udemy' in query:
            webbrowser.open("udemy.com")
        elif 'open amazon' in query:
            webbrowser.open("amazon.com")
        elif 'open photos' in query:
            photo_dir = 'C:\\Users\\MOHAK GOEL\\Desktop\\Photos'
            photo = os.listdir(photo_dir)
            print(photo)
            os.startfile(os.path.join(photo_dir))
        elif 'open videos' in query:
            video_dir = 'C:\\Users\\MOHAK GOEL\\Desktop\\Videos'
            video = os.listdir(video_dir)
            print(video)
            os.startfile(os.path.join(video_dir))
        elif 'play song' in query:
            music_dir = 'C:\\Users\\MOHAK GOEL\\Desktop\\Songs'
            music = os.listdir(music_dir)
            print(music)
            os.startfile(os.path.join(music_dir , music[random.randint(1,8)]))
        elif 'open movies' in query:
            movie_dir = 'C:\\Users\\MOHAK GOEL\\Desktop\\Movies'
            movie = os.listdir(movie_dir)
            print(movie)
            os.startfile(os.path.join(movie_dir))
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            print(strTime)
            speak(f"Sir, the time is{strTime}")
        elif 'open pycharm' in query:
            pycharmPath = "C:\\Program Files\\JetBrains\\PyCharm 2019.1.3\\bin\\pycharm64.exe"
            os.startfile(pycharmPath)
        elif 'email to ashok' in query:
            try:
                speak("What should i say")
                content = takeCommand()
                to = "ashokgoel700@gmail.com"
                sendEmail(to,content)
                speak("Email has been sent!")
            except Exception as e:
                speak("Sorry Mohak your email has not been sent because of some technical issue!")

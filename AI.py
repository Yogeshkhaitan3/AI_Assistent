import os
import webbrowser
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import smtplib
from googlesearch import search

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')  # getting details of current voice
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("good morning!")

    elif hour >= 12 and hour < 18:
        speak("good Afternoon!")

    else:
        speak("good Evening!")

    speak("I am AI!please tell me how may i help you ")


def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as m:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(m)

    try:
        print("Recognizing...")
        # Using google for voice recognition.
        fun = r.recognize_google(audio, language='en-in')
        print("User said: ", fun)  # User query will be printed.

    except Exception as e:
        # print(e)
        # Say that again will be printed in case of improper voice
        print("Say that again please...")
        return "None"  # None string will be returned
    return fun


if __name__ == "__main__":
    wishme()
    while True:
        fun = takecommand().lower()

        if 'wikipedia' in fun:
            print("Searching wikipedia!")
            speak('Searching Wikipedia...')
            fun = fun.replace("wikipedia", "")
            results = wikipedia.summary(fun, sentences=1)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        elif "shut down" in fun:
            x = "are you sure to shut down your pc"
            speak(x)
            x1 = takecommand()
            if "yes" in x1:
                g = "thank you,for your confirmation , now i am goining to shut down your pc"
                speak(g)
        # todo shut down
                os.system('shutdown /s /t 1')
            else:
                speak("thank you,for your confirmation , now i am rejected your command")
        elif "restart" in fun:
            x = "are you sure to restart your pc"
            speak(x)
            x1 = takecommand()
            if "yes" in x1:
                g = "thank you,for your confirmation , now i am goining to restart your pc"
                speak(g)
            # todo shut down
                os.system('shutdown /r /t 1')
            else:
                speak("thank you,for your confirmation , now i am rejected your command")
        elif 'open youtube' in fun:
            webbrowser.open("youtube.com")
        elif 'open google' in fun:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in fun:
            webbrowser.open("stackoverflow.com")
        elif 'the time' in fun:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif "open gmail" in fun:
            g = "thank you,for your confirmation , now i am goining to open Gmail"
            speak(g)
            webbrowser.open("http://gmail.com")
        
        else:
            g = "I am searching on google"
            speak(g)
            my_list = []
            speak("According to google I am opening a web browser for you query")
            for i in search(fun, tld='com', lang='en', num=10, start=0, stop=1, pause=2.0):

                my_list.append(i)
                webbrowser.open(i)
            
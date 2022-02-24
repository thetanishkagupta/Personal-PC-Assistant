import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import os
import time
import pyjokes
import subprocess
from ecapture import ecapture as ec
import wolframalpha
import randfacts
import json
import requests

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
def speak(text):
    engine.say(text)
    engine.runAndWait()

def wishMe():
    hour=datetime.datetime.now().hour
    if hour>=0 and hour<12:
        speak("Hello,Good Morning")
        print("Hello,Good Morning")
    elif hour>=12 and hour<18:
        speak("Hello,Good Afternoon")
        print("Hello,Good Afternoon")
    else:
        speak("Hello,Good Evening")

def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        r.energy_threshold = 10000
        print("Listening...")
        audio=r.listen(source)

        try:
            statement=r.recognize_google(audio,language='en-in')
            print(f"user said:{statement}\n")

        except Exception as e:
            speak("Pardon me, please say that again")
            return "None"
        return statement

def note(statement):
    date = datetime.datetime.now()
    file_name = str(date).replace(":","-") + "-note.txt"
    with open(file_name, "w") as f:
        f.write(statement)

    subprocess.Popen(["notepad.exe", file_name])

print("Loading your AI personal assistant jini")

if __name__=='__main__':
    wishMe()
    speak('Hello Sir, I am jini, your personal pc assistant.')
    while True:
        speak(" how can I help you sir?")
        statement = takeCommand().lower()
        if statement==0:
            continue
        if "good bye" in statement or "ok bye" in statement or "stop" in statement:
            speak('your personal assistant jini is shutting down,Good bye')
            print('your personal assistant jini is shutting down,Good bye')
            break
        if 'wikipedia' in statement:
            speak('Searching Wikipedia...')
            statement = statement.replace("wikipedia", "")
            results = wikipedia.summary(statement, sentences=3)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in statement:
            webbrowser.open_new_tab("https://www.youtube.com")
            speak("youtube is open now")
            time.sleep(5)

        elif 'open google' in statement:
            webbrowser.open_new_tab("https://www.google.com")
            speak("Google chrome is open now")
            time.sleep(5)

        elif 'where is' in statement:
            ind = statement.lower().split().index("is")
            location = statement.split()[ind + 1:]
            url = "https://www.google.com/maps/place/" + "".join(location)
            speak("this is where" + str(location) + "is.")
            webbrowser.open(url)

        elif 'open gmail' in statement:
            webbrowser.open_new_tab("gmail.com")
            speak("Google Mail is open now")

        elif 'open stack overflow' in statement:
            webbrowser.open_new_tab("https://stackoverflow.com")
            speak("Stack overflow is open now")

        elif 'how are you' in statement:
            speak("I am fine, Thank you")
            speak("How are you, Sir")

        elif 'fine' in statement or "good" in statement:
            speak("It's good to know that your fine")

        elif "will you be my gf" in statement or "will you be my bf" in statement:
            speak("I'm not sure about, may be you should give me some time")

        elif "i love you" in statement:
            speak("It's hard to understand")

        elif 'joke' in statement:
            speak("Sure sir, get ready for some chuckles")
            speak(pyjokes.get_joke())

        elif 'time' in statement:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"the time is {strTime}")

        elif 'news' in statement:
            news = webbrowser.open_new_tab("https://timesofindia.indiatimes.com/home/headlines")
            speak('Here are some headlines from the Times of India,Happy reading')
            time.sleep(6)

        elif "camera" in statement or "take a photo" in statement:
                ec.capture(0, "robo camera", "img.jpg")

        elif 'search' in statement:
            statement = statement.replace("search", "")
            webbrowser.open_new_tab(statement)
            time.sleep(5)

        elif 'ask' in statement:
            speak('I can answer to computational and geographical questions  and what question do you want to ask now')
            question = takeCommand()
            app_id = "5XQTE6-9LXA4W67Q3 "
            client = wolframalpha.Client('R2K75H-7ELALHR35X')
            res = client.query(question)
            answer = next(res.results).text
            speak(answer)
            print(answer)

        elif 'who are you' in statement or 'what can you do' in statement:
            speak('I am jini version 1 point O your personal assistant. I am programmed to do minor tasks like'
                  'opening youtube,google chrome, gmail and stackoverflow ,predict time,take a photo,search wikipedia,predict weather'
                  'In different cities, get top headline news from times of india and you can ask me computational or geographical questions too!')

        elif "who made you" in statement or "who created you" in statement or "who discovered you" in statement:
            speak("I was built by tanishka")
            print("I was built by tanishka")

        elif "weather" in statement:
            api_key = "bcc03d25de369c800d87e54e1e3239b9"
            base_url = "https://api.openweathermap.org/data/2.5/weather?"
            speak("what is the city name")
            city_name = takeCommand()
            complete_url = base_url + "appid=" + api_key + "&q=" + city_name
            response = requests.get(complete_url)
            x = response.json()
            if x["cod"] != "404":
                y = x["main"]
                current_temperature = y["temp"]
                current_humidiy = y["humidity"]
                z = x["weather"]
                weather_description = z[0]["description"]
                speak(" Temperature in kelvin unit is " +
                      str(current_temperature) +
                      "\n humidity in percentage is " +
                      str(current_humidiy) +
                      "\n description  " +
                      str(weather_description))
                print(" Temperature in kelvin unit = " +
                      str(current_temperature) +
                      "\n humidity (in percentage) = " +
                      str(current_humidiy) +
                      "\n description = " +
                      str(weather_description))

        elif "note" in statement or "remember this" in statement:
            speak("What would you like me to write down?")
            note_statement = takeCommand()
            note(note_statement)
            speak("I have made a note of that")

        elif "log off" in statement or "sign out" in statement:
            speak("Ok , your pc will log off in 30 sec make sure you exit from all applications")
            subprocess.call(["shutdown", "/l"])

        time.sleep(3)


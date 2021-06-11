from math import trunc
import subprocess
import pyttsx3
import time as t
from datetime import datetime
import speech_recognition as  sr
import wikipedia
import webbrowser
import os
import smtplib
import pyautogui
import sys
import requests
import json
import datetime
from subprocess import Popen, CREATE_NEW_CONSOLE
import psutil
import random
import signal
from sys import executable

from bs4 import BeautifulSoup 


engine = pyttsx3.init('sapi5')
engine.setProperty("rate", 140)
voices = engine.getProperty('voices')

print(voices[1].id)

engine.setProperty('voice', voices[0].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait ()


def screenshot():
    for i in range(60):
        
        ss = pyautogui.screenshot()
        
        ss.save(f"SS {i}.png")
        break


def convertTime(seconds):
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    hr = "hour"

    sc = "seconds"

    mn = "minetes"


    return f"%d {hr} %02d {mn} %02d {sc}" % (hours, minutes, seconds)

def NewsFromBBC():
     
    # BBC news api
    # following query parameters are used
    # source, sortBy and apiKey
    query_params = {
      "source": "bbc-news",
      "sortBy": "top",
      "apiKey": "bbecb7e4d276407f883c1c46de073048"
    }
    main_url = " https://newsapi.org/v1/articles"
 
    # fetching data in json format
    res = requests.get(main_url, params=query_params)
    open_bbc_page = res.json()
 
    # getting all articles in a string article
    article = open_bbc_page["articles"]
 
    # empty list which will
    # contain all trending news
    results = []
     
    for ar in article:
        results.append(ar["title"])
         
    for i in range(len(results)):
         
        # printing all trending news
        print(i + 1, results[i])

    speak(results)

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('Your Email', 'Your Email Password')
    server.sendmail('stvshaji@gmail.com', to, content)
    server.close()
def search_wikihow(query, max_results, lang='en'):
    return list(WikiHow.search(query, max_results, lang))
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("I am Jarvis Sir. Please tell me how may I help you")

def takeCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print(e)

        print("Say that again please....")
        return "None"

    return query


engine.setProperty('voice', voices[0].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait ()

yo = Popen([sys.executable, 'fox.py'], creationflags=CREATE_NEW_CONSOLE)


def killProcess():
     # runs myPyScript.py
     yo.terminate()


     
    
  


def getTimeInput():
    hour = 0
    minutes = 3
    seconds = 0
    time_interval = seconds+(minutes*60)+(hour*3600)
    t.sleep(time_interval)
    return time_interval 



def log():
    now = datetime.datetime.now()
    start_time = now.strftime("%H:%M:%S")
    with open("log.txt", 'a') as f:
        f.write(f"You drank water {now} \n")
    return 0
  
  
  
  
def starttime(time_interval):

    if time_interval == True:
        
        t.sleep(time_interval)

def log():
	now = datetime.datetime.now()
	start_time = now.strftime("%H:%M:%S")
	with open("waterlog.txt", 'a') as f:
		f.write(f"You drank water {now} \n")
	return 0

    

#It takes microphone input from user and returns string output
#Logic for executing task based on query
if __name__ == "__main__":
    
    wishMe()
    while True:


        

        

        query = takeCommand().lower()


        

    
        
    

        battery = psutil.sensors_battery()


        

               
        if int(psutil.sensors_battery().percent)>94 and battery.power_plugged == True:
            
            speak("Sir, your laptop battery has been fully charged you can disconnect the charger now")
  

        elif 'wikipedia' in query:
            
            speak("Searching Wikipedia....")
            
            query = query.replace("wikipedia", "")
            
            results = wikipedia.summary(query, sentences= 2)
            
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'wire' in query:
            speak("Fetching the latest news...")
            t.sleep(20)
            speak("Sir I am going to be reading the top headlines from todays news")
            NewsFromBBC()
            
        elif 'body' in query:

            log()
            

            killProcess()
        elif 'open youtube' in query:
            
            webbrowser.open("youtube.com")
            
        elif 'screenshot' in query:
            speak("I have taken the screenshot of the page succesfully sir")
            screenshot()


        elif 'battery left' in query:

            responses = ["i feel that", "according to me", "i am pretty sure that", "from my assumption", "from my calculations", "from what i think"]

            battery = psutil.sensors_battery()



            speak(f"The Charge in percentage is {battery.percent} percent")

            if battery.power_plugged == True:

                speak("The computer is charging right now sir")

            else:
                
                speak(f"{random.choice(responses)} The battery left right now will approximately last for {convertTime(battery.secsleft)} Sir !")
        elif 'open google' in query:
            
            webbrowser.open("google.com")
       
        elif 'open brilliant' in query:
            webbrowser.open("https://www.brilliantpalaelearn.com/")
        elif 'play music' in query:
            music_dir = "D:\\Users\\AMALSHAJI\\Music\\Songs"
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%I:%M" "%p")    
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            teams = "C:\\Users\\AMALSHAJI\\AppData\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(teams)
        elif 'open teams' in query:
            speak("opening microsoft teams sir")
            code = "C:\\ProgramData\\AMALSHAJI\\Microsoft\\Teams\\Update.exe --processStart Teams.exe"
            os.system(code)

        elif 'thank you' in query:

            speak("Your welcome sir my pleasure helping you !")
            
        elif 'the weather' in query:
              
            search = "temperature in kerala"
            
            url = f"https://www.google.com/search?q={search}"
            
            r = requests.get(url)
            
            data = BeautifulSoup(r.text,"html.parser")
            
            temp = data.find("div",class_="BNeawe").text
            
            

            CITY = "Kerala"
            BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"

            API_KEY = "2d2409cc015c720c6ffc476eb630c5f3"

            url = BASE_URL + "q=" + CITY + "&appid=" + API_KEY

            res = requests.get(url)

            data = res.json()

            weather = data['weather'] [0] ['main'] 



            current_humidity = data['main']['humidity']

            wind_speed = data['wind'] ['speed']

            latitude = data['coord']['lat']

            longitude = data['coord']['lon']

            description = data['weather'][0]['description']

            speak('I am going to be telling the weather in Kerala right now sir')

            speak(f"current {search} is {temp}")

            speak(f"The humidity is {current_humidity} percent")

            speak(f"The wind speed is: {wind_speed} metres per second")

            speak(f"The overall weather condition is {description}")
        
        elif 'search in chrome' in query:
            speak("What should I search ?")

            chrome_path = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe %s"

            
            r = sr.Recognizer()

            with sr.Microphone() as source:
                print("Say something")
                audio = r.listen(source)
                print("done")

            try:

                text = r.recognize_google(audio)
                print('Google thinks you said: \n' +text +'.com')
    
                webbrowser.open_new(f"https://www.google.com/search?q={text}")

            except Exception as e:
                print(e)

        elif 'class' in query:
            speak("Sure sir I'll remind you to join the computer class after 3 mineetes")

            man = getTimeInput()

            t.sleep(man)

            speak("Sir, it is time for you to drink water. Please get up from your desk and drink water")
        elif 'email for work' in query:
            
            try:
                
                speak("What should I say ?")
                
                content = takeCommand()
                
                to = "Person you want to send the mail to"
                
                sendEmail(to, content)
                
                speak("Email has been sent!")

            except Exception as e:
                print(e)

                speak("Sorry my friend Amal. I am unable to send this email at the moment")

        

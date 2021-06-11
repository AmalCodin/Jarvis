import speech_recognition
import time

import pyttsx3
import speech_recognition
import datetime


engine = pyttsx3.init('sapi5')
engine.setProperty("rate", 140)
voices = engine.getProperty('voices')

print(voices[1].id)

engine.setProperty('voice', voices[0].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait ()


def getTimeInput():
	hour = int(0)
	minutes = int(4)
	seconds = int(0)
	time_interval = seconds+(minutes*60)+(hour*3600)
	return time_interval


def log():
	now = datetime.datetime.now()
	start_time = now.strftime("%H:%M:%S")
	with open("log.txt", 'a') as f:
		f.write(f"You drank water {now} \n")
	return 0



def starttime(time_interval):
    
        
    time.sleep(time_interval)
    speak("Sir it is time to drink water now") 
        
    



if __name__ == '__main__':
    

    time_interval = getTimeInput()
            
    starttime(time_interval)

    while True:
        speak("Reminding you again to drink please confirm if you have already drank water so that I can log sir")

        
  



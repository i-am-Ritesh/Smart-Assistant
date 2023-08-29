from asyncore import ExitNow
from calendar import month
from cgitb import text
from distutils import command
from distutils.log import info
from imghdr import what
from importlib.resources import path
from logging.config import listen
from operator import truediv
import re
import pyttsx3 # pip install pyttsx3
import datetime #time and date updating
import speech_recognition as sr #recognition of our speech
import pywhatkit #for well defined functions
import wikipedia  #for the searching news in wikipedia
import pyjokes #for telling a programing jokes
import webbrowser #for using web activities
import os #for using OS of the system
 
 
 
listner=sr.Recognizer()
engine=pyttsx3.init()
voices = engine.getProperty("voices")
engine.setProperty("voice",voices[1].id)

 
 
 
def speak (audio):
    engine.say(audio)
    engine.runAndWait()
 
 
 
 
def time():
    time = datetime.datetime.now().strftime("%I %M:%p")
    speak(time)
 
 
def date ():
    year= int(datetime.datetime.now().year)
    month= int(datetime.datetime.now().month)
    date= int(datetime.datetime.now().day)
 
    speak(date)
    speak(month)
    speak(year)
 
def hour ():
    hour=datetime.datetime.now().hour
    if hour >=6 and hour <12 :
        speak("good morning sir")
    elif hour >=12 and hour <16:
        speak("good afternoon sir")
    elif hour >=16 and hour <19:
        speak("good evening sir")
    else:
        speak ("Good night sir")
 
 
def wishme(): #if moment in command
    hour()
    speak("the current time is")
    time ()
    speak("the current month")
    date()
    speak("logic at your service, how can i help you")
 
hour()
speak("logic at your service,how could i help you sir") 

 
 
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print ("listenting......")
        r.pause_threshold = 1
        audio = r.listen(source)
 
    try:
        print ("Recognizing.......")
        command = r.recognize_google(audio,language  ='en-in')
        if "logic" in command:
            command = command.replace("command","")
            print(command)
 
 
    except Exception as e:
        print(e)
       
 
        return "None"
    return command
 
 
def work():
    command = takecommand()
    if "play" in command:
        song = command.replace("play","")
        speak("playing" +song)
        pywhatkit.playonyt(song)
        print(command)

    elif "who is" in command:
        person = command.replace("who is","")
        info = wikipedia.summary(person,2)
        print(info)
        speak(info)
       
    elif "time " in command:
         print(command)
         time ()

    elif "hi" in command:
        speak("Hi  this is logic , how can i help you" )
        print(speak)
 
    elif" date" in command:
         print(command)
         date()
 
    elif "about yourself" in command:
        print(command)
        speak("Hi iam logic , i work for you , i am his voice assistant, i love to help him")
        print(speak)
 
    elif "joke" in command:
        print(command)
        speak(pyjokes.get_joke())
        
 
    elif "about me" in command:
        print(command)
        speak(" you are good person, you nice to me, you will reach your goals high,")
 
    elif "today" in command:
        print (command)
        wishme()
 
    elif "search " in command:
        command = command.replace("search","")
        text= "https://www.google.co.in/search?q="
        search_command = text + command
        webbrowser.open(search_command)
        speak("searching" + command)

    elif 'open youtube' in command:
            print(command)
            webbrowser.open("youtube.com")

        
    elif 'open google' in command:
            webbrowser.open("google.com")
 
    elif "note" in command:
        print(command)
        os.system("notepad")

 
    elif "music" in command:
        print(command)
        os.system("spotify")
 
    elif "file" in command:
        print(command)
        os.system("explorer.exe")
 
    elif "close" in command:
        print("Thank you")
        speak("its my pleasure to work for you ")
        exit()

    else:
        speak("say that again please")
       
while True:
    work()
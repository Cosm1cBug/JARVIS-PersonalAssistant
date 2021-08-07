# -*- coding: utf-8 -*-
import pyfiglet 
import pyttsx3
import datetime 
import os
import os.path
import subprocess
import time
import pyautogui
import psutil 
import pyjokes
import winshell
import json
import pywhatkit as kit 
import wolframalpha
import webbrowser as wb
import requests
import playsound
import wikipedia
import speech_recognition as sr
from contacts import *
import contact
import urllib 
import urlopen
from gtts import gTTS
from colors import red, green, blue
from colors import color


def banner():  
    ascii_banner = pyfiglet.figlet_format("J.A.R.V.I.S")
    print (green(ascii_banner))

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id ) # 1 = female, 0 = male
engine.setProperty('volume', 2)
engine.setProperty('rate', 200)


def voice_change(v):
    x = int(v)
    engine.setProperty('voice', voices[x].id)
    speak("done sir")


def speak(query):
    engine.say(query)
    engine.runAndWait()
    engine.stop()

def time():
    Time=datetime.datetime.now().strftime("%I:%M:%S") # for 12-hour clock
    speak("The current time is" + Time)
    
def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)
    speak("The current date is")
    speak(date)
    speak(month)
    speak(year)

def checktime(tt):
    hour = datetime.datetime.now().hour
    if ("morning" in tt):
        if (hour >= 6 and hour < 12):
            speak("Good morning sir")
        else:
            if (hour >= 12 and hour < 18):
                speak("it's Good afternoon sir")
            elif (hour >= 18 and hour < 24):
                speak("it's Good Evening sir")
            else:
                speak("it's Goodnight sir")
    elif ("afternoon" in tt):
        if (hour >= 12 and hour < 18):
            speak("it's Good afternoon sir")
        else:
            if (hour >= 6 and hour < 12):
                speak("Good morning sir")
            elif (hour >= 18 and hour < 24):
                speak("it's Good Evening sir")
            else:
                speak("it's Goodnight sir")
    else:
        speak("it's night sir!")

def wishme():
    speak("Welcome Back. All systems will be prepared in just a moment.")
    hour = datetime.datetime.now().hour
    if (hour >= 6 and hour < 12):
        speak("Good Morning sir!")
    elif (hour >= 12 and hour < 18):
        speak("Good afternoon sir")
    elif (hour >= 18 and hour < 24):
        speak("Good Evening sir")
    else:
        speak("Goodnight sir")

    #speak("Jarvis at your service, Please tell me how can i help you?")

def wishme_end():
    speak("signing off")
    hour = datetime.datetime.now().hour
    if (hour >= 6 and hour < 12):
        speak("Good Morning")
    elif (hour >= 12 and hour < 18):
        speak("Good afternoon")
    elif (hour >= 18 and hour < 24):
        speak("Good Evening")
    else:
        speak("Goodnight.. Sweet dreams")
    quit()

def note(note_text):  
    reminder_file = open("reminder.txt", 'a')
    reminder_file.write('\n')
    reminder_file.write(note_text)
    reminder_file.close()

    #date = datetime.datetime.now() 
    #file_name = str(date).replace(":","-") + "-note.txt"
    #with open(file_name,"a") as f:   
    #    f.write(note_text)
    #subprocess.Popen(["C:\\WINDOWS\\system32\\notepad.exe", file_name])


def screenshot():
    img = pyautogui.screenshot()
    img.save("C:\\Users\\Optimus\\Desktop\\VC\\ScreenShots")


def systemstatus():
    usage = str(psutil.cpu_percent())
    speak('CPU usage is at ' + usage)
    print('CPU usage is at ' + usage)
    battery = psutil.sensors_battery()
    speak("Battery is at")
    speak(battery.percent)
    print("battery is at:" + str(battery.percent))

def jokes():
    j = pyjokes.get_joke()
    print(j)
    speak(j)

def weather():
    api_key = "YOUR-API_KEY" #generate your own api key from open weather
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    speak("tell me which city")
    city_name = get_audio()
    complete_url = base_url + "appid=" + api_key + "&q=" + city_name
    response = requests.get(complete_url)
    x = response.json()
    if x["cod"] != "404":
        y = x["main"]
        current_temperature = y["temp"]
        current_pressure = y["pressure"]
        current_humidiy = y["humidity"]
        z = x["weather"]
        weather_description = z[0]["description"]
        r = ("in " + city_name + " Temperature is " +
             str(int(current_temperature - 273.15)) + " degree celsius " +
             ", atmospheric pressure " + str(current_pressure) + " hpa unit" +
             ", humidity is " + str(current_humidiy) + " percent"
             " and " + str(weather_description))
        print(r)
        speak(r)
    else:
        speak(" City Not Found ")

def personal():
    speak("I am JARVIS. Just a rather very intelligent system.")
    

def Introduction():
    speak("Allow me to introduce myself.")
    speak("I am jarvis a virtual artificial intelligence")
    speak("I am here to assist you with a variety of tasks as best as i can.")
    speak("24 hours a day 7 days a week.") 
    speak("Importing all preferences from root directory")
    speak("system is now fully operational")
           

def Creator():
    speak("Krypt-On created me")


def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        said = ""

        try:
            print("Recognizing...")
            said = r.recognize_google(audio)
            print(said)

        except Exception as e:
            #print("Exception: " + str(e))
            pass
    return said.lower()


if __name__ == "__main__":
    clear = lambda: os.system('cls')  
    banner()
    Introduction()
    #wishme()

wake = "jarvis"

while True:  
    print("Listening...")
    query = get_audio()

    if query.count(wake) > 0:
        #speak("yes")
        sound = "wakesound.wav"
        playsound.playsound(sound)
        query = get_audio()


        if "hello" in query: 
            speak("hello, how are you?")

        elif "what is your name" in query:     
            speak("My name is friday")

        #elif "make a note" or "take a note" or "create a reminder" in query:  
            #speak("what do you want me to remember?")
            #note_text = get_audio()
            #note(note_text)
            #speak("i've saved that to my memory.")

        elif ("read my reminder" in query or "remember" in query):
            reminder_file = open("reminder.txt", 'r')
            speak("You said me to remember that: " + reminder_file.read())

        elif 'how are you' in query:
            speak("I am fine, Thanks for asking")
            speak("How are you Sir?")
            if 'fine' in query or "good" in query: 
                speak("It's good to know that your fine")
            else:
                speak("I hope you get well soon.")

        elif ('wikipedia' in query or 'what' in query or 'who' in query or 'when' in query or 'where' in query):
            speak("Searching...")
            query = query.replace("wikipedia","")
            query = query.replace("search", "")
            query = query.replace("what", "")
            query = query.replace("when", "")
            query = query.replace("where", "")
            query = query.replace("who", "")
            query = query.replace("is", "")
            result = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(result)
            speak(result)

        elif ("system status" in query or "status report" in query or "cpu and battery" in query):
            systemstatus()

        elif ("tell me a joke" in query or "joke" in query):
            jokes()

        elif ("logout" in query):
            os.system("shutdown -1")
        
        elif ("restart" in query):
            os.system("shutdown /r /t 1")
        
        elif ("shut down" in query):
            os.system("shutdown /r /t 1")

        elif ("play songs" in query):
            speak("Playing song...")
            songs_dir = "E:\\BackUP\\audio"
            songs = os.listdir(songs_dir)
            os.startfile(os.path.join(songs_dir, songs[1]))
            quit()
        
        elif ("weather" in query or "temperature" in query):
            weather()
        
        elif ("change voice to male" in query or "change voice to female" in query):
            if ("female" in query):
                voice_change(1)
            elif ("male" in query):
                voice_change(0)

        elif ('i am done' in query or 'bye bye jarvis' in query or 'go offline' in query or 'bye' in query):
            speak("commencing shutdown protocol. going offline")
            wishme_end()

        elif ("tell me about yourself" in query or "who are you" in query):
            personal()
        
        elif ('time' in query):
            time()

        elif ('date' in query):
            date()

        elif 'open youtube' in query:
            speak("What should I search?")
            Search_term = get_audio()
            speak("Here we go to Youtube\n")
            wb.open("https://www.youtube.com/results?search_query=" + Search_term)
            time.sleep(5)

        elif 'search google' in query:
            speak("What should I search?")
            Search_term = get_audio()
            wb.open('https://www.google.com/search?q=' + Search_term)

        elif "who am i" in query:
            speak("If you can talk, then definitely you are a human")  

        elif 'what is love' and 'tell me about love' in query:
            speak("It is 7th sense that destroy all other senses , "
                  "And I think it is just a mere illusion , "
                  "It is waste of time") 
        elif 'empty recycle bin' in query:
                winshell.recycle_bin().empty(confirm = False, show_progress = False, sound = True)
                speak("Recycle Bin Recycled")

        elif "write a note" in query:
            speak("What should i write, sir")
            note = get_audio()
            file = open('note.txt', 'w')
            speak("Sir, Should i include date and time")
            dt = get_audio()
            if 'yes' in dt or 'sure' in dt:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                file.write(strTime)
                file.write(" :- ")
                file.write(note)
                speak('done')
            else:
                file.write(note)

        elif "show note" in query:
            speak("Showing Notes")
            file = open("note.txt", "r")
            print(file.read())
            speak(file.read())

        elif 'read news' in query:
                
            try:

                jsonObj = urlopen('''news api link''')
                data = json.load(jsonObj)
                i = 1
                
                speak('here are some top news from the times of india')
                print('''=============== TOP HEADLINES ============'''+ '\n')
                
                for item in data['articles']:
                    
                    print(str(i) + '. ' + item['title'] + '\n')
                    print(item['description'] + '\n')
                    speak(str(i) + '. ' + item['title'] + '\n')
                    i += 1
                    
            except Exception as e:
                print(str(e))

        elif "will you be my girlfriend" in query or "will you be my boyfriend" in query:
            speak("I'm not sure about, may be you should give me some time")

        elif "i love you" in query:
            speak("It's hard to understand, I am still trying to figure this out.")

        elif "calculate" in query:
                
            app_id = "wolfram alpha api"
            client = wolframalpha.Client(app_id)
            indx = query.lower().split().index('calculate')
            query = query.split()[indx + 1:]
            res = client.query(' '.join(query))
            answer = next(res.results).text
            print("The answer is " + answer)
            speak("The answer is " + answer)  


        elif "don't listen" in query or "stop listening" in query:
            speak("for how much seconds you want me to stop listening commands")
            a = int(get_audio())
            time.sleep(a)
            print(a)

        elif "What is my ip address?" in query:
            ip = urllib.get('https://api.ipify.org').text
            speak(f"your IP Address is {ip}")
        
        elif 'send a whatsapp message' in query:
            speak('Whom do you want to contact?')
            user = get_audio()

            speak("What do you want to say?")
            message = get_audio()

            speak("When to send?")
            s_time = get_audio()

            if 'later' in s_time:
                speak("Tell me about the hour?")
                hour__ = int(get_audio())

                speak("Tell me about the minutes?")
                minute__ = int(get_audio())

            elif 'now' in s_time:
                hour__ = datetime.datetime.now().hour
                if (datetime.datetime.now().second) < 30:
                    minute__ = (datetime.datetime.now().minute) + 1
                else:
                    minute__ = (datetime.datetime.now().minute) + 2

            speak("Sending Message.")
            kit.sendwhatmsg(contact[user]["phone"],message,hour__,minute__)

        



# importing required module
import pyttsx3
import datetime

# creating speak engine
engine = pyttsx3.init('sapi5')  # initializing 
voices = engine.getProperty('voices') # getting all voices found in windows
engine.setProperty('voice', voices[0].id) # sellecting voice and setting sellected voice

# creating speak function
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# creating wishMe function
def wishMe():
    hour = int(datetime.datetime.now().hour)  # getting time in hour formate
    
    if hour>=0 and hour<12:
        speak("Good Morning sir!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon sir!")

    else:
        speak("Good Evening sir!")
    speak("have a nice day")

# calling wishMe function
wishMe()







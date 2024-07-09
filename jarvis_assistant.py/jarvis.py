import speech_recognition as sr 
import webbrowser
import pyttsx3
import musicLibrary
import requests

recognizer = sr.Recognizer()
engine = pyttsx3.init()
newsapi = '37fd148c0e394eb7a90ec0c77abbbf22'

def speak(text):
    engine.say(text)
    engine.runAndWait()

def process(c):
    if 'open google' in c.lower():
        webbrowser.open('https://google.com')
    elif 'open youtube' in c.lower():
        webbrowser.open('https://youtube.com')
    elif c.lower().startswith('play'):
        song = c.lower().split(" ")[1]
        link =musicLibrary.music[song]
        webbrowser.open(link)
        

if __name__ == '__main__':
    speak("Initialising Jarvis....")
    #listen for the wake word 'Jarvis'
    # obtain audio from the microphone
    while True:
      r = sr.Recognizer()
      
    
      try:
           with sr.Microphone() as source:
              print("Listening....")
              audio = r.listen(source, timeout=3 , phrase_time_limit=2)
           print('Recognizing....')
           word = r.recognize_google(audio)
           command = r.recognize_google(audio)
           if(word.lower() == 'hey jarvis'):
               #Listen for command
               speak('Yes sir')
           
           
           else:
               process(command)    
            
      
      except Exception as e:
           print("Error; {0}".format(e))

'''write a code using  that will take user input from and search on google and store top 10 url in the list.


conditions : 
    i )   URL must be stored permanently as well
    ii)   user can give input using keyboard and  voice both'''

import pyttsx3
import webbrowser
import speech_recognition as sr
import datetime
import time

engine = pyttsx3.init('sapi5')



voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    print('Computer: ' + audio)
    engine.say(audio)
    engine.runAndWait()

def greetMe():
    currentH = int(datetime.datetime.now().hour)
    if currentH >= 0 and currentH < 12:
        speak('Good Morning! sir')

    if currentH >= 12 and currentH < 18:
        speak('Good Afternoon! sir')

    if currentH >= 18 and currentH !=0:
        speak('Good Evening! sir')

greetMe()


from googlesearch import search

speak(' plz speck topic your search topic')

url=[]


def myCommand():
   
    r = sr.Recognizer()                                                                                   
    with sr.Microphone() as source:                                                                       
        print("Listening...")
        r.pause_threshold =  1
        audio = r.listen(source)
    try:
        web = r.recognize_google(audio, language='en-in')
        print('User: ' + web + '\n')
        
    except sr.UnknownValueError:
        speak('Sorry sir! I didn\'t get that! Try typing the command!')
        web = str(input('Command: '))

    return web
        

if __name__ == '__main__':

    while True:
    
        web = myCommand();
        web = web.lower()
        
        for i in search(web,stop=10):
                print(i) # i will only print url
                time.sleep(1)
                url.append(i)
        
        print(url)
            
        

            
        

import speech_recognition as sr
import pyttsx3
import time
import intro

listener = sr.Recognizer()  # listener Object
engine = pyttsx3.init()
voices = engine.getProperty('voices')

engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 150)




try:
    with sr.Microphone() as source:  # if create a object
        print('Listening...')
        time.sleep(1)
        voice = listener.listen(source)
        command = listener.recognize_google(voice)
        command = command.lower()
        if 'multy ' in command:
            intro.intro()
            print(command)




except:
    pass


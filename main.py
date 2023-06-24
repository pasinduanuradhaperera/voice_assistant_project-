import speech_recognition as sr
import pyttsx3
import time

listener = sr.Recognizer()  # listener Object
engine = pyttsx3.init()
voices = engine.getProperty('voices')

engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 150)

engine.say('I am multy ')
engine.say('What can I do for you')
engine.runAndWait()


try:
    with sr.Microphone() as source:  # if create a object
        print('Listening...')
        time.sleep(1)
        voice = listener.listen(source)
        command = listener.recognize_google(voice)
        command = command.lower()
        if 'hey' in command:
            if 'multy ' in command:
                engine.say(command)
                engine.runAndWait()
                print(command)




except:
    pass


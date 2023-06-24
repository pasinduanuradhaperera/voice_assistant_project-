import speech_recognition as sr

import time

listener = sr.Recognizer() #listner Obect
try:
    with sr.Microphone() as source: #if create a object
        print('Listening...')
        time.sleep(1)
        voice = listener.listen(source)
        command = listener.recognize_google(voice)
        command = command.lower()
        if 'alexa' in command:
            print(command)
        print(command)

except:
    pass


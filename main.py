import speech_recognition as sr

import time

listener = sr.Recognizer()
try:
    with sr.Microphone() as source:
        print('Listening...')
        time.sleep(1)
        voice = listener.listen(source)
        command = listener.recognize_google(voice)
        print(command)

except:
    pass


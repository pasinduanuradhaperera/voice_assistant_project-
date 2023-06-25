import pyttsx3

engine = pyttsx3.init()
voices = engine.getProperty('voices')

engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 150)


def intro():
    engine.say('I am multy')
    engine.say('What can I do for you')
    engine.runAndWait()

import speech_recognition as sr

listener = sr.Recognizer()  # listener Object
speech = sr.Microphone(2)  # change microphone option


def listening():
    with speech as source:
        print('Listening...')  # indicator for listening
        command = listener.adjust_for_ambient_noise(source)
        voice = listener.listen(source, None, 2)
        print('audio is recorded')
        try:
            print("api is enabled")
            command = listener.recognize_google(voice, language='en-GB')
            command = command.lower()
            return command

        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))

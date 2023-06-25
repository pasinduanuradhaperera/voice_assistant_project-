import speech_recognition as sr
import voice_file as vo

listener = sr.Recognizer()  # listener Object
speech = sr.Microphone(2)  # change microphone option

while 1:
    with speech as source:
        print('Listening...')  # indicator for listening
        command = listener.adjust_for_ambient_noise(source)
        voice = listener.listen(source, None, 3)

        print('audio is recorded')
        try:
            print("api is enabled")
            command = listener.recognize_google(voice, language='en-US')
            # for testing purposes, we're just using the default API key
            # to use another API key, use r.recognize_google(audio)
            # instead of r.recognize_google(audio)

            command = command.lower()

            if 'multi' in command:
                vo.intro()  # call introduction
                print(command)
            elif 'exit' in command:
                break
            else:

                print('what',command)
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))

print('program ends')

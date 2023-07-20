import pyttsx3

def roboSpeak():
    if __name__ == '__main__':
        x = input("my name is JARVIS:")
        engine = pyttsx3.init()
        engine.say(x)
        engine.runAndWait()


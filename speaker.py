import pyttsx3

"""
    Requirements: 
    pip install pyttsx3 wikipedia
"""
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()

talk('I am in a relationship with wifi')
talk('Please say the command again.')
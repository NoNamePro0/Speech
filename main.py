import sys
import pyttsx3 

engine = pyttsx3.init() 

def welcome():
    print()
    print("Just enter some words. And this program will speech it.")
    print("Use 'exit' to exit.")
    print()

def read():
    text = input(">")

    if (text=="exit") or (text=="quit"):
        sys.exit(0)     

    speech(text)

    read()

def speech(text):
    engine.say(text)
    engine.runAndWait()

welcome()
read()

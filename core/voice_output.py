import pyttsx3
import threading

engine = pyttsx3.init()
engine.setProperty("rate", 160)

lock = threading.Lock()

def speak(text):
    print(f"Jarvis: {text}")
    with lock:
        engine.say(text)
        engine.runAndWait()

from core.voice_output import speak
from core.mood_manager import log_mood
from core.memory import load_memory

def daily_check():
    memory = load_memory()
    speak(f"Good {memory['part_of_day']}, {memory['user']}. How are you feeling today?")
    mood = input("Your mood today (happy, okay, tired, low): ").strip().lower()
    log_mood(mood)
    return mood
import json
from datetime import datetime

def log_mood():
    mood = input("Your mood today (happy, okay, tired, low): ").strip().lower()
    entry = {"date": str(datetime.now()), "mood": mood}

    with open("memory_data/mood_log.json", "r+") as f:
        data = json.load(f)
        data.append(entry)
        f.seek(0)
        json.dump(data, f, indent=2)

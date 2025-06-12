import json
from datetime import datetime

def log_mood(current_mood):
    entry = {"date": str(datetime.now()), "mood": current_mood}

    with open("memory_data/mood_log.json", "r+") as f:
        data = json.load(f)
        data.append(entry)
        f.seek(0)
        json.dump(data, f, indent=2)

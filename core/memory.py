import json

def load_memory():
    with open("memory_data/memory.json") as f:
        return json.load(f)

def save_memory(data):
    with open("memory_data/memory.json", "w") as f:
        json.dump(data, f, indent=2)

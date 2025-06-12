from core.memory import load_memory

def suggest_tasks():
    memory = load_memory()
    recent = memory.get("recent_task", "resume update")
    return f"You’ve been working on {recent}. Want to continue or switch to your UPI Analyzer?"

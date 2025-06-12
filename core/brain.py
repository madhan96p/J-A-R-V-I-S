from core.heart import heart_responses
from core.suggestor import suggest_tasks
from core.memory import load_memory

def respond(query):
    if "how am i doing" in query:
        return suggest_tasks()

    if "love" in query or "feel sad" in query:
        return heart_responses(query)

    if "resume" in query:
        return "You last updated your resume 3 weeks ago. Want to add your GUVI certificate?"

    return "I'm listening... Tell me what you need."

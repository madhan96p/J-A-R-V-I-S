from core.voice_input import listen
from core.voice_output import speak
from transformers import pipeline
import time

# 🧠 Load the model (you can replace this with a better model if needed)
jarvis_thinker = pipeline("text2text-generation", model="declare-lab/flan-alpaca-large")

# 🎯 Dynamic + mood-aware response
def respond_to_query(query, mood):
    style = {
        "happy": "in a cheerful and fun tone",
        "okay": "in a neutral and helpful tone",
        "tired": "in a gentle and supportive tone",
        "low": "like a caring friend who's really listening"
    }.get(mood, "like a smart and friendly assistant")

    prompt = f"""You are Jarvis, Pragadeesh's AI assistant.
Pragadeesh said: "{query}"
Reply {style}, and make your answer sound natural and human."""
    
    result = jarvis_thinker(prompt, max_length=100, do_sample=True, temperature=0.95)[0]['generated_text']
    return result.strip()

# 🎬 Start Jarvis
def start_jarvis():
    speak("System boot complete. Ready when you are, Pragadeesh.")
    speak("Good morning, Pragadeesh. How are you feeling today?")
    mood = input("Your mood today (happy, okay, tired, low): ").lower()

    while True:
        try:
            query = listen()
            if query:
                print(f"You said: {query}")
                print("🤖 Jarvis is thinking...")
                time.sleep(1.1)

                response = respond_to_query(query, mood)
                print(f"Jarvis: {response}")
                speak(response)

                if any(exit_word in query.lower() for exit_word in ["stop", "bye", "exit", "shutdown"]):
                    speak("Shutting down Jarvis. See you soon!")
                    break
        except KeyboardInterrupt:
            speak("Shutting down Jarvis. See you soon!")
            break

start_jarvis()

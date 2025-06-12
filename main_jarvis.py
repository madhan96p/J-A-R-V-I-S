from core.voice_input import listen
from core.voice_output import speak
from core.brain import respond as get_jarvis_response # Renamed import for clarity
from core.day_checkin import daily_check
import time

# 🎬 Start Jarvis
def start_jarvis():
    speak("System boot complete. Ready when you are, Pragadeesh.")
    
    # Perform daily check-in and get mood
    # daily_check() handles the greeting and mood input/logging
    mood = daily_check() 

    while True:
        try:
            query = listen()
            if query:
                print(f"You said: {query}")
                print("🤖 Jarvis is thinking...")
                time.sleep(1.1)

                response = get_jarvis_response(query, mood)
                print(f"Jarvis: {response}")
                speak(response)

                if any(exit_word in query.lower() for exit_word in ["stop", "bye", "exit", "shutdown"]):
                    speak("Shutting down Jarvis. See you soon!")
                    break
        except KeyboardInterrupt:
            speak("Shutting down Jarvis. See you soon!")
            break

start_jarvis()

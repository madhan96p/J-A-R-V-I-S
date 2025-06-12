import speech_recognition as sr

def listen():
    recognizer = sr.Recognizer()
    mic = sr.Microphone(device_index=0)  # Use working index

    with mic as source:
        print("🎧 Listening...")
        recognizer.adjust_for_ambient_noise(source)
        try:
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=7)
            query = recognizer.recognize_google(audio)
            return query
        except sr.WaitTimeoutError:
            print("⏳ Timeout: Didn't hear anything.")
        except sr.UnknownValueError:
            print("❌ Sorry, couldn't understand that.")
        except sr.RequestError as e:
            print(f"⚠️ API error: {e}")
    return None

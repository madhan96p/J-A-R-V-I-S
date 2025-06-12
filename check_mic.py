# check_mic.py
import pyaudio
import wave

# === Settings ===
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
CHUNK = 1024
RECORD_SECONDS = 5
OUTPUT_FILENAME = "mic_test.wav"

# === Step 1: List available input devices ===
audio = pyaudio.PyAudio()
print("\n🎤 Available Microphone Devices:\n")
input_devices = []
for i in range(audio.get_device_count()):
    info = audio.get_device_info_by_index(i)
    if info["maxInputChannels"] > 0:
        input_devices.append((i, info["name"]))
        print(f"{i}: {info['name']} ({info['maxInputChannels']} channels)")

# === Step 2: Ask user to choose a device ===
if not input_devices:
    print("❌ No input devices found. Exiting.")
    exit()

device_index = int(input("\n🔢 Enter the device index to test recording: "))

# === Step 3: Record audio ===
try:
    stream = audio.open(format=FORMAT, channels=CHANNELS,
                        rate=RATE, input=True,
                        input_device_index=device_index,
                        frames_per_buffer=CHUNK)
    print("🎙️ Recording for 5 seconds...")
    frames = []

    for _ in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)

    print("✅ Recording done.")

    # Stop & close
    stream.stop_stream()
    stream.close()
    audio.terminate()

    # Save to file
    wf = wave.open(OUTPUT_FILENAME, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(audio.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()

    print(f"📁 Audio saved as: {OUTPUT_FILENAME}")

except Exception as e:
    print(f"❌ Error during recording: {e}")
    audio.terminate()

# 🤖 J.A.R.V.I.S — Just A Rather Very Intelligent System

> Your personal AI assistant, powered by LLMs, voice recognition, and mood-aware responses.  
> Built entirely in Python, independently — open for collaboration.

---

## 🧠 What is J.A.R.V.I.S?

**J.A.R.V.I.S** is a smart, voice-activated assistant that:
- Listens to your voice
- Understands your **mood**
- Responds using **LLMs (Large Language Models)** in a natural, helpful, human-like tone
- Built modularly — designed to grow into a full AI productivity buddy

Imagine something between **Siri, Alexa**, and **Tony Stark’s JARVIS** — but built from scratch in Python and open-source.

---

## 🎯 Features

✅ Voice input using SpeechRecognition  
✅ Text-to-Speech voice output (pyttsx3)  
✅ LLM-powered dynamic replies (via Hugging Face `flan-alpaca-large`)  
✅ Mood-aware tone selection (happy, okay, tired, low)  
✅ Modular code (easy to extend)  
✅ Runs offline (no OpenAI API keys needed!)

---

## 🛠️ Tech Stack

| Component        | Library / Tool                           |
|------------------|------------------------------------------|
| Voice Input      | `speech_recognition`                     |
| Voice Output     | `pyttsx3` or `gTTS`                      |
| LLM Response     | `transformers` + `flan-alpaca-large`     |
| Mood Manager     | Custom module                            |
| Assistant Logic  | Python + Prompt Engineering              |
| CLI Interface    | `main_jarvis.py`                         |

---

## 🚀 Getting Started

### 1. Clone the repo:
```bash
git clone https://github.com/madhan96p/J-A-R-V-I-S.git
cd J-A-R-V-I-S
````

### 2. Set up environment:

```bash
python -m venv venv
venv\Scripts\activate      # on Windows
# OR
source venv/bin/activate   # on Linux/Mac
```

### 3. Install dependencies:

```bash
pip install -r requirements.txt
```

### 4. Run Jarvis:

```bash
python main_jarvis.py
```

---

## 🧩 Project Structure

```
📁 J-A-R-V-I-S/
├── .venv/                  # Local Python virtual environment
│   ├── Include/
│   ├── Lib/
│   ├── Scripts/
│   ├── .gitignore
│   └── pyvenv.cfg
│
├── venv/                   # Optional duplicate venv (can remove one later)
│   ├── Include/
│   ├── Lib/
│   ├── Scripts/
│   ├── share/
│   ├── .gitignore
│   └── pyvenv.cfg
│
├── assets/                 # Assets (images, audio, etc.)
│
├── core/                   # Core logic modules
│   ├── __pycache__/
│   ├── brain.py            # Decision-making center
│   ├── day_checkin.py      # Daily check-in logic
│   ├── heart.py            # Emotion and empathy engine
│   ├── llm_response.py     # LLM prompt handling
│   ├── memory.py           # Handles memory saving/loading
│   ├── mood_manager.py     # Mood detection and setting
│   ├── suggestor.py        # Suggests tasks or thoughts
│   ├── voice_input.py      # Listens to your voice
│   └── voice_output.py     # Speaks out responses
│
├── memory_data/            # Persistent user memory
│   ├── memory.json
│   ├── mood_log.json
│   └── resume_log.json
│
├── check_mic.py            # Microphone checker utility
├── config.py               # Configs and constants
├── main_jarvis.py          # Main entry point to launch Jarvis
├── requirements.txt        # Python dependencies
└── README.md               # Project overview

```

---

## 🌟 Contributing

I started this independently — but I’d love to see how **you** would improve it!

You can:

* 🧠 Add new features (e.g. calendar, weather, UPI summary)
* 🎤 Improve voice accuracy
* 💬 Connect it to APIs (ChatGPT, browser, mail)
* 🧪 Convert it to a web or GUI app (Gradio/Streamlit)

```bash
# Fork the repo
# Make your changes
# Submit a PR 🚀
```

Let’s make **our own JARVIS** — one commit at a time.

---

## 🪄 Roadmap

* [X] Voice Input & Output
* [x] LLM-powered replies
* [x] Mood-based tone detection
* [ ] Task scheduling (to-do assistant)
* [ ] Chrome automation (open websites, search)
* [ ] Integration with Streamlit or Gradio
* [ ] Personalized memory (local JSON DB)

---

## 📜 License

MIT License — free to use, modify, and share.

---

## 🙌 Acknowledgements

Thanks to:

* Hugging Face 🤗 for open LLMs
* The Python open-source community
* Everyone dreaming about their own J.A.R.V.I.S

---

## 🔗 Connect

💻 Portfolio: [pragadeeshfolio.netlify.app](https://pragadeeshfolio.netlify.app)
🐍 GitHub: [@madhan96p](https://github.com/madhan96p)
📬 DM on LinkedIn if you’re curious to collaborate!

---

**Built solo. Made for many.**
Let’s bring JARVIS to life. One line of code at a time.

```


# 🗣️ Voice Cloning Web App with YourTTS

This is a lightweight and modern web application that performs **voice cloning** using [Coqui's YourTTS](https://github.com/coqui-ai/TTS). It allows users to upload a short audio reference and synthesize speech that mimics the voice in multiple languages.

---

## 🚀 Features

- 🎧 Upload a reference `.wav` audio file (5–15 seconds)
- 📝 Enter text to be spoken
- 🌍 Supports **15+ languages**
- 🗣️ Synthesizes the input text using the reference voice
- 🔊 Listen to generated voice directly in browser
- 💾 Download the cloned voice output
- 🌙 Dark mode UI with a professional and aesthetic design

---

## 🛠️ Tech Stack

- **Backend**: Python, Flask
- **Frontend**: HTML, CSS
- **TTS Engine**: [`your_tts`](https://github.com/coqui-ai/TTS)
- **Model Used**: `tts_models/multilingual/multi-dataset/your_tts`

---
## File architecture

voice-cloning-webapp/
│
├── app.py                 # Flask app logic
├── recordings/            # Stores uploaded reference audio files
├── templates/
│   └── index.html         # Web interface
└── output.wav             # Most recent cloned audio file





# Iris AI Assistant 🤖🎙️

Iris is a local voice-enabled AI assistant built using Python and Flask.  
It can listen to voice commands, respond using artificial intelligence, open websites, play music, read news, and interact with users through speech.

---

## 🚀 Features
- Voice activation using wake word **“Iris”**
- Speech-to-text using Google Speech Recognition
- Text-to-speech responses
- Opens websites like Google, YouTube, LinkedIn, Instagram, Facebook
- Plays music using a custom music library
- Reads live news headlines
- Uses a **local LLM model (offline AI responses)**
- Flask-based web interface with start/stop control

---

## 🛠️ Tech Stack
- Python
- Flask
- SpeechRecognition
- gTTS + Pygame
- ctransformers (Local LLM)
- HTML, CSS, JavaScript

---

## ▶️ Demo Video
🎥 **Demo:**  
(https://drive.google.com/file/d/1hrlXrWwAWiwqNaYtoFLzRSIZXv7DFdRB/view?usp=sharing)



---

## ⚠️ Model File Notice
The AI model file (`tinyllama.gguf`) is **intentionally excluded** from this repository due to GitHub file size limits.

To run the project locally:
1. Download a compatible `.gguf` model (e.g., TinyLlama)
2. Place it inside the `models/` folder


---

## 📦 How to Run Locally

```bash
pip install -r requirements.txt
python app.py

Open Browser
http://127.0.0.1:5000


Click Start and say:
Iris

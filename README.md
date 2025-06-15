# 🌐 Multilingual AI Chat Translator

A real-time multilingual chat translator built with Flask, Socket.IO, and the Groq LLaMA 3 (via OpenAI-compatible API). This web app translates user-input messages into any selected Indian or international language and uses speech synthesis to read them aloud.

## 🚀 Features

- 🌍 Translate text messages into 20+ languages.
- 🔄 Real-time translation using WebSockets (Socket.IO).
- 🗣️ Text-to-speech (TTS) playback for translated messages.
- 🧠 Powered by Groq's LLaMA 3 API (OpenAI-compatible).
- 🧪 Flask-Login for session handling (guest auto-login).
- 🖼️ Minimal, responsive UI with live translation history.

---

## 🧩 Tech Stack

| Layer        | Technology                          |
|--------------|--------------------------------------|
| Backend      | Flask, Flask-SocketIO, Flask-Login   |
| Frontend     | HTML, CSS, JavaScript                |
| API          | Groq LLaMA 3 (OpenAI-compatible API) |
| Speech       | Web Speech API (SpeechSynthesis)     |
| Deployment   | Localhost (Flask) or cloud-ready     |

---

## 📦 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/shivamgupta79/Multilingual-AI-Chat-Translator.git
cd Multilingual-AI-Chat-Translator
2. Create & Activate Virtual Environment (Optional but Recommended)

venv\Scripts\activate     # Windows
3. Install Requirements
pip install -r requirements.txt

4. Set up .env file
Create a .env file in the root folder with your Groq API key:


GROQ_API_KEY=your_groq_api_key_here
SECRET_KEY=any_random_secret

5. Run the App
python app.py


🌐 Supported Languages
Hindi, Bengali, Telugu, Marathi, Tamil, Gujarati, Kannada, Odia, Punjabi, Malayalam, Urdu, Assamese, Maithili, Sanskrit, Konkani, Manipuri, Dogri, Bodo, Santhali, Kashmiri, Spanish, French

🧠 How It Works (Flow)
User Inputs Message + Selects Target Language

SocketIO sends {message, target_lang} to Flask server.

Flask uses Groq LLaMA 3 API to translate the text via prompt:
"Translate this message to {target_lang}: {message}"

Translated message is sent back to browser via WebSocket.

Frontend updates UI with translation + reads out using SpeechSynthesis.

🗂️ Project Structure
bash
Copy
Edit
📁 Multilingual-AI-Chat-Translator/
│
├── app.py                 # Main Flask app
├── requirements.txt       # Python dependencies
├── .env                   # Environment variables
│
├── templates/
│   └── index.html         # Main frontend HTML
│
└── static/
    └── (Optional: for custom JS/CSS if needed)
🎤 Voice Output
The Speak button uses your browser’s speechSynthesis API to speak translated text aloud in the correct accent (langCode is selected based on language dropdown).

💡 Future Improvements
🌐 Add WebRTC voice input (speech-to-text).

🧾 Store user chat logs in MongoDB or SQLite.

👥 Add user registration & group chat.

🎧 Add downloadable MP3 for voice translations.

📱 Convert into mobile-friendly PWA.

📄 License
This project is open-source and available under the MIT License.


## 🧭 Flowchart (Visual Logic)

Here's a text-based **flowchart** of the system logic:

User opens app
│
▼
Selects language + types message
│
▼
Press "Translate" → Sends to backend via WebSocket
│
▼
Flask receives → Forms translation prompt
│
▼
Groq LLaMA 3 API processes and returns translation
│
▼
Flask emits translated message back via WebSocket
│
▼
Frontend updates UI:
├─ Shows translated message
├─ Adds to translation history
└─ Triggers SpeechSynthesis to speak aloud
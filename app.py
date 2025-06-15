from flask import Flask, render_template, request
from flask_socketio import SocketIO, emit
from openai import OpenAI
from dotenv import load_dotenv
import os


load_dotenv()


groq_api_key = os.getenv("GROQ_API_KEY")
if not groq_api_key:
    raise ValueError("GROQ_API_KEY is missing from .env file")


client = OpenAI(
    api_key=groq_api_key,
    base_url="https://api.groq.com/openai/v1"
)


app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY", "supersecret")


socketio = SocketIO(app, cors_allowed_origins="*")


@app.route("/")
def index():
    return render_template("index.html", username="Anonymous")


@socketio.on("chat_message")
def handle_chat_message(data):
    user_msg = data.get("message")
    target_lang = data.get("target_lang")

    if not user_msg or not target_lang:
        emit("translated_message", {"error": "Missing message or target language"})
        return

    prompt = f"Translate this message to {target_lang}: {user_msg}"
    try:
        response = client.chat.completions.create(
            model="llama3-70b-8192",
            messages=[{"role": "user", "content": prompt}]
        )
        translated = response.choices[0].message.content.strip()
        emit("translated_message", {
            "sender": "Anonymous",
            "original": user_msg,
            "translated": translated,
            "language": target_lang
        })
    except Exception as e:
        emit("translated_message", {"error": f"Groq API Error: {str(e)}"})

# Run app
if __name__ == "__main__":
    socketio.run(app, debug=True, port=5000)

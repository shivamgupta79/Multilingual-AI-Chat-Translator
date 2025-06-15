from flask import Flask, render_template, request, redirect, url_for, session
from flask_socketio import SocketIO, emit
from flask_login import LoginManager, UserMixin, login_user, logout_user, current_user
from openai import OpenAI
from dotenv import load_dotenv
import os

# Load .env variables
load_dotenv()

# Get Groq API key
groq_api_key = os.getenv("GROQ_API_KEY")
if not groq_api_key:
    raise ValueError("GROQ_API_KEY is missing from .env file")

# Setup OpenAI client (Groq compatible)
client = OpenAI(
    api_key=groq_api_key,
    base_url="https://api.groq.com/openai/v1"
)

# Flask setup
app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY", "supersecret")

# Login manager
login_manager = LoginManager()
login_manager.init_app(app)

# Dummy user store
users = {}

# SocketIO setup
socketio = SocketIO(app, cors_allowed_origins="*")

# User class
class User(UserMixin):
    def __init__(self, id, username):
        self.id = id
        self.username = username

    def get_id(self):
        return self.id

# Auto-login Guest user for demo (no login page needed)
@app.before_request
def auto_login_guest():
    if not current_user.is_authenticated:
        guest_id = "0"
        if guest_id not in users:
            users[guest_id] = User(guest_id, "Guest")
        login_user(users[guest_id])

@login_manager.user_loader
def load_user(user_id):
    return users.get(user_id)

# Home page
@app.route("/")
def index():
    return render_template("index.html", username=current_user.username)

# SocketIO Chat Translation Handler
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
            "sender": current_user.username,
            "original": user_msg,
            "translated": translated,
            "language": target_lang
        })
    except Exception as e:
        emit("translated_message", {"error": f"Groq API Error: {str(e)}"})

# Run app
if __name__ == "__main__":
    socketio.run(app, debug=True, port=5000)

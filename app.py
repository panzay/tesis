import os
import uuid
import logging
from logging.handlers import RotatingFileHandler
from datetime import datetime
from threading import Lock

from dotenv import load_dotenv
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_socketio import SocketIO, emit

import azure.cognitiveservices.speech as speechsdk

# -----------------------------------------------------------------------------
# App & Config
# -----------------------------------------------------------------------------
app = Flask(__name__)
app.config.from_object('config.Config')

# -----------------------------------------------------------------------------
# Extensions
# -----------------------------------------------------------------------------
db  = SQLAlchemy(app)
sio = SocketIO(app, async_mode='threading')

# -----------------------------------------------------------------------------
# Model defined *after* db is initialized
# -----------------------------------------------------------------------------
class Transcript(db.Model):
    __tablename__ = 'transcript'

    id         = db.Column(db.Integer, primary_key=True)
    session_id = db.Column(db.String(36), nullable=False, index=True)
    text       = db.Column(db.Text, nullable=False)
    timestamp  = db.Column(
        db.DateTime,
        default=datetime.utcnow,
        index=True
    )

# -----------------------------------------------------------------------------
# Logging
# -----------------------------------------------------------------------------
handler = RotatingFileHandler(app.config['LOG_FILE'], maxBytes=10*1024*1024, backupCount=5)
handler.setLevel(logging.INFO)
handler.setFormatter(logging.Formatter('[%(asctime)s] %(levelname)s in %(module)s: %(message)s'))
app.logger.addHandler(handler)

# -----------------------------------------------------------------------------
# Load .env & Azure creds
# -----------------------------------------------------------------------------
load_dotenv()
SUBSCRIPTION_KEY = os.getenv('SPEECH_KEY')
SERVICE_REGION   = os.getenv('SPEECH_REGION')
SERVICE_LANGUAGE = "id-ID"

# -----------------------------------------------------------------------------
# Ensure DB & tables exist
# -----------------------------------------------------------------------------
def ensure_database():
    uri = app.config['SQLALCHEMY_DATABASE_URI']
    if uri.startswith("sqlite:///"):
        db_path = uri.replace("sqlite:///", "", 1)
        if not os.path.exists(db_path):
            app.logger.info(f"DB not found at {db_path}, creating…")
        else:
            app.logger.info(f"DB found at {db_path}, skipping creation")
        db.create_all()

# -----------------------------------------------------------------------------
# Speech → DB → SocketIO
# -----------------------------------------------------------------------------
thread      = None
thread_lock = Lock()

def speech_recognition_with_microphone():
    speech_config = speechsdk.SpeechConfig(subscription=SUBSCRIPTION_KEY, region=SERVICE_REGION)
    speech_config.speech_recognition_language = SERVICE_LANGUAGE
    audio_config  = speechsdk.audio.AudioConfig(use_default_microphone=True)
    recognizer    = speechsdk.SpeechRecognizer(speech_config=speech_config, audio_config=audio_config)

    result = recognizer.recognize_once()
    if result.reason == speechsdk.ResultReason.RecognizedSpeech:
        text = result.text.strip()
        print(f"[{CURRENT_SESSION_ID}] Recognized: {text}")
        app.logger.info(f"[{CURRENT_SESSION_ID}] Recognized: {text}")

        # Save to db
        with app.app_context():
            rec = Transcript(
                session_id=CURRENT_SESSION_ID,
                text=text
            )
            db.session.add(rec)
            db.session.commit()

        sio.emit('my_response', {'data': text})

    elif result.reason == speechsdk.ResultReason.NoMatch:
        print(f"[{CURRENT_SESSION_ID}] No speech recognized")
        app.logger.warning("No speech recognized")
    else:
        details = result.cancellation_details
        msg = f"Canceled: {details.reason}"
        if details.reason == speechsdk.CancellationReason.Error:
            msg += f" ({details.error_details})"
        app.logger.error(msg)

def background_task():
    sio.sleep(5)
    while True:
        sio.sleep(0.2)
        speech_recognition_with_microphone()

@sio.on('connect')
def connect():
    global thread
    with thread_lock:
        if thread is None:
            thread = sio.start_background_task(background_task)
    emit('my_response', {'data': 'connected'})

@app.route('/')
def index():
    return render_template('index.html')


# one unique ID per “meeting session”
CURRENT_SESSION_ID = str(uuid.uuid4())
print("Starting new session:", CURRENT_SESSION_ID)

# -----------------------------------------------------------------------------
# Start the app
# -----------------------------------------------------------------------------
if __name__ == '__main__':
    with app.app_context():
        ensure_database()

    sio.run(app, host='0.0.0.0', port=5000)

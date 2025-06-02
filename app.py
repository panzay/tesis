import os
import threading
import azure.cognitiveservices.speech as speechsdk

from dotenv import load_dotenv
from flask import Flask, render_template
from flask_socketio import SocketIO, emit
from flask_cors import CORS

# import eventlet
# eventlet.monkey_patch()

# Load environment variables from .env file
load_dotenv()

SUBSCRIPTION_KEY = os.environ.get('SPEECH_KEY')
SERVICE_REGION = os.environ.get('SPEECH_REGION')
SERVICE_LANGUAGE = "id-ID"

# Flask Service
async_mode = None
app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
CORS(app, resources={r"/*": {"origins": "*"}})
socketio = SocketIO(app, async_mode='threading', cors_allowed_origins="*")
# socketio = SocketIO(app, cors_allowed_origins="*")

def continuous_speech_recognition_with_intermediate_results():
    speech_config = speechsdk.SpeechConfig(subscription=SUBSCRIPTION_KEY, region=SERVICE_REGION)
    speech_config.speech_recognition_language = SERVICE_LANGUAGE
    audio_config = speechsdk.audio.AudioConfig(use_default_microphone=True)
    speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config, audio_config=audio_config)

    def recognized_cb(evt):
        print('RECOGNIZED: {}'.format(evt.result.text))
        socketio.emit('recognized', {'text': evt.result.text}, broadcast=True)

    def recognizing_cb(evt):
        print('RECOGNIZING: {}'.format(evt.result.text))
        socketio.emit('recognizing', {'text': evt.result.text}, broadcast=True)

    speech_recognizer.recognized.connect(recognized_cb)
    speech_recognizer.recognizing.connect(recognizing_cb)

    print("Say something...")

    speech_recognizer.start_continuous_recognition()
    input("Press Enter to stop...\n")
    speech_recognizer.stop_continuous_recognition()

@app.route('/')
def index():
    return render_template('index.html')

def start_flask():
    socketio.run(app, debug=True, host='0.0.0.0', port=5000)

if __name__ == "__main__":
    # threading.Thread(target=continuous_speech_recognition_with_intermediate_results).start()
    # start_flask()

    socketio.start_background_task(continuous_speech_recognition_with_intermediate_results)
    socketio.run(app, host="0.0.0.0", port=5000, debug=True)

import pyaudio
import numpy as np
import time
from math import log10
import audioop
from threading import Lock
from flask import Flask, render_template
from flask_socketio import SocketIO, emit
import os
import azure.cognitiveservices.speech as speechsdk
from dotenv import load_dotenv

# Flask and SocketIO setup
app = Flask(__name__)
app.secret_key = 'your secret here'
sio = SocketIO(app)

thread = None
thread_lock = Lock()

# Load environment variables from .env file
load_dotenv()

# Azure Speech SDK setup
subscription_key = os.environ.get('SPEECH_KEY')
service_region = os.environ.get('SPEECH_REGION')
SERVICE_LANGUAGE = "id-ID"

# Audio setup
p = pyaudio.PyAudio()
WIDTH = 2
RATE = int(p.get_default_input_device_info()['defaultSampleRate'])
DEVICE = p.get_default_input_device_info()['index']
rms = 1

def calculate_rms(data):
    """Calculate the Root Mean Square (RMS) of the audio data."""
    data = data.astype(np.float32)
    data = data[~np.isnan(data)]
    if data.size == 0:
        return 0.0
    rms = np.sqrt(np.mean(np.square(data), axis=0))
    return rms

def rms_to_db(rms):
    """Convert RMS to dB."""
    epsilon = 1e-10
    db = 20 * np.log10(rms + epsilon)
    return db

def speech_recognition_with_microphone():
    """Perform speech recognition using Azure Cognitive Services."""
    speech_config = speechsdk.SpeechConfig(subscription=subscription_key, region=service_region)
    speech_config.speech_recognition_language = SERVICE_LANGUAGE
    audio_config = speechsdk.audio.AudioConfig(use_default_microphone=True)
    speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config, audio_config=audio_config)

    print("Say something...")
    result = speech_recognizer.recognize_once()

    if result.reason == speechsdk.ResultReason.RecognizedSpeech:
        print("Recognized: {}".format(result.text))
        sio.emit('my_response', {'text': result.text})
    elif result.reason == speechsdk.ResultReason.NoMatch:
        print("No speech could be recognized")
    elif result.reason == speechsdk.ResultReason.Canceled:
        cancellation_details = result.cancellation_details
        print("Speech Recognition canceled: {}".format(cancellation_details.reason))
        if cancellation_details.reason == speechsdk.CancellationReason.Error:
            print("Error details: {}".format(cancellation_details.error_details))

def callback(in_data, frame_count, time_info, status):
    global rms
    rms = audioop.rms(in_data, WIDTH) / 32767
    return in_data, pyaudio.paContinue

def background_task():
    """Background task to handle both dB meter and speech recognition."""
    stream = p.open(format=p.get_format_from_width(WIDTH),
                    input_device_index=DEVICE,
                    channels=1,
                    rate=RATE,
                    input=True,
                    output=False,
                    stream_callback=callback)
    stream.start_stream()

    while stream.is_active():
        db = 20 * log10(rms)
        if db >= -40:
            # sio.emit('my_response', {'db': db})
            sio.emit('my_response', {'text': f"DB: {db:.1f} dB"})
            print(f"DB: {db}")
            speech_recognition_with_microphone()
        time.sleep(0.3)

    stream.stop_stream()
    stream.close()
    p.terminate()

@app.route('/')
def index():
    return render_template('index.html')

@sio.on('connect')
def connect():
    global thread
    with thread_lock:
        if thread is None:
            thread = sio.start_background_task(background_task)
    emit('my_response', {'text': 'connected'})

if __name__ == '__main__':
    sio.run(app)

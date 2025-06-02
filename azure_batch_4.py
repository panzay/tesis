import azure.cognitiveservices.speech as speechsdk
import os

# Configuration
subscription_key = os.environ.get('SPEECH_KEY_2')
region = os.environ.get('SPEECH_REGION')
SERVICE_LANGUAGE = "id-ID"

# # Path to the local audio file
# audio_file_path = "data_log/audacity/new/built-in/60_20.wav"


# def transcribe_local_audio_file():
#     # Set up the speech configuration
#     speech_config = speechsdk.SpeechConfig(subscription=subscription_key, region=region)

#     # Set up the audio configuration (reading from the local file)
#     audio_config = speechsdk.audio.AudioConfig(filename=audio_file_path)

#     # Create a speech recognizer with the given settings
#     speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config, audio_config=audio_config)

#     # Event handler for recognized speech
#     def recognized_handler(sender, event_args):
#         print(f"Recognized: {event_args.result.text}")

#     # Event handler for session started
#     def session_started_handler(sender, event_args):
#         print("Session started.")

#     # Event handler for session stopped (completed or canceled)
#     def session_stopped_handler(sender, event_args):
#         print("Session stopped.")
#         if event_args.reason == speechsdk.ResultReason.Canceled:
#             print("Recognition canceled: " + event_args.result.cancellation_details.error_details)

#     # Attach event handlers
#     speech_recognizer.recognized.connect(recognized_handler)
#     speech_recognizer.session_started.connect(session_started_handler)
#     speech_recognizer.session_stopped.connect(session_stopped_handler)

#     # Start continuous recognition
#     print("Transcribing audio file...")
#     speech_recognizer.start_continuous_recognition()

#     # Wait for recognition to finish
#     print("Press Ctrl+C to stop the transcription.")
#     try:
#         while True:
#             pass
#     except KeyboardInterrupt:
#         # Stop recognition when done
#         speech_recognizer.stop_continuous_recognition()

# if __name__ == "__main__":
#     transcribe_local_audio_file()

####################################


import requests
import time
import json

LEVEL = "100"
AUDIO_FORMAT = "wav"
AUDIO_FILE_NAME = f"60_{LEVEL}.{AUDIO_FORMAT}"
# AUDIO_FILE_NAME = "abcde.wav"

# Configuration
SUBSCRIPTION_KEY = subscription_key
SERVICE_REGION = region
STORAGE_ACCOUNT = "panzaystorage"
CONTANER_NAME = "tws"
SAS_TOKEN = "sp=rl&st=2025-01-19T08:35:51Z&se=2025-01-21T16:35:51Z&sv=2022-11-02&sr=c&sig=iqOPMI7RjypTkcaDXQRV%2F1bLJD0IxXZpcH59FVxZt9U%3D"


TRANSCRIPTION_API_URL = f"https://{SERVICE_REGION}.api.cognitive.microsoft.com/speechtotext/v3.2/transcriptions"
AUDIO_FILE_URI = f"https://{STORAGE_ACCOUNT}.blob.core.windows.net/{CONTANER_NAME}/{AUDIO_FILE_NAME}?{SAS_TOKEN}"

DISPLAY_NAME = "panzays"
DESCRIPTION = "Azure Speech Service"
LOCALE = SERVICE_LANGUAGE

def create_transcription():
    headers = {
        "Ocp-Apim-Subscription-Key": SUBSCRIPTION_KEY,
        "Content-Type": "application/json"
    }
    body = {
        "displayName": DISPLAY_NAME,
        "description": DESCRIPTION,
        "locale": LOCALE,
        "contentUrls": [AUDIO_FILE_URI],
        "properties": {}
    }
    response = requests.post(TRANSCRIPTION_API_URL, headers=headers, json=body)
    response.raise_for_status()
    return response.json()["self"]

def get_transcription_status(transcription_id):
    headers = {
        "Ocp-Apim-Subscription-Key": SUBSCRIPTION_KEY
    }
    response = requests.get(f"{TRANSCRIPTION_API_URL}/{transcription_id}", headers=headers)
    print('Response Status Code:', response.status_code)
    # print('Response Content:', response.content)
    response.raise_for_status()
    return response.json()

def get_transcription_results(transcription_id):
    headers = {
        "Ocp-Apim-Subscription-Key": SUBSCRIPTION_KEY
    }
    response = requests.get(f"{TRANSCRIPTION_API_URL}/{transcription_id}/files", headers=headers)
    response.raise_for_status()
    files = response.json()["values"]
    
    for file in files:
        if file["name"].endswith(".json"):
            content_url = file["links"]["contentUrl"]
            result_response = requests.get(content_url)
            result_response.raise_for_status()
            return result_response.json()

def main():
    iterations = 1000  # Number of times to transcribe the file
    success_count = 0
    fail_count = 0

    SOURCE = "data_log/audacity/new"
    MIC_TYPE = CONTANER_NAME

    for i in range(iterations):
        print(f"Starting transcription iteration {i + 1}/{iterations}...")
        try:
            # Step 1: Create a new transcription
            print("Creating new transcription...")
            transcription_url = create_transcription()
            transcription_id = transcription_url.split("/")[-1]

            # Step 2: Poll for transcription status
            print("Polling for transcription status...")
            status = "Running"
            while status not in ["Succeeded", "Failed"]:
                time.sleep(5)  # Wait for 5 seconds before polling again
                status_response = get_transcription_status(transcription_id)
                status = status_response["status"]
                print(f"Iteration {i + 1}: Status: {status}")

            if status == "Succeeded":
                print("Retrieving transcription results...")

                # Step 3: Retrieve and view transcription results
                results = get_transcription_results(transcription_id)
                res_raw = results
                print(f"Iteration {i + 1}: Transcription succeeded.")
                print(type(results))

                RAW_TXT_FILE = f"{SOURCE}/{MIC_TYPE}/batch_raw/Batch_raw_{MIC_TYPE}_60_{LEVEL}_{i + 1}.txt"
                PARSED_TXT_FILE = f"{SOURCE}/{MIC_TYPE}/batch_parsed/Batch_parse_{MIC_TYPE}_60_{LEVEL}_{i + 1}.txt"

                ### Save the parsed transcribed
                result_parsed = results['combinedRecognizedPhrases'][0]['display']
                print("res parsed:", result_parsed)
                with open(PARSED_TXT_FILE, "w") as log_file:
                    log_file.write(result_parsed)

                ### Save the raw transcribed
                res_in_json = json.dumps(res_raw, indent=4)
                # print("Transcription Results:", res_in_json)

                with open(RAW_TXT_FILE, "w") as log_file:
                    log_file.write(res_in_json)
                    
                success_count += 1

            else:
                print(f"Iteration {i + 1}: Transcription failed!")
                fail_count += 1

        except Exception as e:
            print(f"Iteration {i + 1}: An error occurred: {e}")
            fail_count += 1

    print(f"Transcription completed: {success_count} succeeded, {fail_count} failed.")


if __name__ == "__main__":
    main()
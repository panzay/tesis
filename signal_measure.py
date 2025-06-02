import numpy as np
import pyaudio
import time
import logging
import wave
import os


"""
Quiet Environment: 0.0001 - 0.001
This range corresponds to a quieter environment with less ambient noise.

Noisy Environment: 0.002 - 0.005
This suggests a moderately noisy environment, such as background chatter or distant noise.

Loud Environment: 0.01 - 0.1
For loud sounds like clapping, music, or shouting, power values will increase significantly.

Maximum Normalized Signal: 1.0
If the microphone captures a signal at its maximum amplitude, the power value will peak at 1.0.
"""


MIC_TYPE = "built-in"
ENV_TYPE = "hening"
LEVEL = "20"

file_path = "data_log/audacity/courthouse"
# 'data_log/audacity/courthouse/built-in/hening'

# SOURCE_LEVEL = "60"
# ENV_LEVEL = "100"
# FILENAME = f"signal_{MIC_TYPE}_{ENV_TYPE}_{SOURCE_LEVEL}_BG{ENV_LEVEL}_joined.log"
# FILENAME = f"signal_{MIC_TYPE}_{ENV_TYPE}_{SOURCE_LEVEL}_5mins.log"

FILENAME = f'{file_path}/{MIC_TYPE}/{ENV_TYPE}/signal_{LEVEL}.log'
print(FILENAME)

## ENV
# FILENAME = f"log_signal_ENV_5mins_{LEVEL}.log"

## Voice
# FILENAME = f"log_signal_voice_5mins_{LEVEL}.log"

# Specify the path to your audio file
# data_log/audacity/courthouse/built-in/hening/30.wav
audio_file_path = f'{file_path}/{MIC_TYPE}/{ENV_TYPE}/{LEVEL}.wav'
print(audio_file_path)

# Ensure the directory for the log file exists
log_dir = os.path.dirname(FILENAME)
os.makedirs(log_dir, exist_ok=True)

# Set up logging configuration
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename=FILENAME,
    filemode='a'
)


def calculate_signal_power(audio_data):
    """
    Calculate the signal power of audio data.
    Signal power is proportional to the square of the RMS value.
    """
    # Normalize audio data to [-1, 1]
    audio_data = audio_data / 32768.0
    # Compute RMS
    rms = np.sqrt(np.mean(np.square(audio_data)))
    # Compute power (proportional to RMS squared)
    power = rms ** 2
    return power

# PyAudio Setup from MIC
p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paInt16, channels=1, rate=44100, input=True, frames_per_buffer=4096)

print("Recording and measuring signal power...")
interval = 1  # Seconds
last_print_time = time.time()

try:
    while True:
        # Read audio data from the microphone
        audio_data = np.frombuffer(stream.read(4096), dtype=np.int16)
        signal_power = calculate_signal_power(audio_data)
        current_time = time.time()
        if current_time - last_print_time >= interval:
            # Log and display the signal power
            print(f"Signal Power: {signal_power:.6f}")
            # logging.info(f"Signal Power: {signal_power:.6f}")
            last_print_time = current_time
except KeyboardInterrupt:
    print("Stopping...")
finally:
    stream.stop_stream()
    stream.close()
    p.terminate()


# # Define a chunk size (in frames) to process the audio file in segments.
# CHUNK_SIZE = 4096
# # Open and read the audio file in chunks using the wave module
# with wave.open(audio_file_path, "rb") as wf:
#     while True:
#         # Read a chunk of frames from the audio file
#         audio_bytes = wf.readframes(CHUNK_SIZE)
#         # Exit loop if no more data is available
#         if not audio_bytes:
#             break
#         # Convert byte data to a numpy array of type int16
#         audio_data = np.frombuffer(audio_bytes, dtype=np.int16)
#         if len(audio_data) == 0:
#             break
#         # Calculate the signal power for the current chunk
#         signal_power = calculate_signal_power(audio_data)
#         # Print and log the signal power
#         print(f"Signal Power: {signal_power:.6f}")
#         logging.info(f"Signal Power: {signal_power:.6f}")

#         # time.sleep(1)


#### TWS

# def calculate_signal_power(audio_data, scale_factor=1e6):
#     """
#     Calculate the signal power of audio data and scale it for better readability.
#     """
#     # Normalize audio data to [-1, 1] and add small offset to avoid zero values
#     audio_data = (audio_data / 32768.0) + 1e-10
#     # Compute RMS with a floor to prevent zero RMS
#     rms = max(np.sqrt(np.mean(np.square(audio_data))), 1e-10)
#     # Compute power (proportional to RMS squared) and scale
#     power = (rms ** 2) * scale_factor
#     return power

# # PyAudio Setup
# p = pyaudio.PyAudio()
# stream = p.open(format=pyaudio.paInt16, channels=1, rate=44100, input=True, frames_per_buffer=4096)

# print("Recording and measuring signal power...")
# interval = 1  # Seconds
# last_print_time = time.time()

# try:
#     while True:
#         # Read audio data from the microphone
#         audio_data = np.frombuffer(stream.read(4096), dtype=np.int16)
        
#         # Debugging: log raw audio data
#         logging.debug(f"Raw audio data: {audio_data[:10]} (Min: {audio_data.min()}, Max: {audio_data.max()})")
        
#         signal_power = calculate_signal_power(audio_data)
        
#         current_time = time.time()
#         if current_time - last_print_time >= interval:
#             # Log and display the signal power
#             print(f"Signal Power: {signal_power:.6f}")
#             logging.info(f"Signal Power: {signal_power:.6f}")
#             last_print_time = current_time
# except KeyboardInterrupt:
#     print("Stopping...")
# finally:
#     stream.stop_stream()
#     stream.close()
#     p.terminate()
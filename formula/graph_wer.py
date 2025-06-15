import matplotlib.pyplot as plt
import numpy as np

mic_type = "TWS"
envi = "Noisy"
volume_level = "60"

MIC = mic_type.lower()

is_wer = True

if is_wer:
    FILEPATH_PNG = f'data_log/audacity/new_self-talk/{MIC}/WER.png'
else:
    FILEPATH_PNG = f'data_log/audacity/new_self-talk/{MIC}/SNR.png'


# Data
if is_wer:
    # # built-in
    # wer_values = [0.82, 2.30, 2.78, 4.84, 99.24]

    # # meeting
    # wer_values = [2.96, 4.78, 10.04, 46.45, 99.24]

    # # podcast
    # wer_values = [2.96, 3.06, 5.35, 11.57, 86.42]

    # tws
    wer_values = [7.27, 13.68, 26.22, 27.44, 100]
else:
    # # built-in
    # snr_values = [15.40, 9.03, 2.45, 0.56, -4.93]

    # # meeting
    # snr_values = [18.02, 6.28, 2.93, -3.26, -5.44]

    # # podcast
    # snr_values = [12.77, 4.89, -0.31, -4.74, -8.53]

    # tws
    snr_values = [28.90, 12.07, 6.52, 5.33, -1.61]

# Adjust timeline to start at 300 for the first value
timeline = np.arange(300, 1500 + 1, 300)  # Start from 300, up to 1500 seconds, in 300-second intervals

# Create plot
plt.figure(figsize=(10, 6))
if is_wer:
    plt.plot(timeline, wer_values, color='red', marker='o', label='WER')
else:
    plt.plot(timeline, snr_values, color='blue', marker='o', label='SNR')

# Add annotations
if is_wer:
    for i, wer in enumerate(wer_values):
        plt.annotate(f'{wer:.2f}%', (timeline[i], wer), textcoords="offset points", xytext=(0, 5), ha='center', color='blue')
else:
    for i, wer in enumerate(snr_values):
        plt.annotate(f'{wer:.2f} dB', (timeline[i], wer), textcoords="offset points", xytext=(0, 5), ha='center', color='red')

# Customize plot
if is_wer:
    plt.title(f'Word Error Rate (WER) Volume Level {volume_level} {mic_type}')
else:
    plt.title(f'Signal to Noise Ratio (SNR) Volume Level {volume_level} {mic_type}')

plt.xlabel('Time (seconds)')

if is_wer:
    plt.ylabel('WER (%)')
else:
    plt.ylabel('SNR (dB)')

plt.ylim(-10, 100)
plt.grid(True)
plt.legend()

# # Show plot
# plt.show()

plt.savefig(FILEPATH_PNG)

plt.close()
import numpy as np
import re

MIC_TYPE = 'tws'

FILEPATH_NOISE = f'data_log/audacity/new_self-talk/{MIC_TYPE}/rms_amplitude_noise_100.txt'
FILEPATH_VOICE = f'data_log/audacity/new_self-talk/{MIC_TYPE}/rms_amplitude_self-talk_60.txt'

# Read RMS noise values
noise_vals = []
with open(FILEPATH_NOISE, 'r') as f:
    for line in f:
        m = re.search(r'RMS\s*=\s*([0-9.]+)', line)
        if m:
            noise_vals.append(float(m.group(1)))

# Read RMS self-talk (signal) values
sig_vals = []
with open(FILEPATH_VOICE, 'r') as f:
    for line in f:
        m = re.search(r'RMS\s*=\s*([0-9.]+)', line)
        if m:
            sig_vals.append(float(m.group(1)))

# Align lengths to minimum
n = min(len(noise_vals), len(sig_vals))
noise_vals = np.array(noise_vals[:n])
sig_vals = np.array(sig_vals[:n])

# Compute instantaneous SNR for each pair
snr_vals = 20 * np.log10(sig_vals / noise_vals)

# Calculate average SNR
avg_snr = np.mean(snr_vals)

print(f"Nilai rata-rata SNR: {avg_snr:.2f} dB")

# import numpy as np
# import logging
# import re

# MIC_TYPE = "Meeting"
# ENV_TYPE = "flat_noise"
# SOURCE_LEVEL = "60"
# ENV_LEVEL = "20"
# # FILENAME = f"audio_signal_{MIC_TYPE}_{ENV_TYPE}_{SOURCE_LEVEL}_BG{ENV_LEVEL}_joined.log"
# # FILENAME = f"audio_signal_{MIC_TYPE}_{ENV_TYPE}_{SOURCE_LEVEL}_3mins.log"
# # FILENAME = f"audio_signal_{MIC_TYPE}_{ENV_TYPE}_3mins_{SOURCE_LEVEL}-{ENV_LEVEL}_ENV.log"

# FILENAME = f"snr_{MIC_TYPE}_{ENV_TYPE}_{SOURCE_LEVEL}_BG{ENV_LEVEL}_joined.log"

# # Set up logging configuration
# logging.basicConfig(
#     level=logging.INFO,
#     format='%(asctime)s - %(levelname)s - %(message)s',
#     filename=FILENAME,
#     filemode='a'
# )

# def load_signal_powers(path):
#     """Parse lines like 'RMS = 585.72' and return [585.72, ...]"""
#     values = []
#     pattern = re.compile(r'RMS\s*=\s*([-\d\.]+)')
#     with open(path, 'r') as f:
#         for line in f:
#             m = pattern.search(line)
#             if m:
#                 values.append(float(m.group(1)))
#     return values

# def load_db_values(path):
#     """Parse lines like '0.0s: 59.02 dB SPL' and return [59.02, ...]"""
#     values = []
#     pattern = re.compile(r':\s*([-\d\.]+)\s*dB SPL')
#     with open(path, 'r') as f:
#         for line in f:
#             m = pattern.search(line)
#             if m:
#                 values.append(float(m.group(1)))
#     return values

# # Load from your two files
# # data_log/audacity/new_self-talk/meeting/rms_amplitude_noise_20.txt
# # data_log/audacity/new_self-talk/meeting/raw_noise_20.txt
# mic_type = MIC_TYPE.lower()
# SIGNAL_FILEPATH = f'data_log/audacity/new_self-talk/{mic_type}/rms_amplitude_noise_{ENV_LEVEL}.txt'
# DB_FILEPATH = f'data_log/audacity/new_self-talk/{mic_type}/raw_noise_{ENV_LEVEL}.txt'

# signal_powers = load_signal_powers(SIGNAL_FILEPATH)
# db_values     = load_db_values(DB_FILEPATH)


# # # Provided signal and noise data
# # signal_powers = [
# #     -453.41, 169.96, -493.34, 1408.89, 398.82, 6600.37, 2722.51, -94.56, 
# #     1415.15, 398.82, 937.92, 1467.5, 1987.32, 525.69, -74.21, 2435.07, 676.56, 
# #     4100.83, 157.84, -856.14, 254.20, 253.88, 734.83, 821.46, 112.48, 1441.50, 
# #     1227.35, 5461.42, 2358.77, 157.84
# # ]

# # db_values = [-44.73366145398238, -36.50481196417992, -63.074175665045054, -36.62979094887816, -34.41897264396671, -43.46027987702143, -23.83132147852235, -12.791309804498924, -29.425781179549446, -31.175762007281232, -35.40723774000388, -35.01027388093405, -31.01411517089257, -39.01541226024163, -37.41996176893967, -30.501956497980665, -30.948419312324916, -59.182682816903416, -15.238604477994107, -22.086445240771624, -49.09477656827431, -45.34926813480092, -33.89157379104745, -30.196544687532562, -32.807508317051905, -28.922773356259917, -44.77949738878151, -34.89169334175202, -28.982215091163134, -36.558154340099705]

# # Sanity check
# if len(signal_powers) != len(db_values):
#     raise ValueError("Signal and noise lists have different lengths!")

# # Calculate SNRs
# snr_values = []
# for sig, db_noise in zip(signal_powers, db_values):
#     if sig <= 0:
#         snr_values.append(None)  # or any sentinel you like
#         continue

#     noise_power = 10 ** (db_noise / 10)
#     if noise_power <= 0:
#         snr_values.append(None)
#         continue

#     snr = 10 * np.log10(sig / noise_power)
#     snr_values.append(snr)

# # # Display the results
# # for i, snr in enumerate(snr_values):
# #     # print(f"SNR for Signal {signal_powers[i]} and Noise {db_values[i]}: {snr}")
# #     print(f"SNR: {snr}")
# #     logging.info(f"SNR: {snr}")

# # Output
# for i, snr in enumerate(snr_values):
#     msg = f"SNR[{i}]: {snr:.2f} dB" if snr is not None else f"SNR[{i}]: invalid"
#     print(msg)
#     logging.info(msg)

# # 'datalog/audacity/new_self-talk/meeting/rms_amplitude_noise_20.txt'
# # 'data_log/audacity/new_self-talk/meeting/rms_amplitude_noise_20.txt'


######### NEW #############

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

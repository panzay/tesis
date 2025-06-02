
# ### Nyquist Theorem ###
# # Import necessary libraries
# import numpy as np

# # Define variables
# f_max = 20000  # Maximum frequency in Hz (20 kHz)
# nyquist_rate = 2 * f_max  # Nyquist Theorem: Minimum sampling rate should be twice the max frequency
# sampling_rate = 44100  # Standard CD sampling rate

# print(f"Nyquist Sampling Rate: {nyquist_rate} Hz")
# print(f"Chosen Sampling Rate: {sampling_rate} Hz")


# ### quantization ###
# import numpy as np

# # Example signal
# signal = np.linspace(-1, 1, num=1000)  # A linear signal from -1 to 1

# # Define bit depth
# bit_depth = 16
# quantization_levels = 2 ** bit_depth  # Number of quantization levels

# # Perform quantization
# quantized_signal = np.round(signal * (quantization_levels / 2)) / (quantization_levels / 2)

# # Ensure the signal is within the range of 16-bit integer values
# quantized_signal = np.clip(quantized_signal, -1, 1)

# # Scale the signal to the 16-bit integer range
# quantized_signal = np.round(quantized_signal * (quantization_levels / 2))

# # Print the quantization levels and the first 10 samples of the quantized signal
# print(f"Quantization Levels: {quantization_levels}")
# print(f"Sample Quantized Signal: {quantized_signal[:10]}")


### Anti-Aliasing Filter ###
import numpy as np
from scipy import signal
import matplotlib.pyplot as plt

# Step 1: Create a sample signal with two frequencies
sampling_rate = 15_000  # Hz
t = np.linspace(0, 1.0, int(sampling_rate * 1.0) + 1)  # Time vector for 1 second at 1000 Hz
input_signal = np.sin(2 * np.pi * 20 * t) + np.sin(2 * np.pi * 80 * t)  # Signal with 20 Hz and 80 Hz components
print('INPUT SIGNALS:', input_signal)

# Step 2: Design a low-pass Butterworth filter
nyquist_rate = sampling_rate / 2  # Nyquist frequency is half the sampling rate
cutoff_frequency = 50  # Cutoff frequency in Hz (above which we attenuate frequencies)
filter_order = 10  # Filter order (higher means sharper cutoff)

# Generate filter coefficients in SOS format for numerical stability
sos = signal.butter(filter_order, cutoff_frequency, 'low', fs=sampling_rate, output='sos')

# Step 3: Apply the filter to the input signal
filtered_signal = signal.sosfilt(sos, input_signal)
print('FILTERED:', filtered_signal)

# Optional Visualization to show the effect of the filter
plt.figure(figsize=(12, 6))

# Plot the original signal
plt.subplot(2, 1, 1)
plt.plot(t, input_signal, label="Original Signal", color="blue")
plt.title("Original Signal (20 Hz and 80 Hz components)")
plt.xlabel("Time [seconds]")
plt.ylabel("Amplitude")
plt.legend()

# Plot the filtered signal
plt.subplot(2, 1, 2)
plt.plot(t, filtered_signal, label="Filtered Signal", color="red")
plt.title("Filtered Signal (Frequencies above 50 Hz removed)")
plt.xlabel("Time [seconds]")
plt.ylabel("Amplitude")
plt.legend()

plt.tight_layout()
# plt.savefig('Anti-Aliasing Filter.png')
plt.show()


# ### Frequency ###
# # Define the period of the wave (in seconds)
# T = 0.001  # Period = 1 ms

# # Calculate frequency
# frequency = 1 / T
# print(f"Frequency: {frequency} Hz")


# ### Amplitude ###
# import numpy as np

# # Example signal
# t = np.linspace(0, 1, 1000)
# waveform = np.sin(2 * np.pi * 5 * t)  # A 5 Hz sine wave

# # Find the amplitude
# amplitude = np.max(np.abs(waveform))
# print(f"Amplitude: {amplitude}")


# ### Decibel ###
# import numpy as np

# # Define signal intensity and reference intensity
# intensity_signal = 1e-6  # In W/m²
# intensity_ref = 1e-12  # Threshold of hearing in W/m²

# # Calculate decibel level
# dB_level = 10 * np.log10(intensity_signal / intensity_ref)
# print(f"Decibel Level: {dB_level} dB")


# ### MFCC ###
# import librosa
# import librosa.display
# import matplotlib.pyplot as plt

# # Load an example audio file
# audio_file = 'example.wav'
# y, sr = librosa.load(audio_file)

# # Compute MFCC features
# mfcc = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=13)

# # Display the MFCC
# librosa.display.specshow(mfcc, x_axis='time')
# plt.colorbar()
# plt.title('MFCC')
# plt.tight_layout()
# plt.savefig('MFCC.png')
# plt.show()


### HMM ###
# from hmmlearn import hmm
# import numpy as np

# # Spesifikasi teknis:
# # - Model menggunakan GaussianHMM dari pustaka hmmlearn
# # - Jumlah state ditentukan dengan parameter n_states
# # - Covariance_type 'diag' menunjukkan bahwa tiap fitur memiliki varians sendiri-sendiri
# # - n_features disesuaikan untuk mendukung fitur berbasis suara seperti MFCC

# # Definisikan parameter HMM
# n_states = 3               # Jumlah state tersembunyi, biasanya merepresentasikan fonem atau suku kata
# n_features = 13            # Jumlah fitur per sampel (contohnya, jumlah koefisien MFCC)

# # Inisialisasi model HMM
# model = hmm.GaussianHMM(n_components=n_states, covariance_type='diag')

# # Menghasilkan data pelatihan contoh
# # Di sini X merupakan array dua dimensi dengan bentuk (jumlah_sampel, n_features)
# # Contoh data dibuat secara acak, namun dalam implementasi nyata, data ini bisa berupa fitur suara (seperti MFCC)
# X = np.random.rand(100, n_features)

# # Latih model menggunakan data pelatihan
# # Model akan menyesuaikan parameter λ = (A, B, π):
# # A: matriks transisi antar state
# # B: distribusi probabilitas observasi per state
# # π: probabilitas awal state
# model.fit(X)

# # Prediksi urutan state tersembunyi untuk data pelatihan
# # Ini menunjukkan kemungkinan urutan state yang ditempuh untuk observasi X
# hidden_states = model.predict(X)
# print(f"Hidden States: {hidden_states}")


### SNR ###
# import numpy as np

# # Example signal and noise power
# P_signal = 0.001  # Signal power in W
# P_noise = 0.00001  # Noise power in W

# # Calculate SNR in dB
# SNR_dB = 10 * np.log10(P_signal / P_noise)
# print(f"Signal-to-Noise Ratio: {SNR_dB} dB")


###########

# import numpy as np
# import matplotlib.pyplot as plt
# from scipy.interpolate import interp1d

# fmax = 15_000  # 15 kHz
# duration = 0.001  # 1 ms

# fs_nyquist = 30_000  # Sesuai teori Nyquist
# fs_aliased = 18_000  # Di bawah Nyquist

# fs_list = [fs_nyquist, fs_aliased]
# labels = [
#     "fs = 30 kHz (Nyquist, No Aliasing)",
#     "fs = 18 kHz (Aliasing)"
# ]
# colors = ['blue', 'green']

# plt.figure(figsize=(10, 5))

# for idx, (fs, label, color) in enumerate(zip(fs_list, labels, colors)):
#     t = np.arange(0, duration, 1/fs)
#     signal = np.sin(2 * np.pi * fmax * t)
#     # Garis halus
#     t_fine = np.linspace(t[0], t[-1], 400)
#     signal_fine = interp1d(t, signal, kind='cubic')(t_fine)

#     plt.subplot(2, 1, idx+1)
#     plt.plot(t_fine*1000, signal_fine, color=color, linewidth=2, label=label)
#     plt.scatter(t*1000, signal, color=color, s=20, zorder=10)
#     plt.title(label)
#     plt.xlabel("Time [ms]")
#     plt.ylabel("Amplitude")
#     plt.legend()
#     plt.grid()

# plt.tight_layout()
# plt.savefig('Aliasing and Anti-Aliasing Filter.png')
# plt.show()

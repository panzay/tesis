import os
import re
import numpy as np
import matplotlib.pyplot as plt

mic_type = "TWS"
envi = "Flat Noise"
source_sound = "Flat Voice"
level = "80"

flag_voice = False
flag_db = False

filename = ''

MIC_TYPE = "TWS"
ENV = "hening"
VOLUME_LEVEL = level
TYPE = "noise"

if flag_voice and flag_db:
    # DB voice
    file_path = f"data_log/audacity/new_self-talk/{MIC_TYPE}/filtered_self-talk_{VOLUME_LEVEL}.txt"
elif not flag_voice and flag_db:
    # DB noise
    file_path = f"data_log/audacity/new_self-talk/{MIC_TYPE}/filtered_{TYPE}_{VOLUME_LEVEL}.txt"

elif flag_voice and not flag_db:
    # RMS voice
    file_path = f"data_log/audacity/new_self-talk/{MIC_TYPE}/rms_amplitude_self-talk_{VOLUME_LEVEL}.txt"
elif not flag_voice and not flag_db:
    # RMS noise
    file_path = f"data_log/audacity/new_self-talk/{MIC_TYPE}/rms_amplitude_noise_{VOLUME_LEVEL}.txt"


output_file = f"data_log/audacity/new_self-talk/{MIC_TYPE}"


SINGLE_FILE_PROCESS_FLAG = False

# Single graph process
if SINGLE_FILE_PROCESS_FLAG:
    # Open the file in read mode
    print('FILEPATH:', file_path)
    with open(file_path, 'r') as file:
        # Read the content of the file
        db_data = file.read()

    # Extracting dB values
    if flag_db:
        db_values = [float(line.split(': ')[1].split()[0]) for line in db_data.strip().split('\n')] # db
    else:
        db_values = [float(line.split(' = ')[1]) for line in db_data.strip().split('\n')] # rms

    print(db_values)
else:
    # Folder containing the .txt files
    folder_path = f"data_log/audacity/new_self-talk/{MIC_TYPE}"
    print('folder_path:', folder_path)

    # List to store all dB values
    db_values = []
    line_lengths = []

    # List of specific files to process, in the desired order
    if flag_db:
        if not flag_voice:
            target_files = [
                'filtered_noise_20.txt',
                'filtered_noise_40.txt',
                'filtered_noise_60.txt',
                'filtered_noise_80.txt',
                'filtered_noise_100.txt'
            ]
        if  flag_voice:
            print('VOICE JOINED')
            target_files = ['filtered_self-talk_60.txt'] * 5
            # print('target_files:', target_files)

        # Loop through the target files in the specified order
        for file_name in target_files:
            file_path = os.path.join(folder_path, file_name)
            print('file_path: ', file_path)
            
            if os.path.exists(file_path):  # Check if the file exists
                # Open the file and extract dB values
                with open(file_path, 'r') as file:
                    db_data = file.read()
                
                # Extracting dB values from the file content
                values = [float(line.split(': ')[1].split()[0]) for line in db_data.strip().split('\n')]
                # print('values:', values)
                
                # Add the extracted values to the db_values list
                db_values.extend(values)

                # Record the length of the values from this file
                line_lengths.append(len(values))
    else:
        # print('Flag DB:', flag_db)
        if not flag_voice:
            target_files = [
                'rms_amplitude_noise_20.txt',
                'rms_amplitude_noise_40.txt',
                'rms_amplitude_noise_60.txt',
                'rms_amplitude_noise_80.txt',
                'rms_amplitude_noise_100.txt'
            ]
        if flag_voice:
            print('AMPLITUDE VOICE JOINED')
            target_files = ['rms_amplitude_self-talk_60.txt'] * 5
        print('Target Files:', target_files)
        
        # Loop through the target files in the specified order
        for file_name in target_files:
            file_path = os.path.join(folder_path, file_name)
            print('file_path: ', file_path)
            
            if os.path.exists(file_path):  # Check if the file exists
                # Open the file and extract dB values
                with open(file_path, 'r') as file:
                    db_data = file.read()
                # print(db_data)
                
                for line in db_data.strip().splitlines():
                    match = re.search(r"RMS = ([\d.]+)", line)
                    if match:
                        db_values.append(float(match.group(1)))
                
                
                # print('db_values:', db_values)
                # Record the length of the values from this file
                line_lengths.append(len(db_values))
            else:
                print('File path not exist!')
    print("Line Lengths:", line_lengths)

print("Extracted dB Values:", db_values)
time_values = list(range(len(db_values)))  # x-axis in seconds
# print('time_values:', time_values)
# print('db_values:', db_values)

# Calculate the trend line
# coefficients = np.polyfit(time_values, db_values, 1)  # Linear fit
# trend_line = np.polyval(coefficients, time_values)  # Calculate trend line values

# Plotting the graph
plt.figure(figsize=(10, 6))

# Plotting the dB levels
# for i in range(len(db_values) - 1):
    # if -75 <= db_values[i] <= -55:  # Check if the current dB value is between -6 and -8
    #     plt.plot(time_values[i:i+2], db_values[i:i+2], color='red', marker='o', linestyle='-')  # Red line
    # else:
    #     plt.plot(time_values[i:i+2], db_values[i:i+2], color='blue', marker='o', linestyle='-')  # Blue line

# plt.plot(time_values, db_values, marker='o', linestyle='-', color='b', label='dB Levels')
# plt.plot(time_values, db_values, marker='o', linestyle='-', color='b', label='Signal')
# plt.plot(time_values, trend_line, color='r', linestyle='--', label='Trend Line')  # Trend line

plt.xlabel('Time (seconds)')

if SINGLE_FILE_PROCESS_FLAG:
    # Adding titles and labels
    if flag_voice and flag_db:
        print('FLAT VOICE')
        ## Flat Voice
        plt.plot(time_values, db_values, marker='o', linestyle='-', color='b', label='dB Levels')
        plt.title(f'{mic_type} Mic - {source_sound} - dB')
        plt.ylabel('dB Level')
        # filename = f'Kalman_db_Voice_5mins_{level}.png'
        filename = f"{output_file}/graph_voice_3mins_{level}.png"

    elif not flag_voice and flag_db:
        print('FLAT NOISE')
        ## ENV Noise
        plt.plot(time_values, db_values, marker='o', linestyle='-', color='b', label='dB Levels')
        plt.title(f'{mic_type} Mic - {envi} - dB')
        plt.ylabel('dB Level')
        # filename = f'db_ENV_5mins_{level}.png'
        filename = f"{output_file}/graph_noise_3mins_{level}.png"

    elif flag_voice and not flag_db:
        ## Signal Voice
        plt.plot(time_values, db_values, marker='o', linestyle='-', color='b', label='Signal')
        plt.title(f'{mic_type} Mic - {source_sound} - Signal')
        plt.ylabel('Signal Power')
        # filename = f'Signal_Voice_5mins_{level}.png'
        filename = f"{output_file}/graph_signal_voice_3mins_{level}.png"

    elif not flag_voice and not flag_db:
        ## Signal Noise
        plt.plot(time_values, db_values, marker='o', linestyle='-', color='b', label='Signal')
        plt.title(f'{mic_type} Mic - {envi} - Signal')
        plt.ylabel('Signal Power')
        # filename = f'Signal_ENV_5mins_{level}.png'
        filename = f"{output_file}/graph_signal_noise_3mins_{level}.png"
else:
    if flag_db:
        if flag_voice:
            print('FLAT VOICE JOINED')
            filename = f"{output_file}/graph_voice_3mins_joined2.png"
            print('FLAT VOICE filename:', filename)
        if not flag_voice:
            print('FLAT NOISE JOINED')
            filename = f"{output_file}/graph_noise_3mins_joined2.png"
            print('FLAT VOICE filename:', filename)

        # Indices for vertical lines
        sep_1 = line_lengths[0]
        print('sep_1:', sep_1)
        sep_2 = sep_1 + line_lengths[1]
        print('sep_2:', sep_2)
        sep_3 = sep_2 + line_lengths[2]
        print('sep_3:', sep_3)
        sep_4 = sep_3 + line_lengths[3]
        print('sep_4:', sep_4)
    else:
        if flag_voice:
            print('AMPLITUDE FLAT VOICE JOINED')
            filename = f"{output_file}/graph_signal_voice_3mins_joined.png"
            print('AMPLITUDE FLAT VOICE filename:', filename)
        else:
            print('AMPLITUDE FLAT NOISE JOINED')
            filename = f"{output_file}/graph_signal_noise_3mins_joined.png"
            print('AMPLITUDE FLAT NOISE filename:', filename)
        
        # Indices for vertical lines
        sep_1 = line_lengths[0]
        print('sep_1:', sep_1)
        sep_2 = line_lengths[1]
        print('sep_2:', sep_2)
        sep_3 = line_lengths[2]
        print('sep_3:', sep_3)
        sep_4 = line_lengths[3]
        print('sep_4:', sep_4)


    print('DB Values LEN:', len(db_values))

    ## Flat Voice
    plt.plot(time_values, db_values, marker='o', linestyle='-', color='b', label='dB Levels')

    # Add vertical dotted lines
    plt.axvline(x=time_values[sep_1 - 1], color='gray', linestyle='--', linewidth=1)  # Between 20 and 40
    plt.axvline(x=time_values[sep_2 - 1], color='gray', linestyle='--', linewidth=1)  # Between 40 and 60
    plt.axvline(x=time_values[sep_3 - 1], color='gray', linestyle='--', linewidth=1)  # Between 60 and 80
    plt.axvline(x=time_values[sep_4 - 1], color='gray', linestyle='--', linewidth=1)  # Between 80 and 100

    if flag_db:
        # Add annotations for each segment
        plt.text(time_values[sep_1 // 2], max(db_values) + 1, '20%', ha='center', color='gray')
        plt.text(time_values[sep_1 + line_lengths[1] // 2], max(db_values) + 1, '40%', ha='center', color='gray')
        plt.text(time_values[sep_2 + line_lengths[2] // 2], max(db_values) + 1, '60%', ha='center', color='gray')
        plt.text(time_values[sep_3 + line_lengths[3] // 2], max(db_values) + 1, '80%', ha='center', color='gray')
        plt.text(time_values[sep_4 + line_lengths[4] // 2], max(db_values) + 1, '100%', ha='center', color='gray')

        plt.title(f'{mic_type} Mic - {source_sound} - dB - Joined')
        plt.ylabel('dB Level')
    else:
        print('plot signal')
        # Add annotations for each segment
        plt.text(time_values[sep_1], max(db_values) + 1, '20%', ha='center', color='gray')
        plt.text(time_values[sep_1], max(db_values) + 1, '40%', ha='center', color='gray')
        plt.text(time_values[sep_2], max(db_values) + 1, '60%', ha='center', color='gray')
        plt.text(time_values[sep_3], max(db_values) + 1, '80%', ha='center', color='gray')
        plt.text(time_values[sep_4], max(db_values) + 1, '100%', ha='center', color='gray')

        plt.title(f'{mic_type} Mic - {source_sound} - Signal - Joined')
        plt.ylabel('Signal Level')
    
    # filename = f'Kalman_db_Voice_5mins_{level}.png'
    
    print('JOINED Plot filename:', filename)

# plt.xticks(time_values)  # Optional: set x-ticks to match time values
plt.legend()

if flag_db:
    # Setting the y-axis range from 0 to 100, for db only
    plt.ylim(0, 100)
else:
    # Setting the y-axis range from 0 to 100, for signal only
    plt.ylim(100, 10000) # joined


# Saving the plot as an image
plt.savefig(filename)
plt.close()

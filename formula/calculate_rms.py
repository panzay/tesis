import math
import ast
from tqdm import tqdm

def calculate_rms(audio_data):
    """Calculate RMS of audio signal."""
    if not audio_data:  # Check for empty list
        return 0.0  # Return 0 as RMS for an empty signal
    square_sum = sum(sample ** 2 for sample in audio_data)  # Simplified sum of squares
    mean_square = square_sum / len(audio_data)
    return math.sqrt(mean_square)

def process_file(input_file, output_log):
    """Calculate RMS for each line in the input file and save results to a log."""
    try:
        with open(input_file, 'r') as infile:
            lines = infile.readlines()  # Read all lines
        total_lines = len(lines)
        
        with open(output_log, 'w') as logfile, tqdm(total=total_lines, desc="Processing Lines") as pbar:
            for line_number, line in enumerate(lines, start=1):
                try:
                    # Parse the line as a list of numbers
                    audio_data = ast.literal_eval(line.strip())
                    if not isinstance(audio_data, list):  # Validate that it's a list
                        raise ValueError("Line does not contain a list")
                    
                    # Calculate RMS
                    rms_value = calculate_rms(audio_data)
                    
                    # Write result to log
                    logfile.write(f"Line {line_number}: RMS = {rms_value:.2f}\n")
                except Exception as e:
                    # Handle parsing or calculation errors
                    logfile.write(f"Line {line_number}: Error - {str(e)}\n")
                pbar.update(1)  # Update the progress bar
    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found.")
    except Exception as e:
        print(f"Unexpected error: {str(e)}")


# Usage
MIC_TYPE = "tws"
ENV = "hening"
VOLUME_LEVEL = "80"
TYPE = "noise"

file_path = f"data_log/audacity/new_self-talk/{MIC_TYPE}/amplitude_{TYPE}_{VOLUME_LEVEL}.txt"
# data_log/audacity/new_self-talk/tws/amplitude_noise_80.txt

output_file = f"data_log/audacity/new_self-talk/{MIC_TYPE}/rms_amplitude_{TYPE}_{VOLUME_LEVEL}.txt"

process_file(file_path, output_file)

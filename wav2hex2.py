import os
import numpy as np
from scipy.io import wavfile
import csv

# Function to segment and normalize the waveform
def segment_and_normalize_waveform(waveform, segment_length, max_segments):
    segments = []
    for i in range(0, min(len(waveform), segment_length * max_segments), segment_length):
        segment = waveform[i:i + segment_length]
        if len(segment) < segment_length:
            segment = np.pad(segment, (0, segment_length - len(segment)), 'constant')
        normalized_segment = np.interp(segment, (segment.min(), segment.max()), (0, 15)).astype(int)
        segments.append(normalized_segment)
    return segments

# Function to convert normalized segments to hexadecimal representation
def segments_to_hex(segments):
    hex_segments_no_leading_zeros = []
    hex_segments_with_leading_zeros = []
    for segment in segments:
        hex_segment_no_leading_zeros = [format(value, 'X') for value in segment]
        hex_segment_no_leading_zeros = [value.lstrip('0') or '0' for value in hex_segment_no_leading_zeros]
        hex_segments_no_leading_zeros.append(''.join(hex_segment_no_leading_zeros))

        hex_segment_with_leading_zeros = [f"${format(value, '02X')}" for value in segment]
        hex_segments_with_leading_zeros.append(''.join(hex_segment_with_leading_zeros))
        
    return hex_segments_no_leading_zeros, hex_segments_with_leading_zeros

# Create output directory if it doesn't exist
os.makedirs('output', exist_ok=True)

# Process each WAV file in the input directory
input_directory = 'input'
for filename in os.listdir(input_directory):
    if filename.endswith('.wav'):
        # Load the audio file
        sample_rate, data = wavfile.read(os.path.join(input_directory, filename))

        # Ensure mono format and normalize
        if data.ndim == 2:
            data = data.mean(axis=1)
        data = data / np.max(np.abs(data))

        # Segment and normalize the waveform
        normalized_segments = segment_and_normalize_waveform(data, 32, 15)

        # Convert the normalized segments to hexadecimal representation
        hex_segments_no_leading_zeros, hex_segments_with_leading_zeros = segments_to_hex(normalized_segments)

        # Write the hex segments to a CSV file
        output_filename = os.path.join('output', f"{os.path.splitext(filename)[0]}.csv")
        with open(output_filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Hex Values without Leading Zeros"])
            for i, segment in enumerate(hex_segments_no_leading_zeros):
                writer.writerow([f"{segment}"])

            writer.writerow([])  # Add an empty row for separation
            writer.writerow(["Hex Values with Leading Zeros"])
            for i, segment in enumerate(hex_segments_with_leading_zeros):
                writer.writerow([f"{segment}"])

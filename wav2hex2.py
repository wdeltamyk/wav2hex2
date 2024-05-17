import numpy as np
from scipy.io import wavfile

# Load the audio file
sample_rate, data = wavfile.read('input/Piano_480bytes.wav')

# Ensure mono format and normalize
if data.ndim == 2:
    data = data.mean(axis=1)
data = data / np.max(np.abs(data))

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

# Segment and normalize the waveform
normalized_segments = segment_and_normalize_waveform(data, 32, 15)

# Function to convert normalized segments to hexadecimal representation
def segments_to_hex(segments):
    hex_segments = []
    for segment in segments:
        hex_segment = [format(value, 'X') for value in segment]
        # Remove leading zeros for values
        hex_segment = [value.lstrip('0') or '0' for value in hex_segment]
        hex_segments.append(hex_segment)
    return hex_segments

# Convert the normalized segments to hexadecimal representation
hex_segments = segments_to_hex(normalized_segments)

# Display the hexadecimal segments
for i, segment in enumerate(hex_segments):
    print(f"Segment {i+1}: {segment}")
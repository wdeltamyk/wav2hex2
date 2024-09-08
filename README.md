# wav2hex2

## Overview
wav2hex2 is an advanced audio processing utility, building upon the original wav2hex script. This upgraded version is specifically tailored for use with hUGETracker, offering enhanced capabilities for converting larger 8-bit mono samples into multiple 32x16 hexadecimal waveform grids. The tool is designed to optimize audio samples for use in chiptune and retro-style music production.

## Key Features
- Processes larger 8-bit mono samples
- Segments samples into up to 15 32x16 grids
- Normalizes and compresses audio to fit the 16-height limit of Game Boy trackers
- Outputs both stripped (leading zeros removed) and formatted ($0F, $06, etc.) hexadecimal representations
- Batch processing of multiple WAV files

## Technical Specifications

### Input Requirements
- File Format: 8-bit mono WAV
- Recommended Duration: ≤ 4 seconds (optimal: ≤ 1 second)
- Input Directory: Place WAV files in the "input" folder

### Output
- Multiple 32x16 hexadecimal waveform grids (up to 15 segments)
- CSV files containing hexadecimal data
- Two hex formats: stripped of leading zeros and formatted for routine triggering

## Dependencies
- Python 3.x
- NumPy
- SciPy
- Standard Python libraries: csv, os

### Installation
Install required packages using pip:
```
pip install -U numpy scipy
```

## Usage
1. Place WAV file(s) in the "input" folder
2. Run the script or executable
3. Output CSV files will be generated in the "output" folder
4. Check the terminal for any processing errors

## Advanced Features
- Batch processing of all WAV files in the input folder
- Hexadecimal output in two formats:
  1. Stripped of leading zeros (for single wavetable conversion)
  2. Formatted as $0F, $06, etc. (for triggering multiple wavetables as a routine)

## Executable Version
An executable (.exe) version is included for users without Python installed. Run it like any standard program.

## Limitations
- Processes only 8-bit mono WAV files
- Optimized for short samples (≤ 4 seconds)
- Maximum of 15 segments per sample

## Future Development
- Dynamic segmentation based on sample length
- Support for additional input formats
- Enhanced error handling and reporting

---

For issues, feature requests, or contributions, please open an issue or pull request on the GitHub repository.

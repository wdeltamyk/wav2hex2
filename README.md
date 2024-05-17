# wav2hex2

An update to my original wav2hex script - more tailored toward hUGETracker, does the same thing in theory, but now can take a bigger 8bit mono sample, chops it into 15 segments (or fewer) 32x16 grids, from the start of the first sample segment to the last. Normalizes and crushes the sound to fit into the max height of 16 for gameboy trackers.

# Limitations

The sample needs to be 8bit mono, it will just crash otherwise. The shorter the sample the better, I wouldn't go over 4 seconds as a max, but 1 second or less will net you the best results, there's a lot of sacrificing that needs to be done to have the sample fit a 32x16 wavetable grid

# Requirements

Requires Numpy, csv, os and SciPy. Numpy and SciPy can be installed easily by running "pip install -U numpy" or pip install -U scipy" in a terminal or console, the other two are bog standard.

# Use

Throw any wav into the included "input" folder, tests included, ~~for now this needs to be pointed to a specific file [will update with additional features at {redacted} date]~~. Updated to include all wav files stored in the input folder. The hex output ignores the first digit of the string, as this is always a return to 0, where hUGETracker only needs the deviations from 0, except where a leading 0 is followed by another 0, the second 0 is still captured.

# Output

after the script runs, it will create a bunch of CSV files per item in the input folder and throw them in an output folder as one string. If it can't process a file it will show it in a terminal but will still run against the files it can process.

# Final update

exe included for those without python or who don't want to use it, just run the exe as you would any normal program.

# Evidently not final update

Added a function for the script to provide the hex as both stripped of the leading 0's and in this format: $0F, $06, etc, the former being more useful for converting a single sample to a single wavetable, the latter for triggering a bunch of wavetables as a routine.
import os
import re

# Directory where the images are saved
directory = '.'

# Pattern to match image files like 'image-001.png'
pattern = re.compile(r'image-(\d+)\.png')

# Loop through all files in the directory
for filename in os.listdir(directory):
    match = pattern.match(filename)
    if match:
        # Get the frame number, strip leading zeros
        frame_number = int(match.group(1))
        # Create the new filename without leading zeros
        new_filename = f'image-{frame_number}.png'
        # Rename the file
        os.rename(filename, new_filename)
        print(f'Renamed: {filename} -> {new_filename}')



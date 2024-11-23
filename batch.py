import os
import shutil
import re

# Set the folder paths
source_folder = '/Users/samahithar/Documents/Capstone2/Face extraction/Sky_Face/Sky_Clip6'  # Replace with the path to your folder containing frames
output_folder = '/Users/samahithar/Documents/Capstone2/Face extraction/Sky_Face/Sky_Clip6_Batch'  # Replace with the path to where you want sorted folders

# Ensure the output folder exists
os.makedirs(output_folder, exist_ok=True)

# Regex to extract time and frame info from filenames
pattern = r"face_(\d+)min_(\d+)sec_(\d+)frame"

# Get all frame files and sort them based on time (minute, second, frame number)
frames = sorted([f for f in os.listdir(source_folder) if re.match(pattern, f)], 
                key=lambda x: (int(re.match(pattern, x).group(1)), 
                               int(re.match(pattern, x).group(2)), 
                               int(re.match(pattern, x).group(3))))

# Organize every 9 frames into separate folders
for i in range(0, len(frames), 9):
    # Determine the output folder name
    folder_num = i // 9 + 1
    dest_folder = os.path.join(output_folder, f"batch_{folder_num}")
    os.makedirs(dest_folder, exist_ok=True)
    
    # Move the 9 frames into the new folder
    for frame in frames[i:i+9]:
        src = os.path.join(source_folder, frame)
        dest = os.path.join(dest_folder, frame)
        shutil.move(src, dest)

print("Frames have been organized into folders.")

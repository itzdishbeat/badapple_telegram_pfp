import os

def rename_files_in_reverse_order(folder_path):
    # Get a list of all files in the folder
    files = sorted(os.listdir(folder_path), reverse=True)
    
    # Iterate through the files
    for index, old_name in enumerate(files, start=1):
        # Get the file extension
        _, extension = os.path.splitext(old_name)
        
        # Create the new name with zero-padding
        new_name = f"{index:03d}{extension}"
        
        # Full paths for old and new names
        old_path = os.path.join(folder_path, old_name)
        new_path = os.path.join(folder_path, new_name)
        
        # Rename the file
        try:
            os.rename(old_path, new_path)
            print(f"Renamed: {old_name} -> {new_name}")
        except Exception as e:
            print(f"Error renaming {old_name}: {e}")

# Define the path to the frames folder
frames_folder = 'frames'

# Get a list of all files in the frames folder
files = sorted(os.listdir(frames_folder))

# Iterate through the files
for index, file in enumerate(files):
    # Delete every 12th file (1-based index)
    if (index + 1) % 12 != 0:
        file_path = os.path.join(frames_folder, file)
        try:
            os.remove(file_path)
            print(f"Deleted: {file}")
        except Exception as e:
            print(f"Error deleting {file}: {e}")

print("Finished processing files.")

# Call the function to rename the remaining files in reverse order
rename_files_in_reverse_order(frames_folder)

print("Finished renaming files in reverse order.")
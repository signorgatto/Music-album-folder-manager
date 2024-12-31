import os
import shutil
from mutagen.mp3 import MP3
from mutagen.easyid3 import EasyID3

# Function to remove invalid characters from folder
def sanitize_folder_name(name):
    invalid_chars = r'<>:"/\|?*'
    return ''.join(char for char in name if char not in invalid_chars)

def organize_mp3_files(directory):
    for file in os.listdir(directory):
        if file.endswith('.mp3'):
            file_path = os.path.join(directory, file)
            try:
                # Read metadata
                audio = MP3(file_path, ID3=EasyID3)
                album_artist = audio.get('albumartist', [None])[0]
                album = audio.get('album', [None])[0]

                # Check if metadata is present
                if not album_artist or not album:
                    print(f"Insufficient metadata for {file}. File ignored.")
                    continue

                # Set folder name and remove invalid characters
                folder_name = sanitize_folder_name(f"{album_artist} - {album}")
                folder_path = os.path.join(directory, folder_name)

                # Create the folder if it doesn't exist
                os.makedirs(folder_path, exist_ok=True)

                # Move files into their directory
                shutil.move(file_path, os.path.join(folder_path, file))
                print(f"{file} moved to {folder_path}.")
            except Exception as e:
                print(f"Error processing {file}: {e}")

# Change the path to your directory
organize_mp3_files('C:/Users/signorgatto/Downloads')
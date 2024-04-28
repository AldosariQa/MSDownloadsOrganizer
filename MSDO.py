import os
import shutil
import time

downloads_dir = os.path.join(os.path.expanduser("~"), "Downloads")

# Dictionary to store extension as key and folder name as value
extension_folders = {}

# List all files in the Downloads directory
files = os.listdir(downloads_dir)

def create_folders(extension_folders, downloads_dir, files):
    # Iterate through the files
    for file_name in files:
        # Get the extension of the file
        _, extension = os.path.splitext(file_name)
        extension = extension.lower()  # Convert extension to lowercase for consistency
        
        # Skip if the file is a directory
        if os.path.isdir(os.path.join(downloads_dir, file_name)):
            continue
        
        # Create a folder for each unique extension if it doesn't exist
        if extension not in extension_folders:
            folder_name = extension.lstrip('.') + '_files'  # Folder name without the dot
            extension_folders[extension] = folder_name
            folder_path = os.path.join(downloads_dir, folder_name)
            os.makedirs(folder_path, exist_ok=True)

def move_files(extension_folders, downloads_dir, files):
    # Move files to their respective folders
    for file_name in files:
        _, extension = os.path.splitext(file_name)
        extension = extension.lower()
        
        # Skip if the file is a directory
        if os.path.isdir(os.path.join(downloads_dir, file_name)):
            continue
        
        # Get the folder name corresponding to the file extension
        folder_name = extension_folders.get(extension)
        if folder_name:
            # Move the file to the respective folder
            src = os.path.join(downloads_dir, file_name)
            dst = os.path.join(downloads_dir, folder_name, file_name)
            shutil.move(src, dst)

def get_files_in_directory(directory):
    return os.listdir(directory)

def check_files_added(previous_files, current_files):
    added_files = [file for file in current_files if file not in previous_files]
    return added_files

def main():
    create_folders(extension_folders, downloads_dir, files)
    move_files(extension_folders, downloads_dir, files)
    previous_files = get_files_in_directory(downloads_dir)

    while True:
        current_files = get_files_in_directory(downloads_dir)
        added_files = check_files_added(previous_files, current_files)
    
        if added_files:
            create_folders(extension_folders, downloads_dir, added_files)
            move_files(extension_folders, downloads_dir, added_files)    
        previous_files = current_files
        time.sleep(30)  


if __name__ == "__main__":
    main() 

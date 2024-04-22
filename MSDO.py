import os

downloads_dir = os.path.join(os.path.expanduser("~"), "Downloads")

# List all files in the Downloads directory
files = os.listdir(downloads_dir)

for file in files:
    print(file)

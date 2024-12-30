"""
Main script for organizing files by type
"""

import os
from file_types import EXTENSION_MAP
from file_utils import create_directories, move_file

def organize_files(directory):
    # Get the absolute path
    directory = os.path.abspath(directory)
    
    # Create necessary directories
    create_directories(directory, set(EXTENSION_MAP.values()))
    
    # Organize files
    for filename in os.listdir(directory):
        # Skip if it's a directory
        if os.path.isdir(os.path.join(directory, filename)):
            continue
            
        # Get the file extension
        file_ext = os.path.splitext(filename)[1].lower()
        
        # Skip if no extension or not in our map
        if not file_ext or file_ext not in EXTENSION_MAP:
            continue
            
        # Source and destination paths
        source = os.path.join(directory, filename)
        dest_folder = os.path.join(directory, EXTENSION_MAP[file_ext])
        destination = os.path.join(dest_folder, filename)
        
        # Move the file
        move_file(source, destination)

if __name__ == "__main__":
    file_path = r"E:/e drive"
# Ensure the directory exists before writing
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    organize_files(file_path)
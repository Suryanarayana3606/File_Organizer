"""
Utility functions for file operations
"""

import os
import shutil

def create_directories(base_dir, folders):
    """Create directories if they don't exist"""
    for folder in folders:
        folder_path = os.path.join(base_dir, folder)
        os.makedirs(folder_path, exist_ok=True)

def move_file(source, destination):
    """Move a file and handle errors"""
    try:
        shutil.move(source, destination)
        filename = os.path.basename(source)
        folder = os.path.basename(os.path.dirname(destination))
        print(f"Moved {filename} to {folder}/")
        return True
    except Exception as e:
        print(f"Error moving {os.path.basename(source)}: {str(e)}")
        return False
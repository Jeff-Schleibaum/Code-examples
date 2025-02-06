# Jeff Schleibaum automation Project
"""
The program defines file categories based on their extensions (e.g., images, documents, videos).
It scans a folder and retrieves a list of files while ignoring subfolders.
It handles errors if the folder does not exist.
"""

import os
import shutil

FILE_CATEGORIES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
    "Documents": [".pdf", ".docx", ".txt", ".xlsx", ".pptx"],
    "videos": [",mp4", ".mov", ".avi", ".mkv"],
    "Audio": [".mp3", ".wav", ".aac"],
    "Archives": [".zip", ".rar", ".tar", ".gz"],
    "Others": []
}


def get_files(folder_path):
    """Returns a list of files in the given folder."""
    try:
        files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
        return files
    except FileNotFoundError:
        print("Error: The folder does not exist.")
        return []


if __name__ == "__main__":
    folder = input("Enter the path of the folder to organize: ")
    files = get_files(folder)
    print("Files found:", files)
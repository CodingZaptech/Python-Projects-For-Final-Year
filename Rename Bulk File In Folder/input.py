# input.py
# Handles user input for Bulk File Renamer

def get_inputs():
    folder_path = input("Enter folder path: ").strip()
    prefix = input("Enter prefix for files: ").strip()
    return folder_path, prefix

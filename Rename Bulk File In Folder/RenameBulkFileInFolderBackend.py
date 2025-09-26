# RenameBulkFileInFolderBackend.py
# Backend logic to rename all files in folder

import os

class BulkRenamer:
    def rename_files(self, folder_path: str, prefix: str):
        files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
        for i, file in enumerate(files, start=1):
            ext = os.path.splitext(file)[1]
            new_name = f"{prefix}_{i}{ext}"
            os.rename(os.path.join(folder_path, file), os.path.join(folder_path, new_name))
        print(f"{len(files)} files renamed successfully!")

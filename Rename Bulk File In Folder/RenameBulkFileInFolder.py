# RenameBulkFileInFolder.py
# Main runner for bulk file renamer

from RenameBulkFileInFolderBackend import BulkRenamer
import input

def main():
    folder_path, prefix = input.get_inputs()
    BulkRenamer().rename_files(folder_path, prefix)

if __name__ == "__main__":
    main()

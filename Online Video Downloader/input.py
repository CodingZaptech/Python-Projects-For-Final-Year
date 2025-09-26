# input.py
# Handles user input for Online Video Downloader

def get_inputs():
    url = input("Enter YouTube video URL: ").strip()
    path = input("Enter download folder path (leave blank for current folder): ").strip()
    if path == "":
        path = "."
    return url, path

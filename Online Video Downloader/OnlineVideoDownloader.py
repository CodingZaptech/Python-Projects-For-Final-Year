# OnlineVideoDownloader.py
# Main runner for Online Video Downloader

from OnlineVideoDownloaderBackend import VideoDownloader
import input

def main():
    url, path = input.get_inputs()
    downloader = VideoDownloader()
    downloader.download_video(url, path)

if __name__ == "__main__":
    main()

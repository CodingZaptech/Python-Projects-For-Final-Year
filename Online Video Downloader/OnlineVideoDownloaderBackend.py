# OnlineVideoDownloaderBackend.py
# Backend logic for Online Video Downloader using pytube

from pytube import YouTube
import os

class VideoDownloader:
    def download_video(self, url: str, path: str):
        """Download YouTube video to specified path."""
        try:
            yt = YouTube(url)
            print(f"Title: {yt.title}")
            stream = yt.streams.get_highest_resolution()
            stream.download(output_path=path)
            print(f"Video downloaded successfully at {os.path.join(path, stream.default_filename)}")
        except Exception as e:
            print(f"Error downloading video: {e}")

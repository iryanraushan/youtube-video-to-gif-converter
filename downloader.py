# downloader.py
from pytube import YouTube

def download_video(url, output_path):
    yt = YouTube(url)
    stream = yt.streams.filter(file_extension='mp4').first()
    output_file = stream.download(output_path)
    return output_file

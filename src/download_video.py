# from pytube import YouTube
from pytubefix import YouTube
from pytubefix.cli import on_progress
import os
import re

def download(link):
    SAVE_PATH = "/Users/mac/Desktop/assignment/mvp_assignment_python_dev/video_summarizer/original_videos"
    try: 
        yt = YouTube(link)
        ys = yt.streams.get_highest_resolution()
        title = cleaned_text = re.sub(r'[^a-zA-Z]', '', yt.streams.first().default_filename)
        ys.download(output_path=SAVE_PATH, filename=f"{title}.mp4")
    except Exception as e: 
        print(str(e))

    return os.path.join(SAVE_PATH, f"{title}.mp4"), f"{title}.mp4"

# if __name__ == "__main__":  
#     video_path = download("https://www.youtube.com/watch?v=n0fW88BMBno")
#     print(video_path)
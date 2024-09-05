from moviepy.editor import *
from moviepy.video.fx import fadein, fadeout
import random

def gen_video(audio_files, video_name):
    video_files = []
    for i, audio_path in enumerate(audio_files):
        image_path = f"generated_images/image_{i+1}.jpg"
        video_path = f"generated_videos{i}.mp4"

        audio = AudioFileClip(audio_path)
        image = ImageClip(image_path, duration=audio.duration)
        video = image.set_audio(audio)
        video.fps = 24 

        video_files.append(video)

    # Add transitions between the video clips
    final_video = video_files[0]
    for i in range(1, len(video_files)):
        transition_duration = 2.0
        transition = fadein.fadein(video_files[i], transition_duration) if i > 0 else video_files[i]
        final_video = concatenate_videoclips([final_video, transition], method="compose")

    final_video.fps = 24

    output_video_path = f"{video_name}_short.mp4"

    final_video.write_videofile(output_video_path, codec="libx264", audio_codec='aac')



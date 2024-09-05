from moviepy.editor import VideoFileClip, concatenate_videoclips
from moviepy.editor import *
from moviepy.video.fx import fadein, fadeout
import os

def generate_highlight(filename):
    directory_path = '/Users/mac/Desktop/assignment/mvp_assignment_python_dev/video_summarizer/highlight_clips'

    all_files = os.listdir(directory_path)

    filtered_files = [file for file in all_files if file.endswith('.mp4')]

    clip_list = []
    for file in filtered_files:
        clip_list.append(VideoFileClip(os.path.join(directory_path, file)))

    final_video = clip_list[0]
    for i in range(1, len(clip_list)):
        transition_duration = 2.0
        transition = fadein.fadein(clip_list[i], transition_duration) if i > 0 else clip_list[i]
        final_video = concatenate_videoclips([final_video, transition], method="compose")

    final_video.fps = 24

    output_video_path = f"highlights/{filename.replace(".mp4", "")}_highlights.mp4"

    final_video.write_videofile(output_video_path, codec="libx264", audio_codec='aac')

    return output_video_path
# from faster_whisper import WhisperModel
import assemblyai as aai
# import ffmpeg
import sys
import pysrt
from moviepy.editor import VideoFileClip, TextClip, CompositeVideoClip
import os
from dotenv import load_dotenv

load_dotenv()

def srt_generator(video_file):
    aai.settings.api_key = os.getenv("ASSEMBLYAI_API_KEY")

    transcriber = aai.Transcriber()
    transcript = transcriber.transcribe(video_file)

    srt = transcript.export_subtitles_srt()

    with open("subtitle_example.srt", "w") as f:
        f.write(srt)

# def time_to_seconds(time_obj):
#     return time_obj.hours * 3600 + time_obj.minutes * 60 + time_obj.seconds + time_obj.milliseconds / 1000


# def create_subtitle_clips(subtitles, videosize,fontsize=24, font='Arial', color='yellow', debug = False):
#     subtitle_clips = []

#     for subtitle in subtitles:
#         start_time = time_to_seconds(subtitle.start)
#         end_time = time_to_seconds(subtitle.end)
#         duration = end_time - start_time

#         video_width, video_height = videosize
        
#         text_clip = TextClip(subtitle.text, fontsize=fontsize, font=font, color=color, bg_color = 'black',size=(video_width*3/4, None), method='caption').set_start(start_time).set_duration(duration)
#         subtitle_x_position = 'center'
#         subtitle_y_position = video_height* 4 / 5 

#         text_position = (subtitle_x_position, subtitle_y_position)                    
#         subtitle_clips.append(text_clip.set_position(text_position))

#     return subtitle_clips


# srt_generator("/Users/mac/Desktop/assignment/mvp_assignment_python_dev/video_summarizer/highlights/Game.mp4_highlights.mp4")

# srtfilename = "/Users/mac/Desktop/assignment/mvp_assignment_python_dev/video_summarizer/subtitle_example.srt"
# mp4filename = "/Users/mac/Desktop/assignment/mvp_assignment_python_dev/video_summarizer/highlights/Game_highlights.mp4"
# video = VideoFileClip(mp4filename)
# subtitles = pysrt.open(srtfilename)
# begin,end= mp4filename.split(".mp4")
# output_video_file = begin+'_subtitled'+".mp4"

# print ("Output file name: ",output_video_file)

# subtitle_clips = create_subtitle_clips(subtitles,video.size)

# final_video = CompositeVideoClip([video] + subtitle_clips)

# final_video.write_videofile(output_video_file)

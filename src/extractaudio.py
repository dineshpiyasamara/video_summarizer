import moviepy.editor as mp

def extract_audio(video_path, audio_name):
    try:
        clip = mp.VideoFileClip(video_path)
        clip.audio.write_audiofile(f"{audio_name}.wav")
        print("Audio extracted")
    except Exception as e:
        print(f"Error: {e}")
    
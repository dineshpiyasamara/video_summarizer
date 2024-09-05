import os

def clear_short_clips():
    directory_path = '/Users/mac/Desktop/assignment/mvp_assignment_python_dev/video_summarizer/highlight_clips'

    all_files = os.listdir(directory_path)

    for file_name in all_files:
        file_path = os.path.join(directory_path, file_name)
        if os.path.isfile(file_path):
            os.remove(file_path)

    print("All files have been removed.")
from flask import Flask, jsonify, request
from src.transcript_generator import generate_transcript
from src.summarizer import get_summary
from src.sentence_tokenizer import sent_tokenizer
from src.download_video import download
from src.extractaudio import extract_audio
from src.make_highlight_chunks import extract_chunks
from src.final_concat_clips import generate_highlight
from src.clear_directory import clear_short_clips
from src.subtitle_generator import srt_generator

app = Flask(__name__)

@app.route("/api/test", methods=['GET'])
def test_api():
    return "Working..."

@app.route("/api/video_summarizer", methods=['POST'])
def article_generator():
    try:
        data = request.get_json()
        url = data["url"]

        print(url)

        video_path, filename = download(url)

        extract_audio(video_path, "audio")

        extract_chunks(video_path)

        highlight_file = generate_highlight(filename)

        extract_audio(highlight_file, "audio_short")

        srt_generator(highlight_file)

        # print(language)
        # print(segments)

        clear_short_clips()

        return {
            "result": highlight_file,
            "status": "success"
        }
    except Exception as e:
        return {
            "result": str(e),
            "status": "failed"
        }


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002, debug=True)
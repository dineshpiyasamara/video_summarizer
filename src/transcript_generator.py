from youtube_transcript_api import YouTubeTranscriptApi
from bs4 import BeautifulSoup
import requests
from pytube import extract

def generate_transcript(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text)

    link = soup.find_all(name="title")[0]
    title = str(link)
    title = title.replace('<title>', '').replace('</title>', '')

    id=extract.video_id(url)
    srt = YouTubeTranscriptApi.get_transcript(id)
    transcript = ''
    for i in srt:
        transcript = transcript + " " + i['text']
    return transcript, title
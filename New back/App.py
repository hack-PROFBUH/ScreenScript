from flask import Flask, request, render_template
import os
import youtube_dl
from google.cloud import speech_v1p1beta1 as speech

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        video_url = request.form['video_url']

        ydl_opts = {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'wav',
                'preferredquality': '192',
            }],
            'outtmpl': 'audio.wav',
        }

        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([video_url])

        return "Video downloaded and converted to audio successfully"
    else:
        return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)

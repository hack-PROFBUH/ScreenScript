from moviepy.editor import VideoFileClip

def extract_audio(video_path):
    video = VideoFileClip(video_path)
    audio = video.audio
    audio_path = "audio.wav"
    audio.write_audiofile(audio_path)
    return audio_path


"""
from moviepy.editor import VideoFileClip

video = VideoFileClip("video.mp4")
audio = video.audio
audio.write_audiofile("audio.mp3")

"""
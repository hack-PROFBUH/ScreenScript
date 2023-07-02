import speech_recognition as sr

r = sr.Recognizer()
file_path = "audio11.wav"

with sr.AudioFile(file_path) as source:
    audio_text = r.record(source)

text = r.recognize_google(audio_text, language="ru-RU")
print(text)

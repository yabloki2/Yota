import speech_recognition
from yota import main

def listen(txt):
         with speech_recognition.Microphone() as micro:
             sr.adjust_for_ambient_noise(source = micro, duration = 0.5)
             audio = sr.listen(source = micro)
             txt = sr.recognize_google(audio_data = audio, language = 'ru-RU').lower()
             main(txt)
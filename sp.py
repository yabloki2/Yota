import time
import torch
import sounddevice as sd

def speak(txt):
    text = txt
    language = 'ru'
    model_id = 'ru_v3'
    speaker = 'xenia' # aidar, kseniya, xenia, random
    put_accent = True
    put_yoo = True
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    sample_rate = 48000


    model, _ = torch.hub.load(repo_or_dir = 'snakers4/silero-models', model = 'silero_tts', language = language, speaker = model_id)
    model.to(device)
    audio = model.apply_tts(text = text, speaker = speaker, sample_rate = sample_rate, put_accent = put_accent, put_yo = put_yoo)

    sd.play(audio, sample_rate)
    time.sleep(len(audio) / sample_rate)
    sd.stop()
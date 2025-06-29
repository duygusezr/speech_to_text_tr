import speech_recognition as sr
from gtts import gTTS
import simpleaudio as sa
import os

language = 'tr'
lang = 'tr-TR'

def speak_text(text):
    tts = gTTS(text=text, lang=language)
    filename = "temp_voice.wav"
    tts.save("temp_voice.mp3")
    os.system("ffmpeg -y -i temp_voice.mp3 " + filename)  # MP3 → WAV
    wave_obj = sa.WaveObject.from_wave_file(filename)
    play_obj = wave_obj.play()
    play_obj.wait_done()
    os.remove("temp_voice.mp3")
    os.remove(filename)

def listen_and_recognize():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎙️ Konuşun lütfen...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        print("📝 Ses metne çevriliyor...")
        text = recognizer.recognize_google(audio, language=lang)
        print("🔊 Anlaşılan metin:", text)
        speak_text(text)

    except sr.UnknownValueError:
        print("🤖 Anlaşılamadı.")
    except sr.RequestError as e:
        print(f"❌ Google API hatası: {e}")

listen_and_recognize()

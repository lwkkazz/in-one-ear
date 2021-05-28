import os, time

os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"

from gtts import gTTS
from pygame import mixer

#TODO Adicionar
language = 'pt-br'
mixer.init(devicename='CABLE Input (VB-Audio Virtual Cable)')


def create_audio(text):
    audio = gTTS(text=text, lang=language, slow=False)
    audio.save("text.mp3")


def play_audio(text):
    mixer.music.unload()
    create_audio(text)
    mixer.music.load("text.mp3")
    mixer.music.play()


def clear():
    mixer.music.unload()
    mixer.quit()
    if os.path.isfile('text.mp3'):
        os.remove('text.mp3')


def loop():
    while True:
        text = input("Text To Mic: ")

        if text == 'exit now':
            print("Exiting...")
            clear()
            time.sleep(2)
            break

        play_audio(text)



loop()

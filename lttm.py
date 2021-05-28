from gtts import gTTS
from pygame import mixer #Playing sound

import os

language = 'pt-br'


def create_audio(text):
    audio = gTTS(text=text, lang=language, slow=False)
    audio.save("text.mp3")


def play_audio(text):
    mixer.init(devicename='CABLE Input (VB-Audio Virtual Cable)')
    mixer.music.unload()
    create_audio(text)
    mixer.music.load("text.mp3") #Load the mp3
    mixer.music.play()

def clear():
    os.remove('text.mp3')
    # os.unlink()

def loop():
    while True:
        text = input("Texto: ")

        if text == 'exit now':
            print("Saindo...")
            clear()
            input('')
            break

        play_audio(text)




loop()

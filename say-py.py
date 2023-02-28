import click
from gtts import gTTS
from playsound import *
import os
import translators as ts
from langdetect import detect, DetectorFactory
from logging import *


@click.command()
@click.option('-p', '--phrase', type=str, help='Phrase or text to say out loud')
def say(phrase):
    os_language = (os.getenv('LANG').split('_'))[0]
    print("Language detected is: ",os_language)



    def say(IN):
        gTTS(text=IN, lang=os_language, slow=False).save("sound/output.wav")
        playsound('sound/output.wav')
        os.remove('sound/output.wav')


    say(phrase)
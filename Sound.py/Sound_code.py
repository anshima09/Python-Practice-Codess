#pip install gtts (google text to speech service)
from gtts import gTTS
import os
f=open('anshima.txt')
x=f.read()
language='en'
audio=gTTS(text=x,lang=language,slow=False)
audio.save("anshima.wav")
os.system("anshima.wav")

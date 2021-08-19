#text in code box (working)

from gtts import gTTS
from playsound import playsound

audio = 'speech.mp3'
language = 'en'
sp = gTTS(text = "HI! My name is Isha Mishra",lang = language, slow=False)

sp.save(audio)
playsound(audio)
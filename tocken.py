from gtts import gTTS
from playsound import playsound
tocken = input("Enter the Tocken Number")
txt = "ടോക്കൺ നമ്പർ" + tocken
ob = gTTS(txt,lang = "ml")
ob.save("Tocken.mp3")
playsound("Tocken.mp3")
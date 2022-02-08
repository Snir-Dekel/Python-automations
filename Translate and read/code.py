import pyperclip
import pyttsx3
from googletrans import Translator

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\MSTTS_V110_heIL_Asaf")
translator = Translator()
while True:
    pyperclip.waitForNewPaste()
    hebrew_translated_text = translator.translate(pyperclip.paste(), dest='he').text
    print(hebrew_translated_text)
    engine.say(hebrew_translated_text)
    engine.runAndWait()
    engine.stop()

import pytesseract.pytesseract
import pyttsx4
import speech_recognition as sr
from PIL import Image
from pytesseract import image_to_string

pytesseract.pytesseract.tesseract_cmd = r'D:\Programming\Projects\PyCharmProjects\Tesseract\tesseract'

record = sr.Recognizer()
engine = pyttsx4.init()

with sr.Microphone(device_index=0) as source:
    while True:
        try:
            print("Speak...")
            audio = record.listen(source)
            result = record.recognize_google(audio)
            result = result.lower()

            if result == 'write file':
                text = image_to_string(Image.open('photo.png'))
                file = open('image_text.txt', 'w+')
                print(text, file=file)
                file.close()
            elif result == 'read file':
                file = open('image_text.txt', 'r+')
                text = file.read()
                print(text)
                engine.say(text)
                engine.runAndWait()
            elif result == 'exit':
                break
            else:
                print('Sorry, I don`t have such command :( \n Try something else...')
        except sr.exceptions.UnknownValueError:
            print('Sorry, I don`t understand you, try again...')
        except Exception:
            print('Something went wrong. Try again...')


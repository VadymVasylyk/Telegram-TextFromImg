import pytesseract.pytesseract
from PIL import Image
from pytesseract import image_to_string
import telebot

pytesseract.pytesseract.tesseract_cmd = r'D:\Programming\Projects\PyCharmProjects\Tesseract\tesseract'

bot = telebot.TeleBot('6869843521:AAGDK04usgroDTTa8YcwbIMyE9X1zumJl2Q')


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Send photo, please...')


@bot.message_handler(content_types=['photo'])
def photo(message):
    try:
        file_info = bot.get_file(message.photo[-1].file_id)
        file = bot.download_file(file_info.file_path)
        ph = open('image.png', 'wb')
        ph.write(file)
        ph.close()
        text = image_to_string(Image.open('image.png'))
        bot.send_message(message.chat.id, text)
    except Exception:
        bot.send_message(message.chat.id, "Sorry, I can`t read this")


bot.polling(none_stop=True)
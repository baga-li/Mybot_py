


import telebot

from translate import Translator

import os

bot = telebot.TeleBot('907078988:AAHvDq3NIRGfJHsrYy3eAkHErunWBN7cZpI')



translator= Translator(to_lang="zh")



@bot.message_handler(commands=['start'])



def start_message(message):

    bot.send_message(message.chat.id, "Do you want to translate?" )


@bot.message_handler(content_types=["text"])

def send_text(message):
    word = message.text
    translation = translator.translate(word)
    bot.send_message(message.chat.id, translation )


if __name__ == '__main__':
    bot.polling(none_stop=True)



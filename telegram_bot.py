from token_keys import key_telegram
import telebot

bot = telebot.TeleBot(key_telegram)


@bot.message_handler(commands=['start'])
def get_text_messages(message):
    bot.send_message(message.from_user.id, "Я помогу тебе скачать видео с Youtube. \n "
                                           "/help - для получение справки \n"
                                           "/download - для скачивания видео")


@bot.message_handler(commands=['help'])
def get_text_messages(message):
    bot.send_message(message.from_user.id, "Текст справки")  # FIX ME


bot.polling(none_stop=True, interval=0)

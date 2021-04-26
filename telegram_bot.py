from token_keys import key_telegram
import telebot
import pytube

bot = telebot.TeleBot(key_telegram)


def get_formats(yt):
    str_format = 'Выберите качество видео:\n'
    num = 1
    formats = yt.streams.order_by ('resolution').filter (mime_type="video/mp4")
    for format_ in formats:
        str_format = str(num)+': ' + str_format + str(format_) + '\n'
        num += 1
    return str_format

def take(n, seq):
    result = []
    try:
        for i in range(n):
            result.append(next(seq))
    except StopIteration:
        pass
    return result


@bot.message_handler(commands=['start'])
def get_text_messages(message):
    bot.send_message(message.from_user.id, "Я помогу тебе скачать видео с Youtube. \n "
                                           "Пришли ссылку")


@bot.message_handler(commands=['help'])
def get_text_messages(message):
    bot.send_message(message.from_user.id, "Текст справки")  # FIX ME


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    yt = None
    try:
        yt = pytube.YouTube(message.text)
    except pytube.exceptions.RegexMatchError:
        bot.send_message(message.from_user.id, "Не могу скачать данный фаил. Проверьте ссылку")
    if yt is not None:
        pass
        #print(yt.streams[0].desc())
        #bot.send_message(message.from_user.id, get_formats(yt)+'Пришлите номер выбранного фаила')



bot.polling(none_stop=True, interval=0)

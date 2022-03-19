import telebot
import pytube
import os

bot = telebot.TeleBot('YOUR_TOKEN')
video = None


def create_keyboard(yt):
    buttons = []
    keyboard = telebot.types.InlineKeyboardMarkup(row_width=1)
    i = 0
    for stream in yt.streams.filter(progressive='True'):
        typ = str(stream).split(' ')[2].split('=')[1][1:-1]
        quality = str(stream).split(' ')[3].split('=')[1][1:-1]

        text_but = 'Тип: {}, Качество: {}'.format(typ, quality)
        buttons.append(telebot.types.InlineKeyboardButton(text=text_but, callback_data=str(i)))
        i += 1
    keyboard.add(*buttons)
    return keyboard


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
    filters = yt.streams.filter(progressive=True, file_extension='mp4')

    # download the highest quality video
    filters.get_highest_resolution().download(filename='name.mp4')
    bot.send_video(callback_query.from_user.id, video)
    video.close()
    os.remove('name.mp4')
    # if yt is not None:
    #     keyboard = create_keyboard(yt)
    #     global video
    #     video = yt
    #     bot.send_message(message.from_user.id, 'Выберите формат для загрузки', reply_markup=keyboard)


@bot.callback_query_handler(func=lambda x: True)
def callback_handler(callback_query):
    global video
    bot.send_message(callback_query.from_user.id, "Подождите, началась загрузка...")
    video = open(video.streams.filter(progressive='True')[int(callback_query.data)].download(
                 filename='{}'.format(callback_query.from_user.id)), 'rb')
    bot.send_video(callback_query.from_user.id, video)
    video.close()
    os.remove('{}.mp4'.format(callback_query.from_user.id))


bot.polling(none_stop=True, interval=0)

import telebot
from telebot import types
from config import bot


@bot.message_handler(commands=['start'])
def send_welcome(message):

    keyboard = types.InlineKeyboardMarkup()

    button1 = types.InlineKeyboardButton("Наша аудитория и цифры 📈", callback_data='button1')
    button2 = types.InlineKeyboardButton("Условия сотрудничества и форматы 💸", callback_data='button2')
    button3 = types.InlineKeyboardButton("Предложить новость ✍🏻", callback_data='button3')

    keyboard.add(button1)
    keyboard.add(button2)
    keyboard.add(button3)

    bot.send_message(message.chat.id,
                     "*Привет! Я бот канала Spot 👋 Я расскажу вам о наших условиях сотрудничества и форматах. Также мне можно присылать любые интересные новости про город!*",
                     parse_mode='Markdown', reply_markup=keyboard)


# Обработчик нажатий на кнопки
@bot.callback_query_handler(func=lambda call: True)
def handle_buttons(call):
    if call.data == 'button1':
        bot.send_message(call.message.chat.id, """ В медиа-проекте SPOT вы можете рассказать о своем бизнесе или услугах. Мы делаем рекламу ресторанов, отелей, салонов красоты, одежды, мастеров, и любых других направлений, которые отражают миссию нашего проекта - помогать развивать и рассказывать о бизнесе на юге. 

Наша аудитория:
Instagram — 12.000 человек
Telegram - 3500 человек""")
    elif call.data == 'button2':
        photo_path1 = r'C:\Users\1\Desktop\pet proj\pythonProject1\photo_2024-12-09_13-07-26.jpg'
        photo_path2 = r'C:\Users\1\Desktop\pet proj\pythonProject1\photo_2024-12-09_13-07-27.jpg'

        with open(photo_path1, 'rb') as photo:
            bot.send_photo(call.message.chat.id, photo)

        with open(photo_path2, 'rb') as phot:
            bot.send_photo(call.message.chat.id, phot)

    elif call.data == 'button3':
        bot.send_message(call.message.chat.id,
                         "Сюда вы можете отправить любые интересные новости про город, фото, полезные знания, идеи и предложения.")
        bot.send_message(call.message.chat.id,
                         'Для этого необходимо отправить @wownusya фото или видео файлом, краткий текст и необходимые ссылки. ')


bot.polling(none_stop=True)

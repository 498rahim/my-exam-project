import telebot
import os
bot = telebot.TeleBot(os.environ.get('BOT_TOKEN'))

def start_button_markup():
    reply_markup = telebot.types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    reply_markup.row(
        telebot.types.InlineKeyboardButton(text='🛍Buyurtma berish')
    )
    reply_markup.add(*[
        '💸Cashback',
        '🎉Tadbirlar',
        '✍Fikr bildirish',
        'ℹMa\'lumot'
    ])
    reply_markup.row(
        telebot.types.InlineKeyboardButton(text='⚙Sozlamalar')
    )
    return reply_markup


@bot.message_handler(commands=['start'])
def start_message(message):
    info = f"Assalomu alykum {message.from_user.first_name}!\n\nLES AILES buyurtma botga xush kelibsiz!" \
           f"\nBirga buyurtma beramizmi?😃"
    bot.send_message(message.from_user.id, info, reply_markup=start_button_markup())



@bot.message_handler(func=lambda m: True)
def echo_message(message):
    if message.text == '🛍Buyurtma berish':
        text = "Buyurtmani o'zingiz olib keting, yoki yetkazib berishni tanlang"
        reply_markup = telebot.types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
        reply_markup.add(*[
            '🚘Yetkazib berish',
            '🏃Olib kelish'
        ])
        reply_markup.row(telebot.types.InlineKeyboardButton(text='⬅Orqaga'))
        bot.send_message(message.from_user.id, text, reply_markup=reply_markup)

    elif message.text == '⬅Orqaga':
        text = "Quyidagilardan birini tanlang:"
        bot.send_message(message.from_user.id, text, reply_markup=start_button_markup())

    elif message.text == '🏃Olib kelish':
        text = "Buyurtma berganingizdan so'ng tayyor bo'lgach olib ketishingiz mumkin!"
        bot.send_message(message.from_user.id, text)

    elif message.text == '🚘Yetkazib berish':
        text = "Buyurtmangizni qayerga yetkazib berish kerak🚙?" \
               "\nAgar joylashuv manzilingizni 📍 yuborsangiz, sizga eng yaqin " \
               "\n filialni va yetkazib berish xarajatlarini aniqlaymiz 💸"
        reply_markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
        reply_markup.row(telebot.types.InlineKeyboardButton(text='Eng yaqin shoxobchani aniqlash'))
        reply_markup.row(telebot.types.InlineKeyboardButton(text='⬅Orqaga'))
        bot.send_message(message.from_user.id, text, reply_markup=reply_markup)

    elif message.text == 'Eng yaqin shoxobchani aniqlash':
        text = "Joylashuv manzilingizni 📍 jo'nating iltimos 🙏 \n" \
               "va biz sizga yordam beramiz"
        bot.send_message(message.from_user.id, text)

    elif message.text == '✅Tasdiqlash':
        text = "10:00 - 22:00 - 1 kmgacha bo'lgan buyurtmalar yetkazish narxi 5000 so'm\n\n" \
               "10:00 - 22:00 - 3 kmgacha 9000 so'm, keyingi har km uchun 1000 so'm Toshkent shahri bo'ylab!"
        text_1 = "Nimadan boshlaymiz?"
        reply_markup = telebot.types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
        reply_markup.add(*[
            '🛒Savat', '🚙Buyurtma berish',
            '🍅Setlar', '🍔Burgerlar',
            '🌯Lesterlar', '🌭Longer/Hot-dog',
            '🍗Tovuqcha', '🍟Sneklar'
        ])
        reply_markup.row(telebot.types.InlineKeyboardButton(text='⬅Orqaga'))
        bot.send_message(message.from_user.id, [text, text_1], reply_markup=reply_markup)



@bot.message_handler(content_types=['location'])
def location_message(message):
    text = f"Sizning manzilingiz: {message.location}\n\n" \
           f"Joylashuv noto'g'rimi?\nQayta jo'nating📍"
    reply_markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    reply_markup.row(telebot.types.InlineKeyboardButton(text='Joylashuvni qayta jo\'natish 📍'))
    reply_markup.row(telebot.types.InlineKeyboardButton(text='✅Tasdiqlash'))
    reply_markup.row(telebot.types.InlineKeyboardButton(text='⬅Orqaga'))
    bot.send_message(message.from_user.id, text, reply_markup=reply_markup)




bot.polling(none_stop=True)
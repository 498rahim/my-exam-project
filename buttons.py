from telebot.types import ReplyKeyboardMarkup, KeyboardButton
import telebot


def home_page_button():
    reply = ReplyKeyboardMarkup(True, row_width=2)
    reply.row('🛍 Buyurtmalarim')
    cashback = KeyboardButton(text='💸Cashback')
    event = KeyboardButton(text='🎉Tadbirlar')
    thought = KeyboardButton(text='✍️Fikr bildirish')
    info = KeyboardButton(text='📝 Malumot')
    reply.add(cashback, event, thought, info)
    return reply


def delivery():
    reply_markup = telebot.types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    reply_markup.add(*[
        '🚘Yetkazib berish',
        '🏃Olib kelish'
    ])
    reply_markup.row(telebot.types.KeyboardButton(text='⬅Orqaga'))
    return reply_markup


# @bot.message_handler(content_types=['location'])
# def location_message(message):
#     reply_markup = telebot.types.ReplyKeyboardMarkup(True)
#     reply_markup.row(telebot.types.KeyboardButton(text='Joylashuvni qayta jo\'natish 📍'))
#     reply_markup.row(telebot.types.KeyboardButton(text='✅Tasdiqlash'))
#     reply_markup.row(telebot.types.KeyboardButton(text='⬅Orqaga'))
#     bot.send_message(message.from_user.id, text.LOCATION, reply_markup=reply_markup)
#     return location_message
def over_page():
    reply_markup = telebot.types.ReplyKeyboardMarkup(True, row_width=2)
    buttons = ['🛒Savat', '🚘Buyurtma berish', '🍱Setlar', '🍔Burgerlar', '🌯Lesterlar', '🌭Longer/Hot-dog',
               '🍗Tovuqcha', '🍟Sneklar', '⬅Orqaga']
    reply_markup.add(*[button for button in buttons])
    return reply_markup

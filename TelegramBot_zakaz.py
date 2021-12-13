from buttons import home_page_button, delivery, over_page
from text_info import TEXT
import telebot
import os

# import json
bot = telebot.TeleBot(os.environ.get("BOT_TOKEN"))
Text = TEXT


@bot.message_handler(commands=['start'])
def start_func(message):
    bot.send_message(message.from_user.id,
                     'Juda yaxshi birgalikda Buyurtma beramiz😄',
                     reply_markup=home_page_button()
                     )


@bot.message_handler(func=lambda m: True)
def router_message(message):
    if message.text == '🛍 Buyurtmalarim':
        bot.send_message(message.from_user.id, Text.BUY, reply_markup=delivery())
    if message.text == '🚘Yetkazib berish':
        reply_markup = telebot.types.ReplyKeyboardMarkup(True)
        reply_markup.row(telebot.types.KeyboardButton(text='⬅Orqaga'))
        bot.send_message(message.from_user.id, Text.LOCATION, reply_markup=reply_markup)
    if message.text == '🏃Olib kelish':
        reply_markup = telebot.types.ReplyKeyboardMarkup(True)
        reply_markup.row("⬅Orqaga")
        bot.send_message(message.from_user.id,
                         Text.dear_user,
                         reply_markup=reply_markup
                         )
    if message.text == '✅Tasdiqlash':
        bot.send_message(message.from_user.id, Text.DELIVERY_AMOUNT, reply_markup=over_page())
    if message.text == '⬅Orqaga':
        bot.send_message(message.from_user.id,
                         f'{message.from_user.first_name} Siz ortga qaytingiz',
                         reply_markup=home_page_button()
                         )
    if message.text == 'Joylashuvni qayta jo\'natish 📍':
        bot.send_message(message.from_user.id,
                         Text.request,
                         reply_markup=delivery().row("Yaqinro'gi"))
    if message.text == "Yaqinrog'i":
        # with open('users.json', 'r') as f:
        #     json.dumps(f)
        #     user = f
        # print(type(user))
        # bot.send_location(message.from_user.id, user)
        pass


@bot.message_handler(content_types=['location'])
def location_message(message):
    reply_markup = telebot.types.ReplyKeyboardMarkup(True)
    reply_markup.row(telebot.types.KeyboardButton(text='Joylashuvni qayta jo\'natish 📍'))
    reply_markup.row(telebot.types.KeyboardButton(text='✅Tasdiqlash'))
    reply_markup.row(telebot.types.KeyboardButton(text='⬅Orqaga'))
    bot.send_message(message.from_user.id, Text.LOCATION, reply_markup=reply_markup)
    # print(f'{(message.location)}')
    # my_location = (message.location)
    #
    # with open('location.txt', 'w') as f:
    #     f.write(str(my_location))
    return location_message


bot.polling(none_stop=True)

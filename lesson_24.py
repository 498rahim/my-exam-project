import telebot
from buttons import home_page_button
import os
bot = telebot.TeleBot(os.environ.get("BOT_TOKEN"))

# Text = TEXT

@bot.message_handler(commands=['start'])
def start_func(message):
    bot.send_message(message.from_user.id,
                     'Juda yaxshi birgalikda Buyurtma beramiz?😄',
                     reply_markup=home_page_button(1)
                     )




@bot.message_handler(content_types=['text'])
def router_func(message):
    if message.text == '🛍 Buyurtmalarim':
        bot.send_message(message.from_user.id, 'gg'.BUY, reply_markup=home_page_button(2))
    # if message.text == 'Banana':
    #     text = PRODUCTS.banana_description
    #     image = PRODUCTS.banana_image
    #     bot.send_photo(message.from_user.id, image, text)
    # if message.text == 'Orange':
    #     text = PRODUCTS.orange_description
    #     image = PRODUCTS.orange_image
    #     bot.send_photo(message.from_user.id, image, text)
    # if message.text == 'Mango':
    #     text = PRODUCTS.mango_description
    #     image = PRODUCTS.mango_image
    #     bot.send_photo(message.from_user.id, image, text)
    # if message.text == 'Pineapple':
    #     text = PRODUCTS.pineapple_description
    #     image = PRODUCTS.pineapple_image
    #     bot.send_photo(message.from_user.id, image, text)
    if message.text == 'Back':
        bot.send_message(message.from_user.id,
                         f'{message.from_user.first_name} you backed',
                         reply_markup=home_page_button()
                         )


bot.polling(none_stop=True)

# if 'bro' or 'BRO' or 'Bro' in message.text:
#     bot.send_photo(message.from_user.id, 'https://i.pinimg.com/236x/fc/5b/23/fc5b230894c22df2b9fdacb6e8de7c0d.jpg')

TOKEN = '1203006477:AAE9MPcWxUkInjHMohwFA3J6bPEL136SlEQ'
import telebot
from telebot import types
bot = telebot.TeleBot('1203006477:AAE9MPcWxUkInjHMohwFA3J6bPEL136SlEQ')
keyboard = types.InlineKeyboardMarkup()
key_yes = types.InlineKeyboardButton(text='Понятно', callback_data='but1')  # кнопка «Да»
keyboard.add(key_yes)

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Добрый день. Наше с тобой обучение будет посвящено KPI-показателм.'
                                      ' Незнакомое слово KPI ? '
                                      'Понимаю, в нашем с тобой обучении ты узнаешь много новых терминов,'
                                      ' но все они будут полезными. ', reply_markup=keyboard)
keyboard1= types.InlineKeyboardMarkup()
key_yes1 = types.InlineKeyboardButton(text='Понятно', callback_data='but1')  # кнопка «Да»
keyboard1.add(key_yes1)
@bot.message_handler(commands=['text'])
def next_message(message):
    bot.send_message(message.chat.id, 'Ну и первое определение - это KPI (ки-пи-ай). '
                                      'Очень полезный термин? Знаешь почему?'
                                      ' Потому что этот термин обозначает '
                                      'эффективность работы. ', reply_markup=keyboard1)

@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    if call.data == "but1":
        next_message()



@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text.lower() == 'привет':
        bot.send_message(message.chat.id, 'Привет, мой создатель')
    elif message.text.lower() == 'пока':
        bot.send_message(message.chat.id, 'Прощай, создатель')
    elif message.text.lower() == 'я тебя люблю':
        bot.send_sticker(message.chat.id, 'CAADAgADZgkAAnlc4gmfCor5YbYYRAI')

@bot.message_handler(content_types=['sticker'])
def sticker_id(message):
    print(message)

bot.polling()
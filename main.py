import telebot
from telebot import types

import config

bot = telebot.TeleBot(config.bot_token)

# Обработчик команды /start и добавление кнопок в меню
@bot.message_handler(commands=['start'])
def handle_start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item_hello = types.KeyboardButton("Привет")
    item_help = types.KeyboardButton("Помощь")
    item_menu = types.KeyboardButton("Меню")
    markup.add(item_hello, item_help, item_menu)

    bot.send_message(message.chat.id, "Приветствую! Я твой бот. Чем могу помочь?", reply_markup=markup)

# Обработчик команды /help
@bot.message_handler(commands=['help'])
def handle_help(message):
    bot.send_message(message.chat.id, '<b>Привет!</b> <em>Information</em>', parse_mode='html')

# Обработчик команды /menu и отображение меню
@bot.message_handler(commands=['menu'])
def handle_menu(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item_option1 = types.KeyboardButton("Опция 1")
    item_option2 = types.KeyboardButton("Опция 2")
    item_option3 = types.KeyboardButton("Опция 3")
    markup.add(item_option1, item_option2, item_option3)

    bot.send_message(message.chat.id, "Выберите опцию из меню:", reply_markup=markup)

# Обработчик текстовых сообщений и приветствие по ключевому слову "привет"
@bot.message_handler(func=lambda message: True)
def handle_text(message):
    if message.text.lower() == 'привет':
        bot.send_message(message.chat.id, f'Приветствую тебя, {message.from_user.first_name}')
    elif message.text.lower() == 'меню':
        handle_menu(message)
    else:
        bot.send_message(message.chat.id, f'Я не понимаю твоего сообщения. Если нужна помощь, используй /help.')

# Программа будет постоянно работать, чтобы работал бот
bot.polling(non_stop=True)

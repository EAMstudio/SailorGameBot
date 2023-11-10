"""Телеграм бот. Код написан на основе видео-урока:
https://www.youtube.com/watch?v=-l_CYgBj4IE&list=PL0lO_mIqDDFUev1gp9yEwmwcy8SicqKbt&index=2"""
import telebot

bot = telebot.TeleBot('6974112573:AAHzvYG0nxopjE04J5Q6QYsjWBJw42pGXc4')

# Декоратор для функции. Если пользователь прислал любой текст.
@bot.message_handler()
# Функция
def info(message):
    if message.text.lower() == 'привет':
        bot.send_message(message.chat.id, f'Приветствую тебя, {message.from_user.first_name}')

    bot.send_message(message.chat.id, f'Приветствую тебя, {message.from_user.first_name}')

# Декоратор для функции. То что присылает пользователь
@bot.message_handler(commands=['start'])
# Функция
def main(message):
    # Обращаемся к пользователю
    bot.send_message(message.chat.id, f'Приветствую тебя, {message.from_user.first_name}')

# Декоратор для функции Help
@bot.message_handler(commands=['help'])
# Функция
def main(message):
    # Обращаемся к пользователю
    bot.send_message(message.chat.id, '<b>Привет!</b> <em>Information</em>', parse_mode='html')

# Программа будет постоянно работать, чтобы работал бот
bot.polling(non_stop=True)



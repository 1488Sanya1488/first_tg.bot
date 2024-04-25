import telebot
import webbrowser
from telebot import types
from aiogram import Bot, Dispatcher, executor, types
#from time import sleep
#import requests
#import sqlite3
#import json
#from currency_converter import CurrencyConverter
#bot = telebot.TeleBot('7064426376:AAG77ujGzw4H0J_K1wV2EwER-RQACMpROaE')
# Погода
#API = 'd4eec42b1ebae93c9d2442171be7a91a'
#currency = CurrencyConverter()
#amount = 0



#aiogram



#bot.polling(none_stop=True)


#Валютний конвертер
# @bot.message_handler(commands=['start'])
# def start(message):
#     bot.send_message(message.chat.id, 'Введіть суму, яку хочете конвертувати')
#     bot.register_next_step_handler(message, summa)
#
#
# @bot.message_handler()
# def summa(message):
#     global amount
#     try:
#         amount = int(message.text.strip())
#
#         if amount > 0:
#             markup = types.InlineKeyboardMarkup(row_width=2)
#             btn1 = types.InlineKeyboardButton('USD/EUR', callback_data='USD/EUR')
#             btn2 = types.InlineKeyboardButton('EUR/USD', callback_data='EUR/USD')
#             btn3 = types.InlineKeyboardButton('USD/GBP', callback_data='USD/GBP')
#             btn4 = types.InlineKeyboardButton('Інше', callback_data='else')
#             markup.add(btn1, btn2, btn3, btn4)
#             bot.send_message(message.chat.id, "Виберіть валютну пару", reply_markup=markup)
#         else:
#             bot.send_message(message.chat.id, 'Введіть додатнє число!')
#
#     except ValueError:
#         time.sleep(1)
#         bot.send_message(message.chat.id, 'Будь ласка, введіть число')
#         time.sleep(3)
#         bot.register_next_step_handler(message, summa)
#
#
# @bot.callback_query_handler(lambda call: True)
# def callback(call):
#     global amount
#     if call.data != 'else':
#         values = call.data.split('/')
#         res = currency.convert(amount, values[0], values[1])
#         bot.send_message(call.message.chat.id, f'Вийшло: {round(res, 2)}')
#         bot.register_next_step_handler(call.message, summa)
#     else:
#         bot.send_message(call.message.chat.id, "Введіть валютну пару через /. Наприклад: USD/EUR")
#         bot.register_next_step_handler(call.message, my_currency)
#
#
# def my_currency(message):
#     global values
#     values = message.text.upper()
#     if values == 'STOP':
#         bot.register_next_step_handler(message, summa)
#     else:
#         try:
#             values = message.text.upper().split('/')
#             res = currency.convert(amount, values[0], values[1])
#             bot.send_message(message.chat.id, f'Вийшло: {round(res, 2)}')
#             time.sleep(1)
#             bot.register_next_step_handler(message, summa)
#         except Exception:
#             bot.send_message(message.chat.id, f'Невірне значення валютної пари: {values}, перевірте його правильність')
#             bot.register_next_step_handler(message, my_currency)


#Погода
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Привіт! Це бот для показу погоди, напиши назву міста')
@bot.message_handler(content_types=['text'])
def get_weather(message):
    city = message.text.strip().lower()
    res = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API}&units=metric')
    if res.status_code == 200:
        data = json.loads(res.text)
        weather = data["weather"][0]["main"]
        temp = data["main"]["temp"]
        wind = data["wind"]["speed"]
        pressure = data['main']['pressure']
        wind_deg = data["wind"]['deg']
        dust = data['wind']['gust']
        humidity = data['main']['humidity']

        bot.reply_to(message, f'Погода зараз:\n{temp} градусів\nПогода: {weather}\nВітер: {wind}\nНапрям вітру: {wind_deg}\nТиск: {pressure}\nПорив вітру: {dust}\nВологість: {humidity}')

        image = 'warm.png' if temp > 15.0 else 'cold.png'
        file = open('./' + image, 'rb')
        bot.send_photo(message.chat.id, file)
    else:
        bot.reply_to(message, f'Місто вказано неправильно')


#db
# name = None
#
#
# @bot.message_handler(commands=['start'])
# def start(message):
#     conn = sqlite3.connect('database.sql')
#     cur = conn.cursor()
#
#     cur.execute('CREATE TABLE IF NOT EXISTS users (id int auto_increment primary key, name varchar(50), pass varchar(50))')
#     conn.commit()
#     cur.close()
#     conn.close()
#
#     bot.send_message(message.chat.id, 'створення нового користувача. Введіть ваш логін')
#     bot.register_next_step_handler(message, user_name)
#
#
# def user_name(message):
#     global name
#     name = message.text.strip()
#     bot.send_message(message.chat.id, 'Введіть ваш пароль')
#     bot.register_next_step_handler(message, user_pass)
#
#
# def user_pass(message):
#     password = message.text.strip()
#
#     conn = sqlite3.connect('database.sql')
#     cur = conn.cursor()
#     cur.execute("INSERT INTO users (name, pass) VALUES ('%s', '%s')" % (name, password))
#     conn.commit()
#     cur.close()
#     conn.close()
#
#     markup = telebot.types.InlineKeyboardMarkup()
#     markup.add(telebot.types.InlineKeyboardButton('Users list', callback_data='users'))
#     bot.send_message(message.chat.id, 'Користувач зареєстрований успішно!', reply_markup=markup)
#
#
# @bot.callback_query_handler(func=lambda call: True)
# def callback(call):
#     w = '`'
#     conn = sqlite3.connect('database.sql')
#     cur = conn.cursor()
#     cur.execute("SELECT * FROM users")
#     users = cur.fetchall()
#     conn.close()
#
#     info = ''
#
#     for el in users:
#         info += f'Ім{w}я:  {el[1]}, Пароль:  {el[2]}\n'
#
#     bot.send_message(call.message.chat.id, info)
#
#     cur.close()
#     conn.close()


#huta
# @bot.message_handler(commands=['start'])
# def start(message):
#     markup = types.ReplyKeyboardMarkup()
#     btn1 = types.KeyboardButton('Перейти на сайт')
#     btn2 = types.KeyboardButton('Видалити фото')
#     btn3 = types.KeyboardButton('Змінити текст')
#     markup.row(btn1)
#     markup.row(btn2, btn3)
#     file = open('./img.png', 'rb')
#     bot.send_photo(message.chat.id, file, reply_markup=markup)
#     # bot.send_message(message.chat.id, 'Привіт', reply_markup=markup)
#     bot.register_next_step_handler(message, on_click)
#
# def on_click(message):
#     if message.text == 'Перейти на сайт':
#         bot.send_message(message.chat.id, 'https://google.com')
#     elif message.text == 'Видалити фото':
#         bot.send_message(message.chat.id, 'wadsadawdaw')
#
# @bot.message_handler(content_types=['photo'])
# def get_photo(message):
#     markup = types.InlineKeyboardMarkup()
#     btn1 = types.InlineKeyboardButton('Перейти на сайт', url='https://google.com')
#     btn2 = types.InlineKeyboardButton('Видалити фото', callback_data='delete')
#     btn3 = types.InlineKeyboardButton('Змінити текст', callback_data='edit')
#     markup.row(btn1)
#     markup.row(btn2, btn3)
#     bot.reply_to(message, 'Гарне фото!)', reply_markup=markup)
#
#
# @bot.callback_query_handler(func=lambda callback: True)
# def callback_message(callback):
#     if callback.data == 'delete':
#         bot.delete_message(callback.message.chat.id, callback.message.message_id - 1)
#     elif callback.data == 'edit':
#         bot.edit_message_text('Edit text', callback.message.chat.id, callback.message.message_id)
#
# @bot.message_handler(commands=['site', 'website', 'web'])
# def site(message):
#     webbrowser.open('https://www.google.com/search?client=opera-gx&q=погода+богородчани&sourceid=opera&ie=UTF-8&oe=UTF-8')
#
# @bot.message_handler(commands=['help'])
# def main(message):
#     bot.send_message(message.chat.id, '<b>Цей бот покаже</b> <em><u>погоду у вибраній області</u></em>', parse_mode='html')
#
# @bot.message_handler()
# def info(message):
#     if message.text.lower() == 'привіт':
#         bot.send_message(message.chat.id, f'Привіт {message.from_user.first_name}')
#     if message.text.lower() == 'id':
#         bot.reply_to(message, f'ID: {message.from_user.id}')
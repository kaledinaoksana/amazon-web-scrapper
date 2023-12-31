import telebot
from telebot import types
import webbrowser
import settings as s
import sqlite3

TOKEN = s.BOT.token

bot = telebot.TeleBot(TOKEN)
name = ''


@bot.message_handler(commands=['sql'])
def start(message):
    conn = sqlite3.connect('bot.sql')
    cur = conn.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS users (id int auto_increment primary key, name varchar(50), pass varchar(50))')
    conn.commit()
    cur.close()
    conn.close()
    bot.send_message(message.chat.id, text='Привет! Сейчас тебя зарегистрируем! Введи имя: ')
    bot.register_next_step_handler(message, user_name)


def user_name(message):
    global name
    name = message.text.strip()
    bot.send_message(message.chat.id, 'Введите пароль:')
    bot.register_next_step_handler(message, user_pass)


def user_pass(message):
    password = message.text.strip()
    conn = sqlite3.connect('bot.sql')
    cur = conn.cursor()
    cur.execute("INSERT INTO users (name, pass) VALUES ('%s', '%s')" % (name, password))
    conn.commit()
    cur.close()
    conn.close()
    markup = telebot.types.InlineKeyboardMarkup()
    btn = telebot.types.InlineKeyboardButton(text='Список пользователей', callback_data='users')
    markup.add(btn)
    bot.send_message(message.chat.id, 'Ты Зарегистрирован!', reply_markup=markup)


@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    conn = sqlite3.connect('bot.sql')
    cur = conn.cursor()
    cur.execute('SELECT * FROM users')
    users = cur.fetchall()
    info = ''
    for el in users:
        info += f'Name: {el[1]}, PSW: {el[2]} \n'
    cur.close()
    conn.close()
    bot.send_message(call.message.chat.id, info)


@bot.message_handler(commands=['start'])
def main(message):
    markup = types.ReplyKeyboardMarkup()
    btn1 = types.KeyboardButton(text='Go to site')
    btn2 = types.KeyboardButton(text='Delete photo')
    btn3 = types.KeyboardButton(text='Edit photo')
    markup.row(btn1)
    markup.row(btn2, btn3)
    file = open('/Users/oksana_kaledina/Documents/5_PORTFOLIO/PortfolioPython/AmazonWebScrapper/assets/logo.png', 'rb')
    bot.send_photo(message.chat.id, file)
    # bot.reply_to(message, text='Hi!', reply_markup=markup)
    bot.register_next_step_handler(message, on_click)


def on_click(message):
    if message.text == 'go to site':
        bot.send_message(message.chat.id, 'Website is open')
    elif message.text == 'delete':
        bot.send_message(message.chat.id, 'Deleted')


@bot.message_handler(content_types=['photo'])
def get_photo(message):
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton(text='Go to site', url='http://kaledinaoksana.ru')
    btn2 = types.InlineKeyboardButton(text='Delete photo', callback_data='delete')
    btn3 = types.InlineKeyboardButton(text='Edit photo', callback_data='edit')
    markup.row(btn1)
    markup.row(btn2, btn3)
    bot.reply_to(message, text='Cool photo!', reply_markup=markup)


@bot.callback_query_handler(func=lambda call_back: True)
def callback_message(call_back):
    if call_back.data == 'delete':
        bot.delete_message(call_back.message.chat.id, call_back.message.message_id - 1)
    elif call_back.data == 'edit':
        bot.edit_message_text('edit text', call_back.message.chat.id, call_back.message.message_id - 1)


@bot.message_handler(commands=['site', 'website'])
def site(message):
    webbrowser.open('http://kaledinaoksana.ru')


@bot.message_handler(commands=['custom'])
def main(message):
    bot.send_message(message.chat.id, 'Hi!')


@bot.message_handler(commands=['help'])
def main(message):
    bot.send_message(message.chat.id, '<b>Help</b> info!', parse_mode='html')


@bot.message_handler(commands=['message'])
def main(message):
    bot.send_message(message.chat.id, f'Hi {message.from_user.first_name} {message.from_user.last_name}!')


@bot.message_handler()
def info(message):
    if message.text.lower() == 'hi':
        bot.send_message(message.chat.id, f'Hi {message.from_user.first_name} {message.from_user.last_name}!')
    elif message.text.lower() == 'id':
        bot.reply_to(message, f'ID: {message.from_user.id}')


bot.polling(none_stop=True)

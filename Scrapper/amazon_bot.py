import telebot
from telebot import types
# import webbrowser
import settings as s
# import sqlite3
# --- Connect to WEB ---
import web_utils as web
# --- Classes for program ---
from classes import Book
# --- Saving ---
from save import CSVwork
# --- Sending ---
import send
# import asyncio
import bot_messages as mes
import os

TOKEN = s.BOT.token

bot = telebot.TeleBot(TOKEN)
search_text = ''
csv_file = ''
user_email = ''


def search_csv():
    global search_text
    global csv_file
    search_line = search_text.replace(' ', '+')
    url = f"https://www.amazon.com/s?k={search_line}"
    csv_file = f"bases_csv/base_{search_line.replace(' ', '_')}.csv"
    bs = web.connect(url)
    books_from_page = Book.add_books_from_page(bs)
    if not books_from_page:
        return False
    else:
        CSVwork.save_to_csv_books(books_from_page, csv_file)
        return True


@bot.message_handler(commands=['start'])
def start(message):
    greeting = mes.greeting(message.from_user.first_name, message.from_user.last_name)
    bot.send_message(message.chat.id, text=greeting, parse_mode="HTML")


@bot.message_handler(commands=['search'])
def start(message):
    bot.send_message(message.chat.id, text='Please enter a book search query: ')
    bot.register_next_step_handler(message, search)


def search(message):
    global search_text
    global csv_file
    search_text = message.text.strip()
    file_is_exist = search_csv()
    # Create an InlineKeyboardMarkup
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton("Yes", callback_data="yes")
    btn2 = types.InlineKeyboardButton("No", callback_data="no")
    markup.row(btn1, btn2)
    if file_is_exist:
        with open(csv_file, 'rb') as doc:
            bot.send_message(message.chat.id, "Books data saved to CSV:")
            bot.send_document(message.chat.id, doc)
        bot.send_message(message.chat.id, "Do you want to send the file via email?", reply_markup=markup)
    else:
        bot.send_message(message.chat.id, "We couldn't find any books.")


@bot.callback_query_handler(func=lambda call_back: True)
def callback_message(call_back):
    global csv_file
    if call_back.data == 'yes':
        bot.send_message(call_back.message.chat.id, "Enter your email:")
        bot.register_next_step_handler(call_back.message, get_email)
    elif call_back.data == 'no':
        bot.send_message(call_back.message.chat.id, "Thank you!")
        delete_csv()


def get_email(message):
    global user_email
    global csv_file
    global search_text
    user_email = message.text.strip()
    body = mes.mail_body(message.from_user.first_name, message.from_user.last_name)
    subject = f'Amazon .CSV file: {search_text}'
    send.send_massage(body, subject, csv_file, user_email)
    bot.send_message(message.chat.id, "An email has sent. Thank you!")
    delete_csv()


def delete_csv():
    try:
        os.remove(csv_file)
    except OSError as e:
        print(f"ERROR in deleting: {e}")


bot.polling(none_stop=True)

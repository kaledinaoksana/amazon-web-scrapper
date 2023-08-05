import telebot
from telebot import types
import webbrowser
import settings as s
import sqlite3
# Connect to WEB
import web_utils as web
# Classes for programm
from classes import Book
# Saving
from save import CSVwork
# Sending
import send
import asyncio

TOKEN = s.BOT.token

bot = telebot.TeleBot(TOKEN)
search_text = ''
csv_file = ''


def search_csv(text):
    global search_text
    global csv_file
    search_line = search_text.replace(' ', '+')
    url = f"https://www.amazon.com/s?k={search_line}"
    csv_file = f"bases_csv/base_{search_line.replace(' ', '_')}.csv"
    bs = web.connect(url)
    books_from_page = Book.add_books_from_page(bs)
    CSVwork.save_to_csv_books(books_from_page, csv_file)
    return


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, text='Hi! Put search request: ')
    bot.register_next_step_handler(message, search)


def search(message):
    global search_text
    global csv_file
    search_text = message.text.strip()
    search_csv(search_text)
    if csv_file:
        bot.send_message(message.chat.id, "Books data saved to CSV: " + csv_file)
        with open(csv_file, 'rb') as doc:
            bot.send_document(message.chat.id, doc)
    else:
        bot.send_message(message.chat.id, "No results found for the search.")


bot.polling(none_stop=True)

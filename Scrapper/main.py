
import settings as s
from info_html import *
from classes import Book
import requests
from bs4 import BeautifulSoup
# Save
from savings import CSVwork
# Mail
import sending as send

URL = "https://www.amazon.com/s?k=python&crid=29YNX6P1J9VR1&sprefix=python%2Caps%2C243&ref=nb_sb_noss_2"

# CONNECTION TO SITE
def connect(URL):
    page = requests.get(URL,headers=s.headers)
    soup1 = BeautifulSoup(page.content, "html.parser")
    return BeautifulSoup(soup1.prettify(), 'html.parser')

bs = connect(URL)

# FIND BOOKS FROM PAGE
books_from_page = Book.add_books_from_page(bs)

# Print the list of books
i = 0
for book in books_from_page:
    i = i+1
    print(f"Index: {i}")
    print(f"Title: {book.title}")
    print(f"Price: {book.price}")
    print(f"Score: {book.score}")
    print("---------------------")
    
# SAVE TO CSV
CSVwork.save_to_csv_books(books_from_page, s.csv_file)
print("Books data saved to CSV:", s.csv_file)

# MAIL TO TELEGRAM BOT
status = send.sent_message_bot("красоточка!")
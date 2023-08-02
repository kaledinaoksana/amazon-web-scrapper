# conda activate env-01 
# --------------------------------------------------------------------------- 
#IMPORT LIBRARIES
# Settings
import settings as s
# Connect to WEB
import web_utils as web
# Classes for programm
from classes import Book
# Saving
from save import CSVwork
# Sending
import send
import asyncio

search = "python"

search_line = search.replace(' ','+')
URL = f"https://www.amazon.com/s?k={search_line}"
csv_file = f"bases_csv/base_{search.replace(' ','_')}.csv"

# --------------------------------------------------------------------------- 
# CONNECTION TO SITE
bs = web.connect(URL)

# --------------------------------------------------------------------------- 
# FIND BOOKS FROM PAGE
books_from_page = Book.add_books_from_page(bs)

# --------------------------------------------------------------------------- 
# SAVE TO CSV
CSVwork.save_to_csv_books(books_from_page, csv_file)

# --------------------------------------------------------------------------- 
text_line = "Books data saved to CSV: " + csv_file
# # MAIL TO TELEGRAM BOT
# status = send.sent_message_bot(text_line)
async def main():
    await send.sent_message_bot_with_file(text_line, csv_file)   
loop = asyncio.get_event_loop()
loop.run_until_complete(main()) 

# MAIL TO GMAIL
# status = send.send_massage(text_line, "CSV file", csv_file)

# --------------------------------------------------------------------------- 
# #DATABASE DBwork
# from DB import DBwork as db

# # Connect to the database and create a session
# engine = db.conn_db()
# session = db.create_session(engine)

# # Create the table if it doesn't exist
# db.create_table(engine)

# with db.session_scope(engine) as session:
#     for book in books_from_page:
#         book_object = db.AmazonBook(Title=book.title, Price=book.price, Score=book.score)
#         db.add_object(session, book_object)

# --------------------------------------------------------------------------- 

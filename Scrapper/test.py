#DATABASE DBwork
from DB import DBwork as db

engine = db.conn_db()
session = db.create_session(engine)

for book in books_from_page:
    book_zero = db.AmazonBook(Title="book.title", Price="book.price", Score="book.score")
    db.add_object(session, book_zero)
from info_html import *

# Define class Book
class Book:
    def __init__(self, title, price, score):
        self.title = title
        self.price = price
        self.score = score

    def get_title(card):
        titles = card.find_all("span", {"class": BookInfo.title})
        title = ' '.join([title.get_text().strip().replace('\n', '') for title in titles])
        return title
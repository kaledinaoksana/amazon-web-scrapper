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
    
    def get_price(card):
        prices = card.find_all("span", {"class": BookInfo.price})
        price = ''.join([p.get_text().strip().replace('\n', '').replace(' ', '') for p in prices])
        return price
    
    def get_score(card):
        stars = card.find("span", {"class": BookInfo.score})
        if stars:
            score = stars.get_text().replace(' ', '').replace('\n', '')[:3]
        else:
            score = "N/A"  # Set a default value if stars element is not found
        return score
    
    def add_books_from_page(bs):
        books = []
        for index in range(2, 100):
            for card in bs.find_all("div", {"data-index": index}):
                if not card.find("span", {"class": VideoInfo.year}):
                    title = Book.get_title(card)
                    if title:
                        price = Book.get_price(card)
                        if price:
                            score = Book.get_score(card)
                            books.append(Book(title, price, score))
        return books
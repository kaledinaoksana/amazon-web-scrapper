
import csv

class CSVwork:
    
    # SAVE BOOK TO CSV
    def save_to_csv_books(books, filename):
        with open(filename, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(["Title", "Price", "Score"])  # Write header row

            for book in books:
                writer.writerow([book.title, book.price, book.score])
                



import csv
import pyodbc
import settings as st

class CSVwork:
    
    # SAVE BOOK TO CSV
    def save_to_csv_books(books, filename):
        with open(filename, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(["Title", "Price", "Score"])  # Write header row

            for book in books:
                writer.writerow([book.title, book.price, book.score])
                
class SQLwork:
    # connect db
    def connect_db():
        try:
            conn = pyodbc.connect('DRIVER=' + st.DRIVER + ';SERVER=' + st.SERVER + ';UID=' + st.USER + ';PWD=' + st.PSW )
            print("Connected to the database")
            return conn
        except pyodbc.Error as e:
            print("Error connecting to the database:", e)
            return None
    # create table
    def create_table(conn):
        if conn:
            try:
                cursor = conn.cursor()
                cursor.execute('''
                    CREATE TABLE YourTableName (
                        ID INT IDENTITY(1,1) PRIMARY KEY,
                        Column1 VARCHAR(255),
                        Column2 INT,
                        Column3 FLOAT
                    )
                ''')
                conn.commit()
                print("Table created successfully")
            except pyodbc.Error as e:
                print("Error creating table:", e)
        else:
            print("Connection to the database failed")


# Подключаемся к базе данных
connection = connect_db()

# Создаем таблицу 
create_table(connection)

# Закрываем соединение
if connection:
    connection.close()
# conda activate env-01 
import csv
import pyodbc
import settings as st

# --------------------------------------------------------------------------- 
class CSVwork:
    # SAVE BOOK TO CSV
    def save_to_csv_books(books, filename):
        with open(filename, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(["Title", "Price", "Score"])  # Write header row

            for book in books:
                writer.writerow([book.title, book.price, book.score])
                
                
# --------------------------------------------------------------------------- 
# USING OF SQLwork

# connection = SQLwork.connect_db()

# table_name = "Amazon_Books"
# # # Создаем таблицу 
# SQLwork.create_table(connection, table_name)
# for book in books_from_page:
#     SQLwork.insert_book(connection, table_name, book.title, book.price, book.score)

# Close connection
# if connection:
#     print("Close connection")
#     connection.close()
              
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
    def create_table(conn,table_name):
        if conn:
            try:
                cursor = conn.cursor()
                if SQLwork.table_exists(cursor, table_name):
                    SQLwork.delete_table(conn, table_name)
                    print("Table already exist: Delete table")
                
                query = f'''
                    CREATE TABLE {table_name} (
                        ID INT IDENTITY(1, 1) PRIMARY KEY,
                        Title VARCHAR(MAX),
                        Price VARCHAR(255),
                        Score VARCHAR(10)
                    )
                '''
                cursor.execute(query)
                conn.commit()
                print("Table created successfully")
            except pyodbc.Error as e:
                print("Error creating table:", e)
        else:
            print("Connection to the database failed")
     
    # insert to the table       
    def insert_book(conn, table_name, title, price, score):
        if conn:
            try:
                cursor = conn.cursor()
                query = "INSERT INTO %s (Title, Price, Score) VALUES ('%s', '%s', '%s')" % (table_name, title, price, score)
                cursor.execute(query)
                conn.commit()
                print("___________")
            except pyodbc.Error as e:
                print("Error inserting data:", e)
        else:
            print("Connection to the database failed")
      
    # delete table      
    def delete_table(conn, table_name):
        if conn:
            try:
                cursor = conn.cursor()
                query = f"DROP TABLE {table_name}"
                cursor.execute(query)
                conn.commit()
            except pyodbc.Error as e:
                print("Error deleting table:", e)
        else:
            print("Connection to the database failed")
            
    def table_exists(cursor, table_name):
        cursor.execute(f"SELECT OBJECT_ID('{table_name}', 'U')") 
        return cursor.fetchone() is not None  
    
# --------------------------------------------------------------------------- 
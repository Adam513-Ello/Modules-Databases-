# Author: Adam Elliott
# Purpose: Uses the sqlite3 database to create a table named books.
import sqlite3

def create_database():
    # Connect to the SQLite database
    connection = sqlite3.connect('books.db')
    
    cursor = connection.cursor()
    # Create table query
    create_table_query = '''
    CREATE TABLE IF NOT EXISTS books (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        author TEXT NOT NULL,
        year INTEGER NOT NULL
    );
    '''
    
    cursor.execute(create_table_query)
    
    connection.commit()
    connection.close()

if __name__ == "__main__":
    create_database()
    print("Database and table created successfully")

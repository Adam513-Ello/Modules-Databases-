# author: Adam Elliott
# Purpose: Creating a table frome sqlite3 data base and sqlalchemy.
from sqlalchemy import create_engine, MetaData, Table
from sqlalchemy.orm import sessionmaker
#Runs through sqlalchemy building a table.
DATABASE_URL = 'sqlite:///books.db'
engine = create_engine(DATABASE_URL, echo=True)
metadata = MetaData()
books_table = Table('books', metadata, autoload_with=engine)
Session = sessionmaker(bind=engine)
session = Session()
with engine.connect() as connection:
    query = books_table.select().order_by(books_table.c.title)
    result = connection.execute(query)

    for row in result:
        print(row.title)

# Close
session.close()

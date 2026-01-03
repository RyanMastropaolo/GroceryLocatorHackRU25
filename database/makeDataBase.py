#this will create and host the database
import sqlite3

db = sqlite3.connect("database.db")  # Creates or connects to an SQLite database
cursor = db.cursor()  # Create a cursor object to interact with the database

cursor.execute("""
CREATE TABLE IF NOT EXISTS stores (
    storeID INTEGER PRIMARY KEY,
    storeName TEXT NOT NULL,
    lat FLOAT NOT NULL,
    long FLOAT NOT NULL,
    zipcode TEXT NOT NULL
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS items (
    storeID INTEGER NOT NULL,
    item TEXT NOT NULL,
    price FLOAT NOT NULL
)
""")

db.commit()  # Save changes
cursor.close
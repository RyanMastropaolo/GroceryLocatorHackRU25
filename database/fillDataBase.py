import sqlite3
import pandas as pd

# Connect to SQLite (or create a new database)
conn = sqlite3.connect("database.db")
cursor = conn.cursor()

# Read the CSV file
df = pd.read_csv("stores.csv")

# Insert the CSV data into a table
df.to_sql("stores", conn, if_exists="replace", index=False)

# Commit and close
conn.commit()

# Read the CSV file
df = pd.read_csv("product_prices - Sheet1.csv")

# Insert the CSV data into a table
df.to_sql("items", conn, if_exists="replace", index=False)


conn.close()

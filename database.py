import sqlite3

# Connect to SQLite database (it will be created if it doesn't exist)
conn = sqlite3.connect('restaurant_data.db')

# Create a cursor object
cursor = conn.cursor()

# Create table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS restaurant (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        online_order INTEGER,
        book_table INTEGER,
        votes INTEGER,
        approx_cost REAL,
        location TEXT,
        rest_type TEXT,
        cuisines TEXT
    )
''')

# Commit changes and close the connection
conn.commit()
conn.close()

import sqlite3

conn = sqlite3.connect('database.db')
conn.execute('CREATE TABLE tasks (id INTEGER PRIMARY KEY, content TEXT)')
conn.close()

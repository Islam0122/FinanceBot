import sqlite3

conn  = sqlite3.connect('finance.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
telegram_id INTEGER NOT NULL,
username TEXT NOT NULL,
created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP)''')
conn.commit()

def add_user(telegram_id, username):
    cursor.execute('''
    INSERT INTO users (telegram_id, username)
    VALUES (?, ?)
    ''', (telegram_id, username))
    conn.commit()


def get_user_by_telegram_id(telegram_id):
    cursor.execute('''
    SELECT username FROM users WHERE telegram_id = ?
    ''', (telegram_id,))
    user = cursor.fetchone()
    return user


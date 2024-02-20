import sqlite3

class Database:
    def __init__(self, db):
        self.conn = sqlite3.connect(db+ ".db")
        self.cur = self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS note ( id INTEGER PRIMARY KEY, title TEXT, content TEXT NOT NULL);")
        self.conn.commit()
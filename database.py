import sqlite3


# This class is used to create a note object
class Note:
    def __init__(self, id=None, title=None, content=''):
        self.id = id
        self.title = title
        self.content = content

class Database:
    def __init__(self, db):
        self.conn = sqlite3.connect(db+ ".db")
        self.cur = self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS note ( id INTEGER PRIMARY KEY, title TEXT, content TEXT NOT NULL);")
        self.conn.commit()
        
    def add(self, note):
        self.conn.execute("INSERT INTO note VALUES (NULL, ?, ?)", (note.title, note.content))
        self.conn.commit()

    def get_all(self):
        cursor = self.conn.execute("SELECT * FROM note")
        lista_notes = []
        for linha in cursor:
            id = linha[0]
            title = linha[1]
            content = linha[2]
            note = Note(id, title, content)
            lista_notes.append(note)
        return lista_notes
    
    def update(self, note):
        self.conn.execute("UPDATE note SET title = ?, content = ? WHERE id = ?", (note.title, note.content, note.id))
        self.conn.commit()

    def delete(self, id):
        self.conn.execute("DELETE FROM note WHERE id = ?", (id,))
        self.conn.commit()
    

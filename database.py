import sqlite3
import os.path


class db():
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(BASE_DIR, "casosklad.db")

    def __init__(self):
        self.mydb = sqlite3.connect(self.db_path)
        self.cursor = self.mydb.cursor()
        query = """CREATE TABLE servers NOT EXISTS (
        id BIGINT PRIMARY KEY NOT NULL,
        prefix VARCHAR(256) DEFAULT '.' NOT NULL);"""
    def fetch_prefix(self, gid):
        prefix_query = "SELECT prefix FROM servers WHERE id = ?"
        self.cursor.execute(prefix_query, (gid,))
        prefix = self.cursor.fetchone()
        return prefix[0]

    def add_prefix(self, gid, prefix="."):
        prefix_query = "INSERT INTO servers(id, prefix) VALUES (?, ?)"
        self.cursor.execute(prefix_query, (gid, prefix,))
        self.mydb.commit()

    def remove_prefix(self, gid):
        prefix_query = "DELETE FROM servers WHERE id = ?"
        self.cursor.execute(prefix_query, (gid,))
        self.mydb.commit()

    def update_prefix(self, gid, prefix):
        prefix_query = "UPDATE servers SET prefix = ? WHERE id = ?"
        self.cursor.execute(prefix_query, (prefix, gid, ))
        self.mydb.commit()

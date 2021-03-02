import sqlite3
import os.path


class db():
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(BASE_DIR, "casosklad.db")

    def __init__(self):
        self.mydb = sqlite3.connect(self.db_path)
        cursor = self.mydb.cursor()
        queries = ["""CREATE TABLE IF NOT EXISTS servers  (
        id BIGINT PRIMARY KEY NOT NULL,
        prefix VARCHAR(256) DEFAULT '.' NOT NULL);""",
                   """CREATE TABLE IF NOT EXISTS quotes (
        id INTEGER PRIMARY KEY,
        author VARCHAR(64) NOT NULL,
        quote VARCHAR(256) NOT NULL
        )""",
                   """CREATE TABLE IF NOT EXISTS "questions" (
        "qid"	INTEGER NOT NULL,
        "uid"	BIGINT NOT NULL,
        "question"	TEXT NOT NULL,
	    "mid"	BIGINT NOT NULL,
        PRIMARY KEY("qid" AUTOINCREMENT)
        );""",
                   """CREATE TABLE IF NOT EXISTS "answers" (
    	"aid"	INTEGER,
    	"qid"	INTEGER NOT NULL,
    	"answer"	TEXT NOT NULL,
    	"reaction"	TEXT NOT NULL,
    	FOREIGN KEY("qid") REFERENCES "questions"("qid") ON DELETE CASCADE,
    	PRIMARY KEY("aid" AUTOINCREMENT)
        );""",
                   """CREATE TABLE IF NOT EXISTS "votes" (
    	"uid"	BIGINT NOT NULL,
    	"aid"	INTEGER NOT NULL,
    	FOREIGN KEY("aid") REFERENCES "answers"("aid") ON DELETE CASCADE,
    	PRIMARY KEY("uid","aid")
        );"""
                   ]
        for query in queries:
            cursor.execute(query, ())
            self.mydb.commit()
        cursor.close()

    def new_poll(self, uid, question, mid):
        cursor = self.mydb.cursor()
        query = "INSERT INTO questions(uid, question, mid) VALUES (?, ?, ?)"
        cursor.execute(query, (uid, question, mid,))
        self.mydb.commit()
        cursor.close()
        return cursor.lastrowid

    def get_poll(self, qid):
        cursor = self.mydb.cursor()
        query = "SELECT uid, mid FROM questions WHERE qid = ?"
        cursor.execute(query, (qid, ))
        poll = cursor.fetchone()
        cursor.close()
        return poll

    def new_answer(self, qid, question, mid):
        pass

    def new_quote(self, quote, author):
        cursor = self.mydb.cursor()
        query = "INSERT INTO quotes(author, quote) VALUES (?, ?)"
        cursor.execute(query, (author, quote,))
        self.mydb.commit()
        cursor.close()

    def list_quotes(self):
        cursor = self.mydb.cursor()
        query = "SELECT * FROM quotes"
        cursor.execute(query, ())
        quotes = cursor.fetchall()
        cursor.close()
        return quotes

    def fetch_prefix(self, gid):
        cursor = self.mydb.cursor()
        prefix_query = "SELECT prefix FROM servers WHERE id = ?"
        cursor.execute(prefix_query, (gid,))
        prefix = cursor.fetchone()
        cursor.close()
        return prefix[0]

    def add_prefix(self, gid, prefix="."):
        cursor = self.mydb.cursor()
        prefix_query = "INSERT INTO servers(id, prefix) VALUES (?, ?)"
        cursor.execute(prefix_query, (gid, prefix,))
        self.mydb.commit()
        cursor.close()

    def remove_prefix(self, gid):
        cursor = self.mydb.cursor()
        prefix_query = "DELETE FROM servers WHERE id = ?"
        cursor.execute(prefix_query, (gid,))
        self.mydb.commit()
        cursor.close()

    def update_prefix(self, gid, prefix):
        cursor = self.mydb.cursor()
        prefix_query = "UPDATE servers SET prefix = ? WHERE id = ?"
        cursor.execute(prefix_query, (prefix, gid, ))
        self.mydb.commit()
        cursor.close()

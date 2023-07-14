import sqlite3


class Database:
    def __init__(self, database):
        self.database = 'db/' + database + '.db'
        self.conn = None

    def connect(self):
        self.conn = sqlite3.connect(self.database)

    def cursor(self):
        return self.conn.cursor()

    def closeConn(self):
        self.conn.close()

    def commit(self):
        self.conn.commit()

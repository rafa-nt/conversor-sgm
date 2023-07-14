import psycopg2


class Postgres():
    def __init__(self, database='', host='localhost', port=5450, user='postgres', password='19983101'):
        self.database = database
        self.host = host
        self.port = port
        self.user = user
        self.password = password

    def connect(self):
        self.conn = psycopg2.connect(
            host=self.host,
            database=self.database,
            port=self.port,
            user=self.user,
            password=self.password,
        )

    def cursor(self):
        return self.conn.cursor()

    def closeConn(self):
        self.conn.close()

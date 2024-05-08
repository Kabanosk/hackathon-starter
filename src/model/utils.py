from dotenv import load_dotenv
import os
import psycopg2

load_dotenv()


class Database:
    def __init__(self):
        self.dbname = os.getenv('DB_NAME')
        self.host = os.getenv('DB_HOST')
        self.user = os.getenv('DB_USER')
        self.password = os.getenv('DB_PASS')

    def create_connection(self):
        dsn = f"dbname={self.dbname} user={self.user} password={self.password} host={self.host}"
        return psycopg2.connect(dsn)

    @staticmethod
    def close_connection(connection):
        connection.close()

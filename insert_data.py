import MySQLdb
import sys, getopt

class Database:

    host = 'localhost'
    user = 'root'
    password = '123456'
    db = 'test_data'

    def __init__(self):
        self.connection = MySQLdb.connect(self.host, self.user, self.password, self.db)
        self.cursor = self.connection.cursor()

    def insert(self, query):
        try:
            self.cursor.execute(query)
            self.connection.commit()
        except:
            self.connection.rollback()



    def query(self, query):
        cursor = self.connection.cursor( MySQLdb.cursors.DictCursor )
        cursor.execute(query)

        return cursor.fetchall()
     def __del__(self):
        self.connection.close()


if __name__ == "__main__":

    db = Database()
    insert_query = """
        INSERT INTO test_tables
        (`ID`, `IP`, `Type`, `Field1`, `Field2`)
        VALUES
        ('1', , '192.168.1.1', 1, 1, 0),
        """
    db.insert(insert_query)
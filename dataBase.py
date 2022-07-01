import mysql.connector

class DataBase:

    def __init__(self):

        self.studentDb = mysql.connector.connect(

            host = 'localhost',
            user = 'root',
            passwd = '',
            database = 'students'

        )

    def checkConnection(self):

        print(self.studentDb)

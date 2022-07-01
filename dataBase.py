import mysql.connector

class DataBase:

    def __init__(self):

        try:

            self.studentDb = mysql.connector.connect(

                host = 'localhost',
                user = 'root',
                passwd = '',
                database = 'students'

            )
        except:

            print("Cannot connect to 'students' database, DataBase class")

    def checkConnection(self):

        print(self.studentDb)

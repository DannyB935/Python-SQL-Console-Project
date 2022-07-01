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

            #The query variable is made to execute queries into the database
            self.query = self.studentDb.cursor()

            #The list will help us to have a better handle of the students
            self.studentsList = []

        except:

            print("Cannot connect to 'students' database, DataBase class")


    #The method gets as a parameter the student object(s)
    def insertStudent(self, s):

        queryAux = f"INSERT INTO students(name, lastName, age, code, semester, degree) VALUES ('{s.name}','{s.lastName}', {s.age}, '{s.code}', {s.semester}, '{s.degree}');"
        self.query.execute(queryAux)
        self.studentDb.commit()

        #Add the new student at the end in case there's more students loaded
        self.studentsList.append(s)

    def checkConnection(self):

        print(self.studentDb)

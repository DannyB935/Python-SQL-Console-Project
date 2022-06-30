
class Student:

    def __init__(self):

        self.name = ''
        self.lastName = ''
        self.age = 0
        self.code = ''
        self.semester = 0
        self.degree = ''

    #Setters

    def setName(self, n):
        self.name = n

    def setLastName(self, l):
        self.lastName = l

    def setAge(self, a):
        self.age = a

    def setCode(self, c):
        self.code = c

    def setSemester(self, s):
        self.semester = s

    def setDegree(self, d):
        self.degree = d

    #Getters

    def getName(self):
        return self.name

    def getLastName(self):
        return self.lastName

    def getAge(self):
        return self.age

    def getCode(self):
        return self.code

    def getSemester(self):
        return self.semester

    def getDregree(self):
        return self.degree

    #Print method

    def printStudent(self):

        print(f"{self.code}\n{self.name}\n{self.lastName}\n{self.age}\n{self.semester}\n{self.degree}")

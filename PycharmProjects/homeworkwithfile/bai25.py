class Person:
    def __init__(self, name:str, address:str):
        self.name = name
        self.address = address

    def getname(self):
        return self.name

    def setname(self,name):
        self.name = name

    def getaddress(self):
        return self.address

    def setaddress(self,address):
        self.address = address

class Student(Person):
    def __init__(self, name:str, address:str, program:str, year:int, score:float):
        Person .__init__(name, address)
        self.program = program
        self.year = year
        self.score = score

    def getprogram(self):
        return self.program

    def setprogram(self,program):
        self.program = program

    def getyear(self):
        return self.year

    def setyear(self,year):
        self.year = year

    def getscore(self):
        return self.score

    def setscore(self,score):
        self.score = score

    
class Staff(Student):
    def __init__(self, name:str, address:str, school:str, salary:int):
        Person .__init__(name, address)
        self.school = school
        self.salary = salary

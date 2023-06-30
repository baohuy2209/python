"""
![](../../AppData/Local/Temp/exercise-oop-class-object-employee.jpg)
getFullName(): FulllName = lastName + firstName

getAnnualSalary() tính tổng lương nhận hằng năm => salary * 12

upToSalary(): Tính tiền lương sau khi tăng lên percent(%). Ví dụ percent = 10% => output = salary  +  (salary * precent) / 100
"""

class Employee:
    def __init__(self,id,firstname,lastname,salary):
        self.id = id
        self.firstname = firstname
        self.lastname = lastname
        self.salary = salary

    def getid(self):
        return self.id

    def setid(self,id):
        self.id = id

    def getfirstname(self):
        return self.firstname

    def setfirstname(self,firstname):
        self.firstname=firstname

    def getlastname(self):
        return self.lastname

    def setlastname(self,lastname):
        self.lastname = lastname

    def getfullname(self):
        return self.firstname + self.lastname

    def getsalary(self):
        return self.salary

    def setsalary(self,lastname):
        self.lastname = lastname

    def getannualsalary(self):
        return self.salary*12

    def uptosalary(self,bonus):
        return self.salary + bonus

    def __repr__(self):
        return "ID : "+str(self.id)+" Fullname : "+str(self.getfullname())+" salary : "+str(self.salary)

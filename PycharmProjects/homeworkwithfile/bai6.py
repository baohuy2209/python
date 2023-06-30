"""
#Khoa CNTT – DHKHTN cần quản lý việc thanh toán tiền lương cho các cán bộ giáo viên trong khoa.
#Để quản lý được, khoa cần các thông tin sau:

#Với mỗi cán bộ giáo viên có các thông tin sau: lương cứng, lương thưởng, tiền phạt, lương thực lĩnh.
#Và các thông tin cá nhân: Họ tên, tuổi, quê quán, mã số giáo viên.

#Yêu cầu 1: Xây dựng lớp Nguoi để quản lý các thông tin cá nhân của mỗi giáo viên.

#Yêu cầu 2: Xây dựng lớp CBGV để quản lý các thông tin của các cán bộ giáo viên.

#Yêu cầu 3: Xây dựng các phương thức thêm, xoá các cán bộ giáo viên theo mã số giáo viên.

#Yêu cầu 4: Tính lương thực lĩnh cho giáo viên: Lương thực = Lương cứng + lương thưởng – lương phạt.
"""


class Teacher(object):

    def __init(self,fullname,age,country,mgv,hardsalary,bonus,fine):
        self.fullname = fullname
        self.age = age
        self.country = country
        self.mgv = mgv
        self.hardsalary = hardsalary
        self.bonus = bonus
        self.fine = fine

    def getFullname(self):
        return self.fullname

    def setFullname(self,fullname):
        self.fullname = fullname

    def getAge(self):
        return self.age

    def setAge(self,age):
        self.age = age

    def getCountry(self):
        return self.country

    def setCountry(self,country):
        self.country = country

    def getMGV(self):
        return self.mgv

    def setMGV(self,mgv):
        self.mgv = mgv

    def getHardsalary(self):
        return self.hardsalary

    def setHardsalary(self,hardsalary):
        self.hardsalary = hardsalary

    def getBonus(self):
        return self.bonus

    def setBonus(self,bonus):
        self.bonus = bonus

    def getFine(self):
        return self.fine

    def setFine(self,fine):
        self.fine = fine

    def getSalary(self):
        return self.hardsalary + self.bonus - self.fine

    def writefileinput(self,fullname,age,country,hardsalary,bonus,fine):
        f = open("Teacher.txt","w")
        f.write("Information of Teacher : ")
        f.write("Fullname : ")
        f.write(str(fullname))
        f.write("\n")
        f.write("Age : ")
        f.write(str(age))
        f.write("\n")
        f.write("Country of Teacher : ")
        f.write(str(country))
        f.write("\n")
        f.write("Hard salary : ")
        f.write(str(hardsalary))
        f.write("\n")
        f.write("Bonus : ")
        f.write(str(bonus))
        f.write("\n")
        f.write("Fine : ")
        f.write(str(fine))
        f.write("\n")
        f.close()

    def readfileinput(self):
        f = open('Student.txt','r')
        nd = f.read()
        print(nd)

    def __str__(self):
        return "Fullname : "+self.fullname+", Age : "+self.age+", Country of Student : "+self.country+", Hard Salary : "+self.hardsalary+", Bonus : "+self.bonus+", Fine : "+self.fine


ListTeacher = []


class ManageTeacher :

    def insertTeacher(self):
        print("Enter the information . ")
        fullname = input("Fullname : ")
        age = int(input("Age : "))
        country = input("Country : ")
        hardsalary = int(input("Hard Salary : "))
        bonus = int(input("Bonus : "))
        fine = int(input("Fine : "))
        op = Teacher(fullname, age, country,hardsalary,bonus,fine)
        ListTeacher.append(op)
        op.writefileinput(fullname, age, country,hardsalary,bonus,fine)

    def deleteTeacher(self):
        mgv = int(input("Enter Code of teacher to delete : "))
        i = 0
        for op in ListTeacher:
            if op.getMGV() == mgv :
                ListTeacher = ListTeacher.pop(i)
            i += 1

    def showTeacher(self):
        for op in ListTeacher :
            print(op)


if __name__  == "__main__" :
    ck = True
    print("List of Operation : ")
    print("1. Insert teacher ")
    print("2. Delete Teacher ")
    print("3. Show information of techer  ")
    print("4. Exit ")
    ms = ManageTeacher()
    while (ck):
        ch = int(input("Enter your choice : "))
        if ch == 1:
            ms.insertTeacher()
        elif ch == 2:
            ms.deleteTeacher()
        elif ch == 3:
            ms.showTeacher()
        elif ch == 4:
            ck = False
        else:
            print("Invalid")
    print("====================================================================")



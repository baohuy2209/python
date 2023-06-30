"""
#Để quản lý hồ sơ học sinh của trường THPT nhà trường cần các thông tin sau: Lớp,  và các thông tin về cá nhân của mỗi học sinh.

#Mỗi học sinh có các thông tin sau: Họ tên, tuổi, quê quán.

#Yêu cầu 1: Xây dựng HocSinh để quản lý thông tin của mỗi học sinh.

#Yêu cầu 2: Xây dựng các phương thức thêm, hiển thị thông tin của mỗi học sinh.

#Yêu cầu 3: Cài đặt chương trình có các chức năng sau:

#Thêm học sinh mới.
#Hiện thị các học sinh 20 tuổi.
#Cho biết số lượng các học sinh có tuổi là 23 và quê ở Quy Nhon .
"""
class Student(object) :
    def __init__(self,fullname,age,country):
        self.fullname = fullname
        self.age = age
        self.country = country
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
    def writefileinput(self,fullname,age,country):
        f = open("Student.txt","w")
        f.write("Information of Student : ")
        f.write("Fullname : ")
        f.write(str(fullname))
        f.write("\n")
        f.write("Age : ")
        f.write(str(age))
        f.write("\n")
        f.write("Country of student : ")
        f.write(str(country))
        f.write("\n")
        f.close()
    def readfileinput(self):
        f = open('Student.txt','r')
        nd = f.read()
        print(nd)
    def __str__(self):
        return "Fullname : "+self.fullname+", Age : "+self.age+", Country of Student : "+self.country
ListStudent = []
class ManageStudent :
    def insertStudent(self):
        print("Enter the information . ")
        fullname = input("Fullname : ")
        age = int(input("Age : "))
        country = input("Country : ")
        op = Student(fullname,age,country)
        ListStudent.append(op)
        op.writefileinput(fullname,age,country)
    def showStudent1(self):
        for op in ListStudent :
            if op.getAge() == 20 :
                print(op)
    def showStudent2(self):
        for op in ListStudent:
            if op.getAge() == 23 and (op.getCountry() == "Quy Nhon" or op.getCountry() == "quy nhon" or op.getCountry() == "Quy Nhon"):
                print(op)
if __name__ == "__main__" :
    ck = True
    print("List of Operation : ")
    print("1. Insert student ")
    print("2. Show students have 20 years old ")
    print("3. Show students have 23 years old and these country are Quy Nhon ")
    print("4. Exit ")
    ms = ManageStudent()
    while(ck) :
        ch = int(input("Enter your choice : "))
        if ch == 1 :
            ms.insertStudent()
        elif ch == 2 :
            ms.showStudent1()
        elif ch == 3 :
            ms.showStudent2()
        elif ch == 4 :
            ck = False
        else :
            print("Invalid")
    print("====================================================================")

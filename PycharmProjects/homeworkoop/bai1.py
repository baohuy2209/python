#Các thí sinh dự thi đại học bao gồm các thí sinh thi khối A, B, và khối C. Các thí sinh cần quản lý các thông tin sau: Số báo danh, họ tên, địa chỉ, mức ưu tiên.

#Thí sinh thi khối A thi các môn: Toán, Lý, Hoá.

#Thí sinh thi khối B thi các môn: Toán, Hoá, Sinh.

#Thí sinh thi khối C thi các môn: Văn, Sử, Địa.

#Yêu cầu 1: Xây dựng các lớp để quản lý các thi sinh dự thi đại học.

#Yêu cầu 2: Xây dựng lớp TuyenSinh có các chức năng:

#Thêm mới thí sinh.
#Hiện thị thông tin của thí sinh và khối thi của thí sinh.
#Tìm kiếm theo số báo danh.
#Thoát khỏi chương trình.

class birthday(object) :
    def __init__(self,day,month,year):
        self.day = day
        self.month = month
        self.year = year
    def getDay(self):
        return self.day
    def setDay(self,day):
        self.day = day
    def getMonth(self):
        return self.month
    def setMonth(self,month):
        self.month = month
    def getYear(self):
        return self.year
    def setYear(self,year):
        self.year = year
    def __str__(self):
        return "Birthday of student : %s// %s// %s "%(self.day,self.month,self.year)
class CSStudent(object) :
    def __init__(self,fullname,age,bd,gender):
        self.fullname = fullname
        self.age = age
        self.bd = bd
        self.gender = gender
    def getFullname(self):
        return self.fullname
    def setFullname(self,fullname):
        self.fullname = fullname
    def getAge(self):
        return self.age
    def setAge(self,age):
        self.age = age
    def getGender(self):
        return self.gender
    def setFullname(self,gender):
        self.gender = gender
    def getBD(self):
        return self.BD
    def setBD(self,bd):
        self.bd = bd
    def __str__(self):
        return "The information of student : + Fullname : %s + Age : %s Bd : %s Gender : %s "%(self.fullname,self.age,self.bd,self.gender)
class A (CSStudent) :
    def __init__(self ,fullname ,age ,bd ,gender , math, physical, chemical,):
        CSStudent .__init__(self, fullname, age, bd, gender)
        self.math = math
        self.physical = physical
        self.chemical = chemical
    def getMath(self):
        return self.math
    def setMath(self,math):
        self.math = math
    def getPhysical(self):
        return self.physical
    def setPhysical(self,physical):
        self.physical = physical
    def getChemical(self):
        return self.chemical
    def setChemical(self,chemical):
        self.chemical = chemical
    def getAverage(self):
        return (self.math + self.physical + self.chemical)/3
    def __str__(self):
        return "+Math : %s +Physical: %s +Chemical: %s"%(self.math,self.physical,self.chemical)

class B (CSStudent) :
    def __init__(self ,fullname ,age ,bd ,gender ,math, chemical, biology):
        CSStudent.__init__(self, fullname, age, bd, gender)
        self.math = math
        self.chemical = chemical
        self.biology = biology
    def getMath(self):
        return self.math
    def setMath(self, math):
        self.math = math
    def getBiology(self):
        return self.biology
    def setPhysical(self, physical):
        self.physical = physical
    def getChemical(self):
        return self.chemical
    def setChemical(self, chemical):
        self.chemical = chemical
    def getAverage(self):
        return (self.math + self.biology + self.chemical) / 3

    def __str__(self):
        return "+Math : %s +Physical: %s +Chemical: %s" % (self.math, self.biology, self.chemical)
class C (CSStudent) :
    def __init__(self ,fullname ,age ,bd ,gender ,literature, history, geography):
        CSStudent.__init__(self, fullname, age, bd, gender)
        self.history = history
        self.literature = literature
        self.geography = geography
    def getLiterature(self):
        return self.literature
    def setLiterature(self, literature):
        self.literature = literature
    def getHistory(self):
        return self.history
    def setHistory(self, history):
        self.history = history
    def getGeography(self):
        return self.geography
    def setGeography(self, geography):
        self.geography = geography
    def getAverage(self):
        return (self.literature + self.geography + self.history) / 3
    def __str__(self):
        return "+Math : %s +Physical: %s +Chemical: %s" % (self.literature, self.history, self.geography)

if __name__ == '__main__':
    print("=====Operation with list of student =====")
    print("1. Insert student .")
    print("2. Show information of student .")
    print("3. Exit ")
    DSHS = []
    check = True
    check1 = True
    while (check) :
        choice = int(input("Enter choice : "))
        if choice == 1:
            namestd = input("Enter fullname : ")
            agestd = int(input("Enter age : "))
            genderstd = input("Enter gender : ")
            day = int(input("Enter day : "))
            month = int(input("Enter month : "))
            year = int(input("Enter year : "))
            bd = birthday(day, month, year)
            while (check1) :
                choice2 = int(input("Enter choice2 : "))
                if choice2 == 1:
                    mathstd = int(input("Enter mark of math : "))
                    physicalstd = int(input("Enter mark of physical : "))
                    chemicalstd = int(input("Enter mrak of chemical : "))
                    std = A(namestd, agestd, bd, genderstd, mathstd, physicalstd, chemicalstd)
                    DSHS.append(std)
                elif choice2 == 2:
                    mathstd = int(input("Enter mark of math : "))
                    biologystd = int(input("Enter mark of physical : "))
                    chemicalstd = int(input("Enter mrak of chemical : "))
                    std = B(namestd, agestd, bd, genderstd, mathstd, biologystd, chemicalstd)
                    DSHS.append(std)
                elif choice2 == 3:
                    litstd = int(input("Enter mark of math : "))
                    hisstd = int(input("Enter mark of physical : "))
                    geostd = int(input("Enter mrak of chemical : "))
                    std = C(namestd, agestd, bd, genderstd, litstd, hisstd, geostd)
                    DSHS.append(std)
                else:
                    check1 = False
        elif choice == 2 :
            for t in DSHS:
                print(t)
        elif choice == 3 :
            check = False
    print("=====================================")
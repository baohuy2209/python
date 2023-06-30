#Tạo một class person với các thông tin sơ yếu lí lịch . Ghi các thông tin đó vào file rồi đọc chúng
class Person (object) :
    def __init__(self,fullname,age,gender,address) :
        self.fullname = fullname
        self.age = age
        self.gender = gender
        self.address = address
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
    def setGender(self,gender):
        self.gender = gender
    def getAddress(self):
        return self.address
    def setAddress(self,address):
        self.address = address
    def writefile(self,fullname,age,gender,address):
        f = open('Person.txt','w')
        f.write("Ho va ten : ")
        f.write(str(fullname))
        f.write("\n")
        f.write("Tuoi : ")
        f.write(str(age))
        f.write("\n")
        f.write("Gioi tinh  : ")
        f.write(str(gender))
        f.write("\n")
        f.write("Dia chi  : ")
        f.write(str(address))
        f.write("\n")
        f.close()

    def readfile(self):
        f = open('Person.txt','r')
        nd = f.read()
        print(nd)
fullname = input("Nhap Ten : ")
age = int(input("Nhap tuoi : "))
gender = input("Nhap gioi tinh : ")
address = input("Nhap dia chi : ")
ps = Person(fullname,age,gender,address)
ps.writefile(fullname,age,gender,address)
ps.readfile()

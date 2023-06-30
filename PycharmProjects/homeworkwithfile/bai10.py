"""#Khoa CNTT – DHKHTN cần quản lý việc thanh toán tiền lương cho các cán bộ giá viên trong khoa. Để quản lý được, khoa cần các thông tin sau:

#Với mỗi cán bộ giáo viên có các thông tin sau: lương cứng, lương thưởng, tiền phạt, lương thực lĩnh, và các thông tin cá nhân: Họ tên, tuổi, quê quán, mã số giáo viên.

#Yêu cầu 1: Xây dựng lớp Nguoi để quản lý các thông tin cá nhân của mỗi giáo viên.

#Yêu cầu 2: Xây dựng lớp CBGV để quản lý các thông tin của các cán bộ giáo viên.

#Yêu cầu 3: Xây dựng các phương thức thêm, xoá các cán bộ giáo viên theo mã số giáo viên.

#Yêu cầu 4: Tính lương thực lĩnh cho giáo viên: Lương thực = Lương cứng + lương thưởng – lương phạt.
"""

class Person:

    def __init__(self, fullname, age, address,tccode):
        self.fullname = fullname
        self.age = age
        self.address = address
        self.tccode = tccode


class Teacher(Person):

    def __init__(self, fullname, age, address, tccode, hardsalary, bonus, fine):
        Person .__init__(fullname, age, address, tccode)
        self.hardsalary = hardsalary
        self.bonus = bonus
        self.fine = fine

    def getsalary(self):
        return self.hardsalary+self.bonus-self.fine

    def __repr__(self):
        return "The fullname :"+self.fullname+" Age :"+self.age+" Address :"+self.address+" Teacher code :"+self.tccode+" Salary : "+self.getsalary()


Listtecher = []


def inputinformation():
    print("Enter the information of teacher :")
    fullname = input("The fullname :")
    age = int(input("Age : "))
    address = input("Address : ")
    tccode = input("Teacher code : ")
    hardsalary = int(input("Hard salary :"))
    bonus = int(input("Bonus : "))
    fine = int(input("Fine : "))
    obj = Teacher(fullname, age, address, tccode, hardsalary, bonus, fine)
    return obj


class Manageteacher:

    def insert(self):
        tc = inputinformation()
        Listtecher.append(tc)

    def remove(self):
        code = input("Enter teacher code you want to remove : ")
        for item in Listtecher:
            if code == item.tccode:
                Listtecher.remove(item)

    def edit(self):
        name = input("Enter name of teacher which you want to remove : ")
        for item in Listtecher:
            if name == item.fullname:
                item = inputinformation()

    def show(self):
        for item in Listtecher:
            print(repr(item))


if __name__ == "__main__":
    print("List of operation : ")
    print("1. Insert repcepit ")
    print("2. Edit information ")
    print("3. Remove repcepit ")
    print("4. Show all information ")
    print("5. Exit")
    check = True
    mt = Manageteacher()
    while (check):
        choice = int(input("Enter the choice :"))
        if choice == 1:
            mt.insert()
        elif choice == 2:
            mt.edit()
        elif choice == 3:
            mt.remove()
        elif choice == 4:
            mt.show()
        elif choice == 5:
            check = False
        else:
            raise Exception("Invalid.")
    print("===========================================================================")
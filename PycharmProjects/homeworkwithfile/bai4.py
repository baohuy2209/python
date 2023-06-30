"""

#Một đơn vị sản xuất gồm có các cán bộ là công nhân, kỹ sư, nhân viên.
#Mỗi cán bộ cần quản lý các dữ liệu: Họ tên, tuổi, giới tính(name, nữ, khác), địa chỉ.

#Cấp công nhân sẽ có thêm các thuộc tính riêng: Bậc (1 đến 10).
#Cấp kỹ sư có thuộc tính riêng: Nghành đào tạo.
#Các nhân viên có thuộc tính riêng: công việc.
#Yêu cầu 1: Xây dựng các lớp CongNhan, KySu, NhanVien kế thừa từ lớp CanBo.

#Yêu cầu 2: Xây dựng lớp QLCB(quản lý cán bộ) cài đặt các phương thức thực hiện các chức năng sau:

#Thêm mới cán bộ.
#Tìm kiếm theo họ tên.
#Hiện thị thông tin về danh sách các cán bộ.
#Thoát khỏi chương trình.
"""
class Officer(object) :
    def __init__(self,fullname,age,gender,address):
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
class worker (Officer) :
    def __init__(self,fullname,age,gender,address,rank):
        Officer .__init__(self,fullname,age,gender,address)
        self.rank = rank

    def getRank(self):
        return self.rank
    def setRank(self,rank):
        self.rank = rank

    def writeinputfile(self,fullname,age,gender,address,rank):
        f = open('Inputfileofficer.txt','w')
        f.write("The information of Worker : ")
        f.write("Fullname : ")
        f.write(str(fullname))
        f.write("\n")
        f.write("Age : ")
        f.write(str(age))
        f.write("\n")
        f.write("Gender : ")
        f.write(str(gender))
        f.write("\n")
        f.write("Address : ")
        f.write(str(address))
        f.write("\n")
        f.write("Rank : ")
        f.write(str(rank))
        f.write("\n")
        f.close()
    def readinputfile(self):
        f = open('Inputfileofficer.txt','w')
        nd = f.read()
        print(nd)

    def __str__(self):
        return "Fullname : "+self.fullname+", Age : "+self.age+", Gender : "+self.gender+", Address :"+self.address+", Rank of worker : "+self.rank+"."
class engineer (Officer) :
    def __init__(self,fullname,age,gender,address,branch):
        Officer .__init__(self,fullname,age,gender,address)
        self.branch = branch

    def getBranch(self):
        return self.branch
    def setBranch(self,branch):
        self.branch = branch


    def writeinputfile(self,fullname,age,gender,address,branch):
        f = open('Inputfileofficer.txt','w')
        f.write("The information of Engineer")
        f.write("Fullname : ")
        f.write(str(fullname))
        f.write("\n")
        f.write("Age : ")
        f.write(str(age))
        f.write("\n")
        f.write("Gender : ")
        f.write(str(gender))
        f.write("\n")
        f.write("Address : ")
        f.write(str(address))
        f.write("\n")
        f.write("Rank : ")
        f.write(str(branch))
        f.write("\n")
        f.close()
    def readinputfile(self):
        f = open('Inputfileofficer.txt','w')
        nd = f.read()
        print(nd)

    def __str__(self):
        return "Fullname : "+self.fullname+", Age : "+self.age+", Gender : "+self.gender+", Address :"+self.address+", Branch of engineer : "+self.branch+"."
class staff(Officer) :
    def __init__(self,fullname,age,gender,address,task):
        Officer .__init__(self,fullname,age,gender,address)
        self.task = task

    def getTask(self):
        return self.task
    def setTask(self,task):
        self.task = task


    def writeinputfile(self,fullname,age,gender,address,task):
        f = open('Inputfileofficer.txt','w')
        f.write("The information of Staff")
        f.write("Fullname : ")
        f.write(str(fullname))
        f.write("\n")
        f.write("Age : ")
        f.write(str(age))
        f.write("\n")
        f.write("Gender : ")
        f.write(str(gender))
        f.write("\n")
        f.write("Address : ")
        f.write(str(address))
        f.write("\n")
        f.write("Task : ")
        f.write(str(task))
        f.write("\n")
        f.close()
    def readinputfile(self):
        f = open('Inputfileofficer.txt','w')
        nd = f.read()
        print(nd)

    def __str__(self):
        return "Fullname : "+self.fullname+", Age : "+self.age+", Gender : "+self.gender+", Address :"+self.address+", Task of worker : "+self.task+"."
ListOfficer = []


def inputrank(self):
    check = True
    while (check):
        rank = int(input("Enter rank : "))
        if (rank > 0) and (rank < 10):
            check = False
        else:
            check = True
            print("Invalid , let's try again . ")
    return rank
class ManageOfficer :
    def insertOfficer(self):
        check = True
        print("List type of officer.")
        print("1. Worker .")
        print("2. Engineer .")
        print("3. Staff .")
        print("4. Exit")
        while(check) :
            print("Enter the information : ")
            fullname = input(" Name : ")
            age = int(input(" Age : "))
            gender = input(" Gender : ")
            address = input(" Address : ")
            choice = int(input("Enter your choice : "))
            if choice == 1 :
                rank = inputrank()
                op = worker(fullname,age,gender,address,rank)
                ListOfficer.append(op)
                op.writeinputfile(fullname,age,gender,address,rank)
            elif choice == 2 :
                branch = input("Enter branch : ")
                op = engineer(fullname,age,gender,address,branch)
                ListOfficer.append(op)
                op.writeinputfile(fullname,age,gender,address,branch)
            elif choice == 3 :
                task = input("Enter task : ")
                op = staff(fullname,age,gender,address,task)
                ListOfficer.append(op)
                op.writeinputfile(fullname,age,gender,address,task)
            elif choice == 4 :
                check = False
            else :
                print("Invalid")

        print("======================================")
    def searchbyname(self):
        name = input("Enter name need to search : ")
        for op in ListOfficer :
            if op.getFullname() == name :
                print(op)
    def showinformation(self):
        for op in ListOfficer :
            op.readinputfile()
if __name__ == "__main__" :
    ck = True
    print("List Operation With Officers : ")
    print("1. Insert officer .")
    print("2. Show information of Officer .")
    print("3. Search information of person by name .")
    print("4. Exit ")
    mo = ManageOfficer()
    while(ck) :
        ch = int(input("Enter your choice : "))
        if ch == 1 :
            mo.insertOfficer()
        elif ch == 2 :
            mo.showinformation()
        elif ch == 3 :
            mo.searchbyname()
        elif ch == 4 :
            ck = False
        else :
            print("Invalid, Let's try again .")
    print("============================================================================")
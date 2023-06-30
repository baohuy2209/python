"""
Để quản lý hồ sơ học sinh của trường THPT nhà trường cần các thông tin sau: Lớp,  và các thông tin về cá nhân của mỗi học sinh.

Mỗi học sinh có các thông tin sau: Họ tên, tuổi, quê quán.

Yêu cầu 1: Xây dựng HocSinh để quản lý thông tin của mỗi học sinh.

Yêu cầu 2: Xây dựng các phương thức thêm, hiển thị thông tin của mỗi học sinh.

Yêu cầu 3: Cài đặt chương trình có các chức năng sau:

Thêm học sinh mới.
Hiện thị các học sinh 20 tuổi.
Cho biết số lượng các học sinh có tuổi là 23 và quê ở DN.
"""

class Student:
    def __init__(self, fullname:str, age:int, address:str):
        self.fullname = fullname
        self.age = age
        self.address = address

class Filestudent(Student):
    def __init__(self, fullname:str, age:str, address:str, grade:int):
        Student .__init__(fullname,fullname, age, address)
        self.grade = grade


lststd = []


class Management:

    def insert(self):


    def show(self):


    def show20(self):


    def edit(self):



    def remove(self):


    def showDN23(self):



if __name__ == "__main__":
    print("List operation with list pofile of student  : ")
    print("1. Inserting student .")
    print("2. Showing information of student .")
    print("3. Removing out list .")
    print("4. Editing information .")
    print("5. Showing students 20 years old ")
    print("6. show the number of students who are 23 years old and come from Da Nang province")
    print("7. Write in file .")
    print("8. Read a file ")
    print("9. Exit loop .")
"""
Các thí sinh dự thi đại học bao gồm các thí sinh thi khối A, B, và khối C. Các thí sinh cần quản lý các thông tin sau: Số báo danh, họ tên, địa chỉ, mức ưu tiên.

Thí sinh thi khối A thi các môn: Toán, Lý, Hoá.

Thí sinh thi khối B thi các môn: Toán, Hoá, Sinh.

Thí sinh thi khối C thi các môn: Văn, Sử, Địa.

Yêu cầu 1: Xây dựng các lớp để quản lý các thi sinh dự thi đại học.

Yêu cầu 2: Xây dựng lớp TuyenSinh có các chức năng:

Thêm mới thí sinh.
Hiện thị thông tin của thí sinh và khối thi của thí sinh.
Tìm kiếm theo số báo danh.
Thoát khỏi chương trình.
"""

class Constant:
    def __init__(self, sbd:str, fullname:str, address:str, prior:str):
        self.sbd = sbd
        self.fullname = fullname
        self.address = address
        self.prior = prior


class Blocka(Constant):
    def __init__(self, sbd:str, fullname:str, address:str, prior:str, math:float, physical:float, chemical:float):
        Constant .__init__(self, sbd, fullname, address, prior)
        self.math = math
        self.physical = physical
        self.chemical = chemical


class Blockb(Constant):
    def __init__(self, sbd:str, fullname:str, address:str, prior:str, math:float, chemical:float, biology:float):
        Constant .__init__(self, sbd, fullname, address, prior)
        self.math = math
        self.chemical = chemical
        self.biology = biology



class Blockc:
    def __init__(self, sbd:str, fullname:str, address:str, prior:str, literature:float, historical:float, geography:float):
        Constant .__init__(self, sbd, fullname, address, prior)
        self.literature = literature
        self.historical = historical
        self.geography = geography



listA = []
listB = []
listC = []


class Management:
    def insert(self):


    def show(self):


    def searchsbd(self):



    def remove(self):



if __name__ == "__main__":

    print("List operation with list student : ")
    print("1. Inserting student .")
    print("2. Showing information of student .")
    print("3. Removing out list .")
    print("4. Editing information .")
    print("5. Searching by SBD")
    print("6. Searching by name ")
    print("7. Searching by address ")
    print("8. Write in file .")
    print("9. Read a file ")
    print("10. Exit loop .")

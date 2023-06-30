"""
Để quản lý các hộ dân cư trong một khu phố, người ta cần các thông tin sau: Số thành viên trong gia đình, Số nhà, thông tin mỗi cá nhân trong gia đình.
Với mỗi cá nhân, người ta quản lý các thông tin sau: Họ tên, Tuổi, Nghề nghiệp, số chứng minh nhân dân(duy nhất cho mỗi người).

Yêu cầu 1: Hãy xây dựng lớp Nguoi để quản lý thông tin của mỗi cá nhân.

Yêu cầu 2: Xây dựng lớp HoGiaDinh để quản lý thông tin của từng hộ gia đình.

Yêu cầu 2: Xây dựng lớp KhuPho để quản lý các thông tin của từng hộ gia đình.

Yêu cầu 3: Nhập n hộ dân. (n nhập từ bàn phím), hiển thị thông tin của các hộ trong khu phố.
"""

class Private:
    def __init__(self, fullname, age, job, cmnd):
        self.fullname = fullname
        self.age = age
        self.job = job
        self.cmnd = cmnd



class household(Private):
    def __init__(self, no_mem:int, address:str , lstmem : list[object]):
        self.no_mem = no_mem
        self.address = address
        self.lstmem = lstmem


class Management:
    def insert(self):


    def edit(self):



    def remove(self):


    def searchbyaddress(self):


if __name__ == "__main__":
    print("List operation with list household : ")
    print("1. Inserting household .")
    print("2. Showing information of households .")
    print("3. Removing out list .")
    print("4. Editing information .")
    print("5. Searching by address ")
    print("6. Write in file .")
    print("7. Read a file ")
    print("8. Exit loop .")
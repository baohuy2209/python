"""#Để quản lý biên lai thu tiền điện, người ta cần các thông tin sau:

#Với mỗi biên lai: Thông tin về hộ sử dụng điện, chỉ số điện cũ, chỉ số mới, số tiền phải trả.
#Các thông tin riêng của từng hộ gia đình sử dụng điện: Họ tên chủ hộ, số nhà, mã số công tơ điện.
#Yêu cầu 1: Hãy xây dựng lớp khachHang để lưu trữu các thông tin riêng của mỗi hộ gia đình.

#Yêu cầu 2: Xây dựng lớp BienLai để quản lý việc sử dụng và thanh toán tiền điện của các hộ dân.

#Yêu cầu 3: Xây dựng các phương thức thêm, xoá sửa các thông tin riêng của mỗi hộ sử dụng điện.

#Yêu cầu 4: Viết phương thức tính tiền điện cho mỗi hộ gia đình theo công thức: (số mới – số cũ ) * 5.
"""

class Client(object):
    def __init__(self, headhouse, apartment, eleccode):
        self.headhouse = headhouse
        self.apartment = apartment
        self.eleccode = eleccode


class Receipt(Client):
    def __init__(self, headhouse, apartment, eleccode, oldindex, newindex,):
        Client .__init__(headhouse, apartment, eleccode)
        self.oldindex = oldindex
        self.newindex = newindex

    def getcost(self, oldindex, newindex):
        return (newindex - oldindex)*5

    def __repr__(self):
        return "Name of head of household : "+self.headhouse+"Apartment number : "+self.apartment+"Electric meter code : "+self.eleccode+"Old index of electric meter : "+self.oldindex+"New index of electric meter : "+self.newindex+" The money have to pay receipt : "+self.getcost()


listreceipt = []


def inputinformation() :
    print("Enter the information : ")
    headhouse = input("Name of head of household : ")
    apartment = int(input("Apartment number : "))
    eleccode = input("Electric meter code : ")
    oldindex = float(input("Old index of electric meter : "))
    newindex = float(input("New index of electric meter : "))
    obj = Receipt(headhouse, apartment, eleccode, oldindex, newindex)
    return obj


class Managementreceipt:
    def insert(self):
        recei = inputinformation()
        listreceipt.append(recei)

    def edit(self):
        name = input("Enter name of head of household which you want to edit information : ")
        for item in listreceipt:
            if name == item.headhouse:
                item = inputinformation()

    def remove(self):
        name = input("Enter name of head of household which you want to remove information : ")
        for item in listreceipt:
            if name == item.headhouse:
                listreceipt.remove(item)

    def show(self):
        for item in listreceipt:
            print(repr(item))


if __name__ == "__main__":

    print("List of operation : ")
    print("1. Insert repcepit ")
    print("2. Edit information ")
    print("3. Remove repcepit ")
    print("4. Show all information ")
    print("5. See the electricity price of households ")
    print("6. Exit")
    mr = Managementreceipt()
    check = True
    while (check):
        choice = int(input("Enter the choice : "))
        if choice == 1:
            mr.insert()
        elif choice == 2:
            mr.edit()
        elif choice == 3:
            mr.remove()
        elif choice == 4:
            mr.show()
        elif choice == 5:
            for item in listreceipt:
                print("Name of head of household : ", item.headhouse, " The money have to pay receipt : ", item.getcost())
        elif choice == 5:
            check = False
        else:
            raise Exception("Invalid")
    print("===========================================================================")

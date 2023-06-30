#Nghành công an cần quản lý các phương tiện giao thông gồm: ô tô, xe máy, xe tải.
#Mỗi loại gồm các thông tin: ID, Hãng sản xuất, năm sản xuất, giá bán và màu xe.

#Các ô tô có các thuộc tính riêng: số chỗ ngồi, kiểu động cơ.

#Các xe máy có các thuộc tính riêng: công xuất.

#Xe tải cần quản lý thêm: Trọng tải.

#Yêu cầu 1: Xây dựng các lớp để quản lý các phương tiện trên sao cho hiệu quả.

#Yêu cầu 2: Xây dựng lớp QLPTGT có các chức năng:

#Thêm, xoá(theo ID) các phương tiện thuộc các loại trên.
#Tìm phương tiện theo hãng sản xuất, màu.
#Thoát chương trình.
class Date :
    def __init__(self,day,month,year):
        self.day = day
        self.month = month
        self.year = year
    def getDay(self):
        return self.day
    def setDay(self,day):
        self.day = day
    def getMonth(self):
        return self.day
    def setMonth(self,month):
        self.month = month
    def getYear(self):
        return self.year
    def setYear(self,year):
        self.year = year
    def __str__(self):
        return self.day+"//"+self.month+"//"+self.year

# HSX : hãng sản xuất
# NSX : năm sản xuất
# Cost : giá tiền mua xe
# color : màu sắc xe
class Vehicle (object) :
    def __init__(self,ID,HSX,NSX,cost,color):
        self.ID = ID
        self.HSX = HSX
        self.NSX = NSX
        self.cost = cost
        self.color = color
    def getID(self):
        return self.ID
    def setID(self,ID):
        self.ID = ID
    def getHSX(self):
        return self.HSX
    def setHSX(self, HSX):
        self.HSX = HSX
    def getNSX(self):
        return self.NSX
    def setNSX(self, NSX):
        self.NSX = NSX
    def getCost(self):
        return self.cost
    def setCost(self, cost):
        self.cost = cost
    def getColor(self):
        return self.color
    def setColor(self,color):
        self.color = color
# no_seat : số chỗ ngồi
# Engine_type : loại động cơ
class Car (Vehicle) :
    def __init__(self,ID,HSX,NSX,cost,color,no_seat,engine_type) :
        Vehicle .__init__(ID,HSX,NSX,cost,color)
        self.no_seat = no_seat
        self.engine_type = engine_type
    def getNo_seat(self) :
        return self.no_seat
    def setNo_seat(self,no_seat):
        self.no_seat = no_seat
    def getEngine_type(self):
        return self.engine_type
    def setEngine_tyoe(self,engine_type):
        self.engine_type = engine_type
class Motorbike (Vehicle) :
    def __init__(self, ID, HSX, NSX, cost, wattage) :
        Vehicle .__init__(ID,HSX,NSX,cost)
        self.wattage = wattage # wattage : công suất xe
    def getWattage(self):
        return self.wattage
    def setWattage(self,wattage):
        self.wattage = wattage
ListVehicle = []
class Manage_Vehicle :
    def insertVehicle(self):
        print("Type of vehicle .")
        print("1. Motorbike ")
        print("2. Car")
        print("3. Exit ")
        check = True
        while(check) :
            ch = int(input("Enter your type of vehicle you want to insert"))
            if ch == 1 :
                ID = int(input("Enter ID : "))
                day1 = int(input("Enter day of HSX : "))
                month1 = int(input("Enter month of HSX : "))
                year1 = int(input("Enter year of HSX : "))
                hsx = date(day1,month1,year1)
                day2 = int(input("Enter day of HSX : "))
                month2 = int(input("Enter month of HSX : "))
                year2 = int(input("Enter year of HSX : "))
                nsx = date(day2, month2, year2)
                cost = int(input("Enter cost of vehicle : "))
                color = input("Enter color : ")
                wattage = int(input("Enter wattage : "))
                op = Motorbike(ID,hsx,nsx,cost,color,wattage)
                ListVehicle.append(op)
            elif ch == 2 :
                ID = int(input("Enter ID : "))
                day1 = int(input("Enter day of HSX : "))
                month1 = int(input("Enter month of HSX : "))
                year1 = int(input("Enter year of HSX : "))
                hsx = date(day1, month1, year1)
                day2 = int(input("Enter day of HSX : "))
                month2 = int(input("Enter month of HSX : "))
                year2 = int(input("Enter year of HSX : "))
                nsx = date(day2, month2, year2)
                cost = int(input("Enter cost of vehicle : "))
                color = input("Enter color : ")
                no_seat = int(input("Enter wattage : "))
                engine_type = int(input("Enter Engine tyoe "))
                op = Car(ID, hsx, nsx, cost, color, no_seat, engine_type)
                ListVehicle.append(op)
            elif ch == 3 :
                check = False ;
            else :
                print("Invalid. Let's try again ")
    def deleteVehicle(self):
        index = int(input("Enter the index"))
        i = 0
        for op in ListVehicle :
            if i == index :
                ListVehicle.pop(i)
            i += 1
        print("List after delete : ")
        for op in ListVehicle :
            print(op)

    def searchbyHSX(self):
        hsx1 = input("Enter HSX to find : ")
        for op in ListVehicle :
            if op.getHSX() == hsx1 :
                print(op)

    def searchbyColor(self):
        color1 = input("Enter HSX to find : ")
        for op in ListVehicle:
            if op.getColor() == color1:
                print(op)
if __name__ == "__main__" :
    print("List operation.")
    print("1. Insert Vehicle.")
    print("2. Delete Vehicle.")
    print("3. Search vehicle by HSX.")
    print("4. Search Vehicle by color.")
    print("5. Exit")
    mv = Manage_Vehicle()
    ch = True
    while(ck) :
        choice = int(input("Enter your choice : "))
        if choice == 1 :
            mv.insertVehicle()
        elif choice == 2 :
            mv.deleteVehicle()
        elif choice == 3 :
            mv.searchbyHSX()
        elif choice == 4 :
            mv.searchbyColor()
        elif choice == 5 :
            check = False
        else :
            print("Invalid")
    print("\n")
"""
Thiết kế class Rectangle theo sơ đồ trên gồm:

Constructor mặc định và constructor có 2 tham số length, width để gán giá trị cho 2 thuộc tính tương ứng của Rectangle.
setLength(length: int): gán giá trị cho thuộc tính length của class.
getLength(): Trả về giá trị length của class.
setWidth(width: int): gán giá trị cho thuộc tính width của class.
getWidth(): Trả về giá trị width của class.
getArea(): Tính diện tích của Rectangle
toString(): Trả về chuỗi thông tin cần thiết của Rectangle như length, width.
"""


class Rectangle:
    def __init__(self, length:float, width:float ):
        self.length = length
        self.width = width

    def getlength(self):
        return self.length

    def setlength(self,length):
        self.length = length

    def getwidth(self):
        return self.width

    def setwidth(self,width):
        self.width = width

    def getarea(self):
        return self.width*self.length

    def __repr__(self):
        return "Area of rectangle : "+str(self.getarea())

if __name__ == "__main__":
    length = float(input("Enter the length : "))
    width = float(input("Enter the width : "))
    cr = Rectangle(length,width)
    print(repr(cr))
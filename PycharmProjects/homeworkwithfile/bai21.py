"""
Cho class Circle được thiết kế theo, có chứa:

Hai biến private (-): radius có kiểu dữ liệu là double, và color là String. Hai thuộc tính có có giá trị mặc định khi khởi tạo là radius = 1.0 và color = red.
Ba constructor trong đó có 1 constructor mặc định sẽ khởi tạo giá trị mặc định cho radius và red là 1.0 và red. Các constructor Circle(radius: double) sẽ khởi tạo giá trị cho radius và color là red. Circle(radius: double, color: String) sẽ khởi tạo giá trị cho cả radius và color.
getRadius() và setRadius(radius: double) là 2 hàm lấy và gán giá trị mới cho radius.
getColor và setColor(color: String) là 2 hàm gán và lấy giá trị mới cho color.
getArea(): dùng để tính diện tích hình tròn.
toString(): Trả về thông tin của radius và color ra màn hình console.
"""
import math


class Circle:

    def __init__(self,radius,color):
        self.radius = radius
        self.color = color

    def getradius(self):
        return self.radius

    def setradius(self,radius):
        self.radius = radius

    def getcolor(self):
        return self.color

    def setcolor(self,color):
        self.color = color

    def getarea(self):
        return self.radius**2*math.pi

    def __repr__(self):
        return "Area of circle: "+str(self.getarea())

if __name__ == "__main__":
    radi = float(input("Enter the radius : "))
    color = input("Enter the color : ")
    cr = Circle(radi,color)
    print(repr(cr))
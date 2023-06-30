"""
#Tính chu vi & diệntích các hình (abstract)

#Viết chương trình tính chu vi và điện tích của một số hình như sau:

# + Hình tròn
# + Hình chữ nhật
# + Hình tam giac
"""
class Circle(object) :
    def __init__(self,radius):
        self.radius = radius
    def getArea(self,radius):
        return self.radius**2*3.14
    def getParameter(self,radius):
        return 2*self.radius*3.14
    def writefile(self,radius):
        cr = Circle(radius)
        f = open('Circle.txt','w')
        f.write("Ban kinh : ")
        f.write(str(radius))
        f.write("\n")
        f.write("Area of cirle : ")
        f.write(str(cr.getArea(radius)))
        f.write("\n")
        f.write("Parameter of Circe : ")
        f.write(str(cr.getParameter(radius)))
        f.write("\n")
    def readfile(self):
        f = open('Circle.txt','r')
        nd = f.read()
        print(nd)
class Rectangle(object) :
    def __init__(self,width,length):
        self.width = width
        self.length = length

    def getArea(self,width,length):
        return self.width*self.length
    def getParameter(self,width,length):
        return (self.width + self.length)*2

    def writefile(self,width,length):
        cr = Rectangle(width,length)
        f = open('Rectangle.txt','w')
        f.write("Chieu dai : ")
        f.write(str(width))
        f.write("\n")
        f.write("Chieu rong : ")
        f.write(str(length))
        f.write("\n")
        f.write("Area of Rectangle : ")
        f.write(str(cr.getArea(width,length)))
        f.write("\n")
        f.write("Parameter of Rectangle : ")
        f.write(str(cr.getParameter(width,length)))
        f.write("\n")
def readfile(self):
        f = open('Circle.txt','r')
        nd = f.read()
        print(nd)
class Square(object):
    def __init__(self, z):
        self.z = z

    def getArea(self,z):
        return self.z**2

    def getParameter(self,z):
        return 4*self.z
    def writefile(self,z):
        cr = Square(z)
        f = open('Square.txt','w')
        f.write("Kich thuoc hinh vuong : ")
        f.write(str(z))
        f.write("\n")
        f.write("Area of Square : ")
        f.write(str(cr.getArea(z)))
        f.write("\n")
        f.write("Parameter of Square : ")
        f.write(str(cr.getParameter(z)))
        f.write("\n")
    def readfile(self):
        f = open('Circle.txt','r')
        nd = f.read()
        print(nd)

if __name__ == '__main__':
    r = int(input("Enter radius : "))
    a = Circle(r)
    a.writefile(a)
    a.readfile()


    x = int(input("Enter width :"))
    y = int(input("Enter length : "))
    b = Rectangle(x,y)
    b.writefile(x,y)
    b.readfile() 
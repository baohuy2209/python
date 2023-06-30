"""#Xây dựng lớp SoPhuc có các thuộc tính PhanThuc, PhanAo kiểu double.
#Yêu cầu 1: Xây dựng các phương thức tạo lập
#Yêu cầu 2: Xây dựng các phương thức:
#Nhập một số phức.
#Hiện thị số phức.
#Cộng 2 số phức.
#Nhân 2 số phức.
"""
class complexnumber(object) :
    def __init__(self,real,virtual):
        self.real = real
        self.virtual = virtual
    def getReal(self):
        return self.real
    def setReal(self,real):
        self.real = real
    def getVirtual(self):
        return self.virtual
    def setVirtual(self,virtual):
        self.virtual = virtual
    def __str__(self):
        return str(self.real)+' + '+str(self.virtual)+'*i '
    def writefileinput(self,real,virtual):
        f = open("Input.txt","w")
        f.write("Complex Number is entered : ")
        f.write(str(real))
        f.write("+")
        f.write(str(virtual))
        f.write("*i")
        f.write("\n")
        f.close()
    def readfileinput(self):
        f = open('Input.txt','r')
        nd = f.read()
        print(nd)
    def writefileoutput(self,real,virtual):
        f = open("Output.txt","w")
        f.write("result : ")
        f.write(str(real))
        f.write("+")
        f.write(str(virtual))
        f.write("*i")
        f.write("\n")
        f.close()
    def readfileoutput(self):
        f = open('Output.txt','r')
        nd = f.read()
        print(nd)
class Operation :
    def addition(self):
        real1 = int(input("Enter real part of first comlex_number : "))
        virtual1 = int(input("Enter virtual part of first complex_number: "))
        cn1 = complexnumber(real1,virtual1)
        cn1.writefileinput(real1,virtual1)
        cn1.readfileinput()
        real2 = int(input("Enter real part of second complex_number : "))
        virtual2 = int(input("Enter virtual part of second complex_number: "))
        cn2 = complexnumber(real2,virtual2)
        cn2.writefileinput(real2, virtual2)
        cn2.readfileinput()
        cn3 = complexnumber(cn1.getReal()+cn2.getReal(),cn1.getVirtual()+cn2.getVirtual())
        cn3.writefileoutput(cn1.getReal()+cn2.getReal(),cn1.getVirtual()+cn2.getVirtual())
        cn3.readfileoutput()
    def subtraction(self):
        real1 = int(input("Enter real part of first comlex_number : "))
        virtual1 = int(input("Enter virtual part of first complex_number: "))
        cn1 = complexnumber(real1, virtual1)
        cn1.writefileinput(real1, virtual1)
        cn1.readfileinput()
        real2 = int(input("Enter real part of second complex_number : "))
        virtual2 = int(input("Enter virtual part of second complex_number: "))
        cn2 = complexnumber(real2, virtual2)
        cn2.writefileinput(real2, virtual2)
        cn2.readfileinput()
        cn3 = complexnumber(cn1.getReal() - cn2.getReal(), cn1.getVirtual() - cn2.getVirtual())
        cn3.writefileoutput(cn1.getReal() - cn2.getReal(), cn1.getVirtual() - cn2.getVirtual())
        cn3.readfileoutput()
    def multiplication(self):
        real1 = int(input("Enter real part of first comlex_number : "))
        virtual1 = int(input("Enter virtual part of first complex_number: "))
        cn1 = complexnumber(real1, virtual1)
        cn1.writefileinput(real1, virtual1)
        cn1.readfileinput()
        real2 = int(input("Enter real part of second complex_number : "))
        virtual2 = int(input("Enter virtual part of second complex_number: "))
        cn2 = complexnumber(real2, virtual2)
        cn2.writefileinput(real2, virtual2)
        cn2.readfileinput()
        cn3 = complexnumber(cn1.getReal()*cn2.getReal() - cn1.getVirtual()*cn2.getVirtual(), cn1.getReal()*cn2.getVirtual() + cn1.getVirtual()*cn2.getReal())
        cn3.writefileoutput(cn1.getReal()*cn2.getReal() - cn1.getVirtual()*cn2.getVirtual(), cn1.getReal()*cn2.getVirtual() + cn1.getVirtual()*cn2.getReal())
        cn3.readfileoutput()
    def division(self):
        real1 = int(input("Enter real part of first comlex_number : "))
        virtual1 = int(input("Enter virtual part of first complex_number: "))
        cn1 = complexnumber(real1, virtual1)
        real2 = int(input("Enter real part of second complex_number : "))
        virtual2 = int(input("Enter virtual part of second complex_number: "))
        cn2 = complexnumber(real2, virtual2)
        cn3 = complexnumber((cn1.getReal()*cn2.getReal() + cn1.getVirtual()*cn2.getVirtual())/(cn2.getReal()**2 + cn2.getVirtual()**2),(cn1.getVirtual()*cn2.getReal() - cn1.getReal()*cn2.getVirtual())/(cn2.getReal()**2 + cn2.getVirtual()**2))
        print("Result (cn1/cn2) : ", cn3)
if __name__ == '__main__':
    op = Operation()
    print("1. Addition of two complex_number")
    print("2. Substraction of two complex_number")
    print("3. Multiplication of two complex_number")
    print("4. Division of two complex_number")
    print("5. Exit ")
    check = True
    while(check) :
        choice = int(input("Enter choice : "))
        if choice == 1 :
            op.addition()
        elif choice == 2 :
            op.subtraction()
        elif choice == 3 :
            op.multiplication()
        elif choice == 4 :
            op.division()
        elif choice == 5 :
            check = False
        else :
            print("Invalid , try again ")
    print("End programming ")

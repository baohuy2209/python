class fraction(object) :
    def __init__(self,numerator,denominator):
        self.numerator = numerator
        self.denominator = denominator
    def getNumerator(self):
        return self.numerator
    def setNumerator(self,numerator):
        self.numerator = numerator
    def getDenominator(self):
        return self.denominator
    def setDenominator(self,denominator):
        self.denominator = denominator
    def __str__(self):
        return str(self.numerator)+'/'+str(self.denominator)
    def writefileinput(self,numerator,denominator):
        f = open("Inputfraction.txt","w")
        f.write("Fraction is entered : ")
        f.write(str(numerator))
        f.write("/")
        f.write(str(denominator))
        f.write("\n")
        f.close()
    def readfileinput(self):
        f = open('Inputfraction.txt','r')
        nd = f.read()
        print(nd)
    def writefileoutput(self,numerator,denominator):
        f = open("Outputfraction.txt","w")
        f.write("result : ")
        f.write(str(numerator))
        f.write("/")
        f.write(str(denominator))
        f.write("\n")
        f.close()
    def readfileoutput(self):
        f = open('Outputfraction.txt','r')
        nd = f.read()
        print(nd)

class operation :
    def addition(self):
        numerator1 = int(input("Enter numerator part of first fraction : "))
        denominator1 = int(input("Enter denominator part of first fraction : "))
        cn1 = fraction(numerator1, denominator1)
        cn1.writefileinput(numerator1, denominator1)
        cn1.readfileinput()
        numerator2 = int(input("Enter numerator part of second fraction : "))
        denominator2 = int(input("Enter denominator part of second fraction: "))
        cn2 = fraction(numerator2, denominator2)
        cn2.writefileinput(numerator2, denominator2)
        cn2.readfileinput()
        if cn1.getDenominator() == cn2.getDenominator() :
            a = cn1.getNumerator() + cn2.getNumerator()
            b = cn1.getDenominator()
            cn3 = fraction(a,b)
        else :
            a = cn1.getNumerator()*cn2.getDenominator() + cn2.getNumerator()*cn1.getDenominator()
            b = cn1.getDenominator()*cn2.getDenominator()
            cn3 = fraction(a,b)
        cn3.writefileoutput(a,b)
        cn3.readfileoutput()
    def substraction(self):
        numerator1 = int(input("Enter numerator part of first fraction : "))
        denominator1 = int(input("Enter denominator part of first fraction : "))
        cn1 = fraction(numerator1, denominator1)
        cn1.writefileinput(numerator1, denominator1)
        cn1.readfileinput()
        numerator2 = int(input("Enter numerator part of second fraction : "))
        denominator2 = int(input("Enter denominator part of second fraction: "))
        cn2 = fraction(numerator2, denominator2)
        cn2.writefileinput(numerator2, denominator2)
        cn2.readfileinput()
        if cn1.getDenominator() == cn2.getDenominator():
            a = cn1.getNumerator() - cn2.getNumerator()
            b = cn1.getDenominator()
            cn3 = fraction(a, b)
        else:
            a = cn1.getNumerator() * cn2.getDenominator() - cn2.getNumerator() * cn1.getDenominator()
            b = cn1.getDenominator() * cn2.getDenominator()
            cn3 = fraction(a, b)
        cn3.writefileoutput(a, b)
        cn3.readfileoutput()

    def multiplication(self):
        numerator1 = int(input("Enter numerator part of first fraction : "))
        denominator1 = int(input("Enter denominator part of first fraction : "))
        cn1 = fraction(numerator1, denominator1)
        cn1.writefileinput(numerator1, denominator1)
        cn1.readfileinput()
        numerator2 = int(input("Enter numerator part of second fraction : "))
        denominator2 = int(input("Enter denominator part of second fraction: "))
        cn2 = fraction(numerator2, denominator2)
        cn2.writefileinput(numerator2, denominator2)
        cn2.readfileinput()
        a = cn1.getNumerator() * cn2.getNumerator()
        b = cn1.getDenominator() * cn2.getDenominator()
        cn3 = fraction(a, b)
        cn3.writefileoutput(a, b)
        cn3.readfileoutput()

    def division(self):
        numerator1 = int(input("Enter numerator part of first fraction : "))
        denominator1 = int(input("Enter denominator part of first fraction : "))
        cn1 = fraction(numerator1, denominator1)
        cn1.writefileinput(numerator1, denominator1)
        cn1.readfileinput()
        numerator2 = int(input("Enter numerator part of second fraction : "))
        denominator2 = int(input("Enter denominator part of second fraction: "))
        cn2 = fraction(numerator2, denominator2)
        cn2.writefileinput(numerator2, denominator2)
        cn2.readfileinput()
        a = cn1.getNumerator() * cn2.getDenominator()
        b = cn1.getDenominator() * cn2.getNumerator()
        cn3 = fraction(a, b)
        cn3.writefileoutput(a, b)
        cn3.readfileoutput()
if __name__ == "__main__" :
    op = operation()
    print("1. Addition of two fraction")
    print("2. Substraction of two fraction")
    print("3. Multiplication of two fraction")
    print("4. Division of two fraction")
    print("5. Exit ")
    check = True
    while (check):
        choice = int(input("Enter choice : "))
        if choice == 1:
            op.addition()
        elif choice == 2:
            op.subtraction()
        elif choice == 3:
            op.multiplication()
        elif choice == 4:
            op.division()
        elif choice == 5:
            check = False
        else:
            print("Invalid , try again ")
    print("End programming ")

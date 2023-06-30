#class for the computer Science Student

class CSStudent :
    stream = 'cse '
    def __init__(self,name,roll):
        self.name = name
        self.roll = roll

#New object for further implementation
a = CSStudent("check",3)
print("a.stream =",a.stream)
#Corect way to change the value of class variable
CSStudent.stream = "mec"
print("\n Class variable changes to mec")
#New object for further implementation
b = CSStudent("carter",4)
print("\n Value of variable stream for each object")
print("a.stream =",a.stream)
print("b.stream =",b.stream)

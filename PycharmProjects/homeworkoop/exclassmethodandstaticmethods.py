class CSStudent (object) :
    stream = 'cse'
    def __init__(self,name,roll):
        self.name = name
        self.roll = roll

#Driver program to text the functionallity
    #Creating objects of CSStudent class
a = CSStudent("Cafevn",1)
b = CSStudent("Nerd",2)
print("Initially")
print("a.stream = ",a.stream)
print("b.stream =",b.stream)

#thí thing does'nt change class(static) variable
#Instead creates instance variable for the object
# 'a ' that shadows class member .
a.stream = "ece"
print("\n After changing a.stream")
print("a.stream =",a.stream)
print("b.stream =",b.stream)


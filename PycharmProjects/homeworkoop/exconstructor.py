class Addition :
    first = 0
    second = 0
    answer = 0

    def __init__(self,f,s):
        self.first = f
        self.second = s

    def display(self):
        print("First number = "+str(self.first))
        print("Second number = "+str(self.second))
        print("Addition of two number = "+str(self.answer))

    def calculate(self):
        self.answer = self.first + self.second

#Creating object of the class
#this will invoke parameterized constructor
obj = Addition(1000,2000)
obj.calculate()
obj.display()
from input_information_for_example import Input_information


class Person (object) :
    def __init__(self,fullname,age,gender,address) :
        self.fullname = fullname
        self.age = age
        self.gender = gender
        self.address = address
        self.input = Input_information()
        
    def getFullname(self):
        return self.fullname

    def setFullname(self,fullname):
        self.fullname = fullname

    def getAge(self):
        return self.age

    def setAge(self,age):
        self.age = age

    def getGender(self):
        return self.gender

    def setGender(self,gender):
        self.gender = gender

    def getAddress(self):
        return self.address

    def setAddress(self,address):
        self.address = address

    def __str__(self):
        return "Fullname :"+str(self.fullname)+" Age : "+str(self.age)+" Gender : "+str(self.gender)+" Address : "+str(self.address)+"."


if __name__ == "__main__":
    print("Enter the information :")
    with open('classperson.txt','r') as obj:
        fullname = obj.readline()
        age = obj.readline()
        gender = obj.readline()
        address = obj.readline()
        fullname1 = obj.readline()
        age1 = obj.readline()
        gender1 = obj.readline()
        address1 = obj.readline()
    per1 = Person(fullname, age, gender, address)
    per2 = Person(fullname1, age1, gender1, address1)
    l = []
    l.append(per1)
    l.append(per2)
    for i in l:
        print(str(i))
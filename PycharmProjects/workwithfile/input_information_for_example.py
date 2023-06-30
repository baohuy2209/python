class Input_information:

    def input(self,fullname,age,gender,address):
        f = open('text1.txt','w')
        f.write(str(fullname)+"\n")
        f.write(str(age)+"\n")
        f.write(str(gender)+"\n")
        f.write(str(address)+"\n")
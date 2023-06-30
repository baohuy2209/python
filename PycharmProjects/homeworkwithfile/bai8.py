import datetime
from certificate import Certificate


class Employee(object):
    def __init__(self, id, fullname, birthday, phone, email, rank, date):
        self.id = id
        self.fullname = fullname
        self.birthday = birthday
        self.phone = phone
        self.email = email
        self.rank = rank  # Thu hang bang cap
        self.date = date  # Ngay nhan bang
        self.certificate = Certificate(self.id, self.fullname, self.rank, self.date)

    def getid(self):
        return self.id

    def setid(self, id):
        self.id = id

    def getfullname(self):
        return self.fullname

    def setfullname(self, fullname):
        self.fullname = fullname

    def getbirthday(self):
        return self.birthday

    def setbirthday(self, birthday):
        self.birthday = birthday

    def getphone(self):
        return self.phone

    def setphone(self, phone):
        self.phone = phone

    def getemail(self):
        return self.email

    def setemail(self, email):
        self.email = email

    def output(self):
        print("ID : ", self.id)
        print("Fullname : ", self.fullname)
        print("Birthday : ", self.birthday)
        print("Phone : ", self.phone)
        print("Email : ", self.email)
        print("Certificates : ", self.certificate.getcertificate())


class Experience (Employee):
    def __init__(self, id, fullname, birthday, phone, email, rank, date, expinyear, proskill):
        Employee .__init__(self, id, fullname, birthday, phone, email, rank, date)
        self.expinyear = expinyear
        self.proskill = proskill

    def getexpinyear(self):
        return self.expinyear

    def setexpinyear(self, expinyear):
        self.expinyear = expinyear

    def getproskill(self):
        return self.proskill

    def setproskill(self, proskill):
        self.proskill = proskill

    def __repr__(self):
        return "ID : "+str(self.id)+" Fullname : "+self.fullname+" Birthday : "+str(self.birthday)+"Phone : "+str(self.phone)+"Email : "+self.email+" Certificates : "+str(self.certificate.getcertificate())+" Experience year :"+str(self.expinyear)+" Skill : "+self.proskill


class Fresher (Employee):
    def __init__(self, id, fullname, birthday, phone, email, rank, date, graduation_date, graduation_rank, education):
        Employee .__init__(self, id, fullname, birthday, phone, email, rank, date)
        self.graduation_date = graduation_date  # day whioh fresher pass
        self.graduation_rank = graduation_rank
        self.education = education  # where fresher studied

    def __repr__(self):
        return "ID : "+str(self.id)+" Fullname : "+self.fullname+" Birthday : "+str(self.birthday)+" Phone : "+str(self.phone)+" Email : "+self.email+" Certificates : "+str(self.certificate.getcertificate())+" Date which fresher graduate university :"+str(self.graduation_date)+" Rank of graduation : "+str(self.graduation_rank)+" University which person graduate : "+str(self.education)


class Intern (Employee):
    def __init__(self, id, fullname, birthday, phone, email, rank, date, majors, semester, universition_name):
        Employee .__init__(self, id, fullname, birthday, phone, email, rank, date)
        self.majors = majors
        self.semester = semester
        self.universition_name = universition_name

    def __repr__(self):
        return "ID : "+str(self.id)+" Fullname : "+self.fullname+" Birthday : "+str(self.birthday)+" Phone : "+str(self.phone)+" Email : "+self.email+" Certificates : "+str(self.certificate.getcertificate())+" Major"+str(self.majors)+" Sesmeter : "+self.semester+" University which intern is studying :"+self.universition_name


listExperience = []
listFresher = []
listIntern = []


def inputname():
    name = input("Enter the name :")
    ck = True
    while(ck):
        if name.isalpha() == False:
            raise Exception("Invalid , let's try again")
        else:
            ck = False
    return name


def inputemail():
    em = input("Enter the email : ")
    ck = True
    while(ck) :
        if "@gmail.com" not in em :
            raise Exception("Invalid , let's try again")
        else :
            ck = False
    return em


def inputDate():
    day = int(input("+ day :"))
    month = int(input("+ month :"))
    year = int(input("+ year : "))
    bir = datetime.date(year, month, day)
    return bir


def inputCertificate(n,fullname,id):
    lstcer = []  # list of certificates of this person
    for i in range(n):
        cerid = id
        cername = fullname
        cerrank = input("Rank of certificate: ")
        cerdate = inputDate()
        cer = Certificate(cerid, cername, cerrank, cerdate)
        lstcer.append(cer)
    return lstcer


def inputexperience():
    print("Enter the information of experience: ")
    id = int(input("ID : "))
    fullname = inputname()
    print("Birthday : ")
    birthday = inputDate()
    phone = int(input("Phone : "))
    email = inputemail()
    n = int(input("Enter number of certificates of this person : "))
    listcerti = inputCertificate(n, fullname, id)
    expinyear = int(input("Experience year : "))
    proSkill = input("Skill of this person : ")
    experience = Experience(id, fullname, birthday, phone, email, listcerti, expinyear, proSkill)
    return experience


def inputfresher():
    print("Enter the information of Fresher : ")
    id = int(input("ID : "))
    fullname = inputname()
    print("Birthday : ")
    birthday = inputDate()
    phone = int(input("Phone : "))
    email = inputemail()
    n = int(input("Enter number of certificates of this person : "))
    listcerti = inputCertificate(n, fullname, id)
    gra_date = inputDate()
    gra_rank = input("Rank of education : ")
    edu = input("Where training the fresher : ")
    fre = Fresher(id, fullname, birthday, phone, email, listcerti, gra_date, gra_rank, edu)
    return fre


def inputintern():
    print("Enter the information of Intern : ")
    id = int(input("ID : "))
    fullname = inputname()
    print("Birthday : ")
    birthday = inputDate()
    phone = int(input("Phone : "))
    email = inputemail()
    n = int(input("Enter number of certificates of this person : "))
    listcerti = inputCertificate(n, fullname, id)
    maj = input("Major : ")
    ses = input("Sesmeter : ")
    uni_name = input("University which this intern is studying : ")
    inte = Intern(id, fullname, birthday, phone, email, listcerti, maj, ses, uni_name)
    return inte


class Management:

    def insert(self):
        print("Type of employee : ")
        print("1. Experience")
        print("2. Fresher")
        print("3. Intern ")
        print("4. Exit")
        ck = True
        while(ck):
            choice = int(input("Enter the choice : "))
            if choice == 1:
                n = int(input("Enter the number of experience : "))
                with open('Experience.txt','r') as obj:
                    for i in range(n):
                        id = obj.readline()
                        fullname = obj.readline()
                        birthday = obj.readline()
                        phone = obj.readline()
                        email = obj.readline()
                        rank = obj.readline()
                        date = obj.readline()
                        expinyear = obj.readline()
                        proSkill = obj.readline()
                        experience = Experience(id, fullname, birthday, phone, email, rank, date, expinyear, proSkill)
                        listExperience.append(experience)
            elif choice == 2:
                n = int(input("Enter the number of Fresher : "))
                with open('Fresher.txt', 'r') as obj:
                    for i in range(n):
                        id = obj.readline()
                        fullname = obj.readline()
                        birthday = obj.readline()
                        phone = obj.readline()
                        email = obj.readline()
                        rank = obj.readline()
                        date = obj.readline()
                        gra_date = obj.readline()
                        gra_rank = obj.readline()
                        edu = obj.readline()
                        fre = Fresher(id, fullname, birthday, phone, email, rank, date, gra_date, gra_rank, edu)
                        listFresher.append(fre)
            elif choice == 3:
                n = int(input("Enter the number of Intern : "))
                with open('Intern.txt', 'r') as obj:
                    for i in range(n):
                        id = obj.readline()
                        fullname = obj.readline()
                        birthday = obj.readline()
                        phone = obj.readline()
                        email = obj.readline()
                        rank = obj.readline()
                        date = obj.readline()
                        maj = obj.readline()
                        ses = obj.readline()
                        uni_name = obj.readline()
                        inte = Intern(id, fullname, birthday, phone, email, rank, date, maj, ses, uni_name)
                        listIntern.append(inte)
            elif choice == 4:
                ck = False
            else:
                raise Exception("Invalid , try again ")

    def edit(self):
        print("Type of employee : ")
        print("1. Experience")
        print("2. Fresher")
        print("3. Intern ")
        print("4. Exit")
        ck = True
        while(ck):
            choice = int(input("Type of employee you want to edit infromation : "))
            if choice == 1:
                idexp = int(input("Enter id this experience : "))
                for item in listExperience:
                    if idexp == item.id:
                        new = inputexperience()
                        listExperience.append(new)
                        listExperience.remove(item)
            elif choice == 2:
                idfre = int(input("Enter id this fresher : "))
                for item in listFresher:
                    if idfre == item.id:
                        new = inputfresher()
                        listFresher.append(new)
                        listFresher.remove(item)
            elif choice == 3:
                idinte = int(input("Enter id this intern : "))
                for item in listIntern:
                    if idinte == item.id:
                        new = inputintern()
                        listIntern.append(new)
                        listIntern.remove(item)
            elif choice == 4:
                ck = False
            else:
                raise Exception("Invalid, let's try again ")

    def showinformation(self):
        print("Type of employee : ")
        print("1. Experience")
        print("2. Fresher")
        print("3. Intern ")
        print("4. Exit")
        ck = True
        while (ck):
            cho = int(input("Enter the choice : "))
            if cho == 1:
                for item in listExperience:
                    print(repr(item))
            elif cho == 2:
                for item in listFresher:
                    print(repr(item))
            elif cho == 3:
                for item in listIntern:
                    print(repr(item))
            elif cho == 4:
                ck = False
            else :
                raise Exception("Invalid")


if __name__ == "__main__":
    print("List operation with list employee : ")
    print("1. Insert information of the employee .")
    print("2. Show information .")
    print("3. Edit the information .")
    print("4. Count amount of each type employee .")
    print("5. Exit ")
    check = True
    me = Management()
    while (check):
        choi = int(input("Enter the your operation : "))
        if choi == 1:
            me.insert()
        elif choi == 2:
            me.showinformation()
        elif choi == 3:
            me.edit()
        elif choi == 4:
            print("Number of experience employee : ", len(listExperience))
            print("Number of Fresher : ", len(listFresher))
            print("Number of Intern : ", len(listIntern))
        elif choi == 5:
            check = False
        else:
            raise Exception("Invalid")
    print("============================================================================================================")
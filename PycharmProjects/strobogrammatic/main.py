# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import math
def checkPrimenumber(number):
    t = int(math.sqrt(number))
    for i in range(2,t) :
        if number%i == 0 :
            return False
        return True

def checkStrobogrammatic(number) :
    map = (("0","0"),("1","1"),("6","9"),("8","8"),("9","6"))
    i = 0
    a = str(number)
    j = len(a)-1
    while i <= j :
        if (a[i],a[j]) not in map :
            return False
        i += 1
        j -= 1
    return True

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    list = []
    dem = 0
    for x in range(1,10000000) :
        if checkPrimenumber(x) == True and checkStrobogrammatic(x) == True :
            dem = dem + 1
            list.append(x)

    print(list)
    print(dem)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

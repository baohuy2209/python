import random
check = True
while check :
    index = random.randint(1,3)
    if index == 1 :
        computer = 'd'
    if index == 2 :
        computer = 'l'
    if index == 3 :
        computer = 'k'

    try :
        player = input("Input your choice ('d' is dam, 'k' is keo , 'l' is la ) : ")
        if player != 'd' and player != 'l' and player != 'k' :
            raise ValueError("Invalid")
        if computer == player:
            print("draw ! ")
        else:
            if computer == 'd':
                if player == 'k':
                    print("you lose . ")
                else:
                    print("You win . ")
            if computer == 'l':
                if player == 'k':
                    print("you win . ")
                else:
                    print("You lose . ")
            if computer == 'k':
                if player == 'l':
                    print("you lose . ")
                else:
                    print("You win . ")
    except ValueError as err :
        print("invalid")


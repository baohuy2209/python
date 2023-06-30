import random
def guess(x) :
    random_number = random.randint(1,x)
    guess = 0
    while guess != random_number :
        guess = int(input(f'Guess a number between and {x} : '))
        if guess < random_number :
            print("Wrong , guess again , too low ")
        elif guess > random_number :
            print("Wrong , guess again , too high ")
    print("Exactly!")
guess(10)
import random
def computer_guess(x) :
    low = 1
    high = x
    feedback = ''
    while feedback != 'c' and low < high:
        guess = random.randint(low,high)
        feedback = input(f'Is guess {guess} too high {H} , too low {L}, or correct {C}')
        if feedback == 'h' :
            high = guess - 1
        elif feedback == 'l' :
            low = guess + 1
    print("Exactly")
computer_guess(100)
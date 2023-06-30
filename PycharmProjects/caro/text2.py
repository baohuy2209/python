x = 1
board = [i for i in range(0,9)]
for i in board :
    end = ' | '
    if i%3 == 2 :
        end = ' \n'
        if i != 1 : end += '----------\n'
        char = ' '
        print(char,end = end)
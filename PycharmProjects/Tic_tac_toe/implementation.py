import random

boards = [i for i in range(0, 9)]
player, computer = "", ""
moves = ((1, 7, 3, 9), (5,), (2, 4, 6, 8))
winner = (
    (0, 1, 2),
    (3, 4, 5),
    (6, 7, 8),
    (1, 4, 7),
    (2, 5, 8),
    (0, 4, 8),
    (2, 4, 6),
)
tab = range(1, 10)


# print tic_tac_toe board
def print_board():
    x = 1
    for i in boards:
        end = "  |"
        if x % 3 == 0:
            end = "\n"
            if i != 1:
                end += "------------\n"
        char = " "
        if i in ("X", "O"):
            char = i
        x += 1
        print(char, end=end)


def select_char():
    chars = ("X", "O")
    if random.randint(0, 1) == 0:
        return chars[::-1]
    return chars


def can_move(brd, player, move):
    if (move in tab) and (brd[move - 1] == move - 1):
        return True
    return False


def can_win(brd, player, move):
    places = []
    x = 0
    for i in brd:
        if i == player:
            places.append(x)
        x += 1
    win = True
    for tup in winner:
        for x in tup:
            if brd[x] != player:
                win = False
                break
        if win is True:
            break
    return win


def make_move(brd, player, move, undo=False):
    if can_move(brd, player, move):
        brd[move - 1] = player
        win = can_win(brd, player, move)
        if undo:
            brd[move - 1] = move - 1
        return (True, win)
    return (False, False)


def computer_move():
    move = -1
    for i in range(1, 10):
        if make_move(boards, computer, i, True)[1]:
            move = i
            break
    if move == -1:
        for i in range(1, 10):
            if make_move(boards, player, i, True)[1]:
                move = 1
                break
    if move == -1:
        for tup in moves:
            for mv in tup:
                if (move == -1) and can_move(boards, computer, mv):
                    move = mv
                    break
    return make_move(boards, computer, move)


def space_exist():
    return boards.count("X") + boards.count("O") != 9


if __name__ == "__main__":
    player, computer = select_char()
    print("Player is [%s] and computer is [%s]" % (player, computer))
    result = "<<< Dual ! >>>"
    while space_exist():
        print_board()
        print("Make your move [1-9] : ", end="")
        move = int(input("Enter your move: "))
        move, won = make_move(boards, player, move)
        if not move:
            print(">> Invalid number ! Try again")
            continue
        if won:
            result = "*** Congratulations! You won ! ***"
            break
        elif computer_move()[1]:
            result = "You lose!"
            break
    print_board()
    print(result)

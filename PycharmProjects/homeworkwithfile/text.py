def checkint(n):
    check = False
    if n > 1:
        n = n/4
        checkint(n)
    if n == 1:
        check = True
    return check


print(checkint(16))

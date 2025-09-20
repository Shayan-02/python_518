def game(num):
    n1 = int(str(num)[0])
    n2 = int(str(num)[1])
    if n1 > n2: return n1 - n2
    elif n2 > n1 : return n2 - n1
    else: return 0


print(game(int(input())))

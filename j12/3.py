c = 50

for i in range(3):
    g = int(input("guess: "))
    if g == c:
        print("you win")
        break
    else:
        print("false number")
else:
    print("you loss")

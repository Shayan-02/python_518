from random import randint

start = int(input("enter start: "))
end = int(input("enter end: "))

c = randint(start, end)

for i in range(3):
    g = int(int(input("guess: ")))
    if g == c:
        print("win")
        break
    else:
        if g > c:
            print("lower")
        else:
            print("bigger")
else:
    print(f"game over corrct number was {c}")

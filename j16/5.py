from random import *

lst = ["ahmad", "ava", "reza", "mohammad"]

cn = choice(lst)

chances = len(cn)

invalid = []

print("you have", chances, "chances")

i = chances
while i > 0:
    g = input(f"enter {chances} char word (chance {i}): ")
    if len(g) == chances:
        if g == cn:
            print("you win")
            break
        else:
            if g not in invalid:
                print("wrong")
                i -= 1
            else:
                print("tekrari")
            invalid.append(g)
    else:
        print("invalid length")

from random import *

start = int(input("enter start: "))
end = int(input("enter end: "))

p = ["ali", "reza", "saeed", "sara", "ana", "amir"]

rn = randint(start, end)
rc = choice(p)

print(rn, rc)

from ast import List


lst = [1, 2, 3]
lst[1] = "ali"

t = (1, 2, 3)
# t[1] = "ali"

t2 = list(t)
t2[2] = "ana"
t = tuple(t2)


print(t)

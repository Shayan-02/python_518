x = 121

y = ""

for i in range(len(str(x)) - 1, -1, -1):
    y += str(str(x)[i])

print(str(x) == y)
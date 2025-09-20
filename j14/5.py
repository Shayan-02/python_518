def calculate_floor(x):
    f = 0
    for i in x:
        if i == "u" or i == "U":
            f += 1
        elif i == "d" or i == "D":
            f -= 1
    return f

floor = input()
print(calculate_floor(floor))

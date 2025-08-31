l = 0 # tedad
s = 0 # majmoo
while True:
    a = float(input("enter your score: "))
    if a <= 0:
        break
    else:
        s += a
        l += 1


avg = s / l

print(avg)

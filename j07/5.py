import time
i = 1
j = 11
while i <= 20:
    if i == 7 or j == 13:
        i += 2
        j += 3
        continue
    print(i, j)
    time.sleep(1)
    i += 1
    j += 1

row1, row2 = input().split(), input().split()

count = 0

for i in range(8):
    if row1[i] == row2[i] == "1":
        count += 1

print(count)
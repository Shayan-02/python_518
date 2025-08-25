start = int(input("start: "))
end = int(input("end: "))
n = int(input("mazrab: "))
j = 1
while start <= end:
    if start % n == 0:
        print(j, start, sep=" : ")
        j += 1
    start += 1
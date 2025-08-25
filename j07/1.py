i = 4
majmoo = 0
while i:
    a = float(input("enter your score: "))
    majmoo += a
    i -= 1

avg = majmoo / 4

if avg >= 18:
    print(avg, ": A")
elif avg >= 16:
    print(avg, ": B")
elif avg >= 14:
    print(avg, ": c")
elif avg >= 10:
    print(avg, ": D")
elif avg < 10:
    print(avg, ": Failed")

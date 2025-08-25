a = int(input("enter a number: "))

if a % 15 == 0:
    print("fizz bazz")
elif a % 5 == 0:
    print("bazz")
elif a % 3 == 0:
    print("fizz")
else:
    print(a)
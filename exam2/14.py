valid = [10 ** x for x in range(1, 101)]

num1 = int(input())
op = input()
num2 = int(input())

if num1 in valid and num2 in valid:
    if op == "+":
        print(num1 + num2)
    elif op == "*":
        print(num1 * num2)

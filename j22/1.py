n1 = "10"
n2 = 20
op = "/"

try:
    if op == "+":
        print(n1 + n2)
    if op == "-":
        print(n1 - n2)
    if op == "*":
        print(n1 * n2)
    if op == "/":
            print(n1 / n2)
except ZeroDivisionError:
    print("can't devide by zero")
except TypeError:
    print("num1 and num2 must be number")
print("continue")

num1 = float(input("enter number1: "))
num2 = float(input("enter number2: "))
num3 = float(input("enter number3: "))
num4 = float(input("enter number4: "))

if 0 <= num1 <= 20:
    if 0 <= num2 <= 20:
        if 0 <= num3 <= 20:
            if 0 <= num4 <= 20:
                avg = (num1 + num2 + num3 + num4) / 4
                if avg >= 18:
                    print(avg, "-> A")
                elif avg >= 16:
                    print(avg, "-> B")
                elif avg >= 14:
                    print(avg, "-> C")
                elif avg >= 10:
                    print(avg, "-> D")
                else:
                    print(avg, "-> Failed")
            else:
                print("invalid num4")
        else:
            print("invalid num3")
    else:
        print("invalid num2")
else:
    print("invalid num1")
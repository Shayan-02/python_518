# way1
nationalcode = input()
controldigit = int(nationalcode[-1])

sumdigits = 0
for i in range(10, 1, -1):
    sumdigits += i * int(nationalcode[10 - i])

mod11 = sumdigits % 11
if controldigit < 2:
    print("valid Personal ID" if controldigit == mod11 else "invalid Personal ID")
else:
    print("valid Personal ID" if controldigit ==  11 - mod11 else "invalid Personal ID")

# way2

nationalcode = input()
if not nationalcode.isdigit() or len(nationalcode) != 10:
    print("invalid Personal ID")
else:
    controldigit = int(nationalcode[-1])
    sumdigits = 0
    for i in range(9):
        sumdigits += int(nationalcode[i]) * (10 - i)

    mod11 = sumdigits % 11

    is_valid = False
    if mod11 < 2:
        if controldigit == mod11: is_valid = True
    else:
        if controldigit == 11 - mod11: is_valid = True

    if is_valid: print("valid Personal ID")
    else: print("invalid Personal ID")

num = int(input())
for _ in range(num):
    t = input()
    if t[0:2] == "09" and len(t) == 11 and t.isdigit():
        print("+" + "98" + t[1:])
    elif t[0:3] == "+98" and len(t) == 13 and t[1:].isdigit():
        print(t)
    elif t[0:2] == "98" and len(t) == 12 and t.isdigit():
        print("+" + t)
    else:
        print("invalid")

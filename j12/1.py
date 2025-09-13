a = list(map(int, input().split()))
if len(a) == 3:
    for _ in a:
    # if b[0] > 0 and b[1] > 0 and b[2] > 0:
        if _ <= 0:
            print("No")
            break
        elif sum(a) != 180:
            print("No")
            break
    else:
        if sum(a) == 180:
            print("Yes")
else:
    print("No")

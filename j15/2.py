def avgNumber(*a):
    s = 0
    l = 0
    for i in a:
        s += i
        l += 1
    return s / l


running = 1


# while running:
#     number = int(input())
#     if number == 0:
#         running = 0


print(avgNumber(lst))

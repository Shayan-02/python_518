def separator(ls):
    even, odd = [], []
    for _ in ls:
        if _ % 2 == 0: even.append(_)
        else: odd.append(_)
    return even, odd


a = input().split()
# b = list(map(int, a))
b = [int(_) for _ in a]
print(separator(b))

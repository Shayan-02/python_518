def show_even(a, b):
    lst = []
    for i in range(a, b+1):
        if i % 2 == 0:
            lst.append(i)
    for _ in lst:
        print(_)


start = int(input("enter start: "))
end = int(input("enter end: "))

show_even(start, end)

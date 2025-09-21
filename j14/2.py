def bigger(lst, value):
    valid = []
    for _ in lst:
        if _ > value:
            valid.append(_)
    return valid


print(bigger([1, 2, 3, 4, 5], int(input())))

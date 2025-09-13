start = int(input("enter start: "))
end = int(input("enter end: "))
# lst = []

# for i in range (start, end+1):
#     if i % 2 == 0 and i % 8 != 0:
#         lst.append(i)

# print(lst)


lst = [i**2 for i in range(start, end+1) if i % 2 == 0]
print(lst)

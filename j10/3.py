# lst = []
# lst.append(1)
# lst.append(2)
# lst.append("ali")
# lst.insert(1, "reza")

a = input()
lst = []
b = ["a", "e", "i", "u", "o"]
for i in a:
    if i not in b:
        lst.append(i)

print(lst)

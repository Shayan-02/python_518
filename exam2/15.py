num = int(input())

text = input().split()

for i in range(num, 0, -1):
    print(text[i - 1], end=" ")

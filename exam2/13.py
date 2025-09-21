num = int(input())
print("YES" if num == int(str(num)[::-1]) else "NO")

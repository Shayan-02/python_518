num = int(input())

sum_numbers = 0
for i in range(1, num//2 + 1):
    if num % i == 0: sum_numbers += i

print("YES" if num == sum_numbers else "NO")

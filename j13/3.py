# a = int(input())

# if a % 2 == 0:
#     print("even")
# else:
#     print("odd")

def isEven(num):
    return "even" if num % 2 == 0 else "odd"

print(isEven(2))
print(isEven(3))
print(isEven(5))
print(isEven(70))
print(isEven(59))
print(isEven(80))

# def fibonacci(n):
#     a = 0
#     b = 1
#     if n < 0:
#         print("Incorrect input")
#     elif n == 0:
#         return a
#     elif n == 1:
#         return b
#     else:
#         for i in range(2, n + 1):
#             c = a + b
#             a = b
#             b = c
#         return b


# print(fibonacci(9))

# def fibonacci(x):
#     if x == 1 or x == 2:
#         return 1
#     else:
#         return fibonacci(x-1) + fibonacci(x-2)

# print(fibonacci(5))

def fact(num):
    f = 1
    for i in range(1, num+1):
        f *= i
    
    return f

print(fact(5))

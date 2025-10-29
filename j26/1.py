import time

def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} ran in {end_time - start_time:.2f} seconds")
        return result
    return wrapper

@timer
def slow_function():
    sumNumbers = 0
    i = 1
    while i <= 1_000_000_000:
        sumNumbers += i
        i += 1
    return sumNumbers

print(slow_function())
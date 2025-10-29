def limit_calls(max_calls):
    def decorator(func):
        calls = 0
        def wrapper(*args, **kwargs):
            nonlocal calls
            if calls >= max_calls:
                raise ValueError(f"Function {func.__name__} has been called more than {max_calls} times")
            calls += 1
            return func(*args, **kwargs)
        return wrapper
    return decorator

@limit_calls(3)
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")  # Hello, Alice!
greet("Bob")    # Hello, Bob!
greet("Charlie")  # Hello, Charlie!
greet("David")  # Raises ValueError
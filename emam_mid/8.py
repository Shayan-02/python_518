def find_next_power(n: int) -> int:
    """
    Finds the smallest power of 2 that is greater than or equal to a number n.

    Args:
        n (int): A non-negative integer.

    Returns:
        int: The smallest power of 2 that is >= n.
    """
    if n <= 0:
        return 1

    # Use a loop to find the smallest power of 2.
    # While a list comprehension could be used, a simple loop is more direct
    # and efficient for this specific problem as we only need a single value.
    power_of_2 = 1
    while power_of_2 <= n:
        power_of_2 *= 2
    return power_of_2


# calling function
print(find_next_power(int(input())))

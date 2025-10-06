def is_right_triangle(a: int, b: int, c: int) -> str:
    """
    Checks if three given positive integers can form the sides of a right-angled triangle.

    This function takes three positive integers representing the lengths of the sides
    of a potential triangle. It determines if these lengths satisfy the Pythagorean theorem
    (a^2 + b^2 = c^2), which is characteristic of a right-angled triangle.

    Args:
        a (int): The length of the first side (1 <= a <= 150).
        b (int): The length of the second side (1 <= b <= 150).
        c (int): The length of the third side (1 <= c <= 150).

    Returns:
        str: "YES" if a right-angled triangle can be formed, "NO" otherwise.
    """
    sides = sorted([a, b, c])

    # Check if the square of the two shorter sides sums up to the square of the longest side
    if sides[0] ** 2 + sides[1] ** 2 == sides[2] ** 2:
        return "YES"
    else:
        return "NO"


# calling function
print(is_right_triangle(int(input()), int(input()), int(input())))

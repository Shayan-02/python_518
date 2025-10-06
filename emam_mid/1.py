def check_registrations(n):
    """
    Checks if the number of class registrations exceeds the limit of 50.

    Args:
        n (int): The number of registrations in a class.

    Returns:
        str: "Yes" if n > 50, otherwise "No".
    """
    if n > 50:
        return "Yes"
    else:
        return "No"


# calling function
print(check_registrations(int(input())))

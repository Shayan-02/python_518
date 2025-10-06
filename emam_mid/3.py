def calculate_final_price(days: int, daily_price_changes: list) -> int:
    """
    Calculates the final price of a good after a series of daily changes.

    This function takes the number of days, the initial price, and subsequent
    daily price changes as input. It then calculates and prints the final price
    after applying all the daily changes. The final price is the sum of the initial
    price and all the daily changes.

    Args:
        days (int): The number of days.
        daily_price_changes (list): The daily price changes.

    Returns:
        int: The final price of the good.
    """
    final_price = 0
    for i in range(days):
        final_price += daily_price_changes[i]
    return final_price


# calling function
print(calculate_final_price(int(input()), [int(x) for x in input().split()]))


def classify_city_risk(p: int, q: int) -> str:
    """
    Classifies a city's COVID-19 risk level (White, Yellow, or Red) based on
    average new cases and hospitalizations per day per one million population.

    Args:
        p (int): Average number of new cases per day per one million population
                 over the past two weeks (0 <= p <= 1000).
        q (int): Average number of new hospitalizations per day per one million
                 population over the past two weeks (0 <= q <= 500).
                 Note: q is always less than or equal to p (q <= p).

    Returns:
        str: The color-code indicating the city's COVID-19 risk level.

    Classification Criteria:
    - White: p <= 50 and q <= 10 (low-risk zone)
    - Red: q > 30 (high-risk zone)
    - Yellow: All other cases (moderate-risk zone)
    """
    if p <= 50 and q <= 10:
        return "White"
    elif q > 30:
        return "Red"
    else:
        return "Yellow"


# calling function
print(classify_city_risk(int(input()), int(input())))

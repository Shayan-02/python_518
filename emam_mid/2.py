def calculate_free_courses(n):
    """
    Calculates the number of free courses a student can enroll in based on the number of referrals.

    Each referral provides a 10% discount, and 10 referrals result in a free course (100% discount).
    This function uses integer division to determine the number of free courses.

    Args:
        n (int): The total number of students referred.

    Returns:
        int: The number of courses the student can enroll in for free.
    """
    total_discount = 10 * n
    free_courses_count = total_discount // 100
    return free_courses_count


# calling function
print(calculate_free_courses(int(input())))

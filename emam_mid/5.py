def check_jinn_location(locations: str) -> str:
    """
    Checks if two jinns are in the same location based on a string of locations.

    Args:
        locations (str): A string containing two location names separated by a space.
                         Example: "salt marshes salt marshes" or "salt marshes Rig-e Jenn".

    Returns:
        str: "together" if the jinns are in the same place, "lost" otherwise.
    """
    loc_list = locations.split()
    if loc_list[0] == loc_list[1]:
        return "together"
    else:
        return "lost"


# calling function
print(check_jinn_location(input()))

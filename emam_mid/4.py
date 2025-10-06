def simulate_bird_ritual(
    n: int, s: int, initial_birds: list[str], actions: list[str]
) -> list[str]:
    """
    Simulates the bird permutation dance ritual based on a sequence of actions.

    Args:
        n (int): Initial number of birds (1 ≤ n ≤ 1000)
        s (int): Number of actions to perform (1 ≤ s ≤ 5000)
        initial_birds (list[str]): List of initial bird names in order from left to right
        actions (list[str]): List of action strings, each representing one operation

    Returns:
        list[str]: Final configuration of birds from left to right

    Operations supported:
        - "insert bird-name position": Insert bird at specified position (0-indexed from left)
        - "depart bird-name": Remove the specified bird from the row
        - "relocate bird-name displacement": Move bird by displacement positions
          (positive = right, negative = left, 0 = stay in place)
    """
    # Initialize the bird row with the initial configuration
    birds = initial_birds.copy()

    # Process each action in sequence
    for action in actions:
        parts = action.strip().split()
        operation = parts[0]

        if operation == "insert":
            bird_name = parts[1]
            position = int(parts[2])
            # Insert bird at the specified position
            birds.insert(position, bird_name)

        elif operation == "depart":
            bird_name = parts[1]
            # Remove the bird from the row
            birds.remove(bird_name)

        elif operation == "relocate":
            bird_name = parts[1]
            displacement = int(parts[2])

            # Find current position of the bird
            current_pos = birds.index(bird_name)

            # Remove bird from current position
            birds.pop(current_pos)

            # Calculate new position after displacement
            # Displacement is relative to the original position before removal
            new_pos = current_pos + displacement

            # Clamp new position to valid range [0, len(birds)]
            new_pos = max(0, min(len(birds), new_pos))

            # Insert bird at new position
            birds.insert(new_pos, bird_name)

    return birds


# Read input
n, s = map(int, input().split())
initial_birds = input().split()

actions = []
for _ in range(s):
    actions.append(input().strip())

# Simulate the ritual
final_configuration = simulate_bird_ritual(n, s, initial_birds, actions)

# Output the result
print(" ".join(final_configuration))

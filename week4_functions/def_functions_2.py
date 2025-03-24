def display_ladder(steps):
    """Displays an ASCII ladder with the given number of steps."""
    for _ in range(steps):
        print("|  |")
        print("|__|")
    print("\nLadder with", steps, "steps displayed.")


def create_ladder():
    """Asks the user for the number of steps and calls display_ladder."""
    try:
        steps = int(input("Enter the number of steps for the ladder: "))
        if steps > 0:
            display_ladder(steps)
        else:
            print("Please enter a positive integer.")
    except ValueError:
        print("Invalid input! Please enter an integer.")


# Call the create_ladder function to start the program
create_ladder()

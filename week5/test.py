def movements():
    steps = ["forward", 10, "back", 5, "right", 3, "left", 1]
    return steps


def menu():
    print("\nPlease select a direction by entering an index number:")
    directions = movements()

    # Display available movements
    for index in range(len(directions)):
        print(f"{index}: {directions[index]}")

    # Get user input safely
    while True:
        try:
            user_choice = int(input("Enter index: "))
            if 0 <= user_choice < len(directions):
                return directions[user_choice]  # Return the selected movement
            else:
                print("Invalid choice, please enter a valid index.")
        except ValueError:
            print("Invalid input, please enter a number.")


def run_task4():
    route = []
    print("\nEscape Route Selection:")

    for count in range(5):
        choice = menu()
        route.append(choice)

    print("\nYour escape route:", route)


run_task4()

def movements():
    steps = ["forward", 10, "back", 5, "right", 3, "left", 1]
    return steps

def menu():
    print("Please select a direction...")
    dir = movements()
    for index in range(len(dir)):
        print(f"Index {index}: {dir[index]}")
    users_choice = int(input("Enter index: "))
    return users_choice

def run_task4():
    route = []
    print("Escape route:")
    for count in range(5):
        route.append(menu())
    print("Your selected route:", route)


run_task4()


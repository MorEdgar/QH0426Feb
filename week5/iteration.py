def movements():
    path = ["forward", 10, "back", 5, "right", 3,  "left", 1]
    return path

def menu():
    print("direction....")
    dir = movements()
    for index in range(len(dir)):
        print(f"index is {index} and the value is {dir[index]}")

menu()
fruits = ["apple", "kiwi", "grapes"]
print(fruits[0])

code = "problem solving"
print(code[0:3])

def movements():
    path = ["forward", 10, "back", 5, "right", 3,  "left", 1]
    return path

def run_task2():
    print("moving....")
    dir = movements()
    print(f"direction:{dir[0]},steps {dir[1]}")
    print(f"direction:{dir[2]},steps {dir[3]}")
    print(f"direction:{dir[4]},steps {dir[5]}")

run_task2()

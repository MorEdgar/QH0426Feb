length = str(input("please enter the sequence?"))
marker = str(input("enter the character for the marker"))
first_x = -1
second_x = -1
distance = 0
for char in range(len(length)):
    if length[char] == "x":
        if first_x == -1:
            first_x = char
        else:
            second_x = char
            break
distance = second_x - first_x -1
print(f"The distance between the markers is {distance}")
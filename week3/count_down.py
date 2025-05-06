#steps count down
steps = int(input("how far are we from the target?"))
for steps_remaining in range(steps,0, -1):
    print(steps_remaining,"steps remaining")
cover_type = input("What is the cover type? ")
if cover_type == "soft":
    perfect_bound = input("Perfect bound?")
    if perfect_bound == "yes":
        print("Soft covers, perfect bound books are very popular!")
    elif perfect_bound == "no":
        print("Soft covers with coils or stitches are great for short books")
elif cover_type == "hard":
    print("Books with hard covers can be more expensive.")
else:
    print("Invalid cover type.")
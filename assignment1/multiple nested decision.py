user_asking = input("where should i look?")
if user_asking == "in the bedroom":
     bedroom = input("where in the bedroom should i look?")
     if bedroom == "under the bed":
         print("Found some shoes but no phone")
     else:
         print("Found some mess but no phone")
if user_asking == "in the bathroom":
    bathroom = input("Where in the bathroom should i look?")
    if bathroom == "in the bathtub":
        print("Found a rubber duck but no phone")
    else:
        print("Found bathroom stuff but no phone")
if user_asking == "in the living room":
    living_room = input("Where in the living room should i look?")
    if living_room == "on the table":
        print("Yes! I found my phone")
    else:
        print("Found some stuff but no phone")
else:
    print("I do not know where that is but i will keep looking.")
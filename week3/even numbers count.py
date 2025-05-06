#even number inc
bright = int(input("What level of brightness is required?"))
for brightness_level in range(2,bright+2, 2):
    if bright % 2 == 0:
        print("brightness level:", brightness_level)
    elif bright % 2 == 1:
        print("brightness level:", brightness_level)
print("Complete!")
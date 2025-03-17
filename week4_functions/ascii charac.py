print("pgm started")
print("pls enter ascii code")
ascii_code=int(input())
if ascii_code in range(32,127):
    print("the ascii chr is", chr(ascii_code))
else:
    print("pgm ended")
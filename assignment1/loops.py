#first question how many bars should be charged?
bars = int(input("how many bars should be charged?"))
#set charged bars to 0
charged_bars = 0
#loop runs until charged bars less than bars to charge
while charged_bars < bars:
    charged_bars += 1 #with each loop amount of bars increment
    print(f"Bars charged: {"\u2588" * charged_bars}")
print("battery fully charged")
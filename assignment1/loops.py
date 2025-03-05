#first question how many bars should be charged?
bars_to_charge = int(input("how many bars should be charged?"))
#set charged bars to 0
charged_bars = 0
#loop runs until charged bars less than bars to charge
while charged_bars < bars_to_charge:
    print("charging...")
    charged_bars += 1 #with each loop amount of bars increment
    print(f"Bars charged: {charged_bars}/{bars_to_charge}") # showing charged/to charge
print("battery fully charged")
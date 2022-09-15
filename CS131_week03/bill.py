# Dorje Pradhan
# Spetember 12, 2022
# Python 1, CS 133
# Write a program that prints what everyone has to pay
# including the tip at a restuarant 

party = 4
TIP = 0.15
total = 200
personalBill = round((TIP + 1) * total / party, 2)

print("The bill is $", total)
print("The tip is $", TIP * total)
print("Each person has to pay $", personalBill)


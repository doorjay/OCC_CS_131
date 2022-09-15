# Dorje Pradhan
# Spetember 12, 2022
# Python 1, CS 133
# Print the surface area of a house to paint
# Subtract the windows and doors from total SA

# House dimensions
houseW = 23
houseL = 45
houseH = 9.5

# Number of windows and dimensions 
numOfWindows = 12
windW = 3
windH = 3.5

# Number of doors and dimensions
numOfDoors = 4
doorW = 3
doorH = 7.5

# Surface area of house and how much to paint
aOfHouse =  2 * ((houseW * houseH) + (houseL * houseH))
aToPaint = aOfHouse - (numOfWindows * windW * windH) - (numOfDoors * doorW * doorH)

print("The surface area to be painted of a house is", aToPaint, "sqft.")
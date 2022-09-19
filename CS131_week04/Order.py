# Dorje Pradhan
# September 19, 2022
# Python 1, CS 131
# Determine if three inputs are increasing
# or decreasing in numerical value

one = int(input("Enter the first number: "))
two = int(input("Enter the second number: "))
three = int(input("Enter the third number: "))

if one < two < three :
   print("They are in increasing order.")
elif one > two > three :
   print("They are in decreasing order.")
else :
   print("They are neither in increasing order nor decreasing order.")


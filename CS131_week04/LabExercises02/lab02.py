# Dorje Pradhan
# September 21, 2022
# Python 1, CS 131
# Write a program that reads three number and prints "all the same"
# if they are all the same, "all different" if they are all different
# and "neither" otherwise

# input the three numbers
num01 = int(input("Enter the first integer: "))
num02 = int(input("Enter the second integer: "))
num03 = int(input("Enter the third integer: "))

if num01 == num02 == num03 :    # all the same
    print("They are all the same.")
elif num01 != num02 != num03  : # all different
    print("They are all different.") 
else :  # a pair of numbers are the same
    print("They are neither all the same nor all different")
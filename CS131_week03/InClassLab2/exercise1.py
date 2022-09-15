# Dorje Pradhan
# September 14, 2022
# Python 1, CS 131
# user inputs a phone number, output it formated 
# 4155551212 -> (415) 555-1212

# ask user for input
phoneNumber = input("The phone number is: ")

# Format the (123) 456-7890
phoneNumber = "(" + phoneNumber[0 : 3 ] + ") " + phoneNumber[3 : 6] + "-" + phoneNumber[6 : ]

# output the formatted phone number
print("The formatted number is:", phoneNumber)
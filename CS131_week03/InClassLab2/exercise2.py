# Dorje Pradhan
# September 14, 2022
# Python 1, CS 131
# Take in a string with an even length
# swap the middle characters and output

# Take in the input
string = input("Please enter a string with an even number of characters: ")
halfLength = len(string) // 2 # the mid point

# swap the middle two characters
string = string[0 : halfLength  - 1] + string[halfLength] +\
         string[halfLength - 1] + string[halfLength + 1:]

# output the new string
print("Look! I swapped the middle two characters:", string)
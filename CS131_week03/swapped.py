# Dorje Pradhan
# Spetember 12, 2022
# Python 1, CS 133
# Swap the first and last letters of a string

word = input("Enter a string: ")

firstLetter = word[0]
lastLetter = word[-1]

# last letter + (all letters starting at index 1 exluding the last index) + first letter
swapped = lastLetter + word[ 1 : -1 ] + firstLetter

print(swapped)
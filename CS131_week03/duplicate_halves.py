# Dorje Pradhan
# Spetember 12, 2022
# Python 1, CS 133
# double the first and last half of a string and print

string = input("Enter a string: ")
half = len(string) // 2

doubled = (string[0 : half] * 2) + ((string[ half : ]) * 2)
print(doubled)
# Dorje Pradhan
# October 10, 2022
# Python 1 CS131
# Read a string form the user, then print the number
# of lower case, upper case, digits, and special symbols

rawString = input("Enter a string: ")
chars = 0
digits = 0
symbols = 0

for char in rawString :
    if char.isalpha() : 
        chars += 1
    elif char.isdigit() : 
        digits += 1
    else :
        symbols +=1

print("Total counts of Chars =", chars)
print("Total counts of Digits =", digits)
print("Total counts of Symbols =", symbols)
# Dorje Pradhan 
# Python 1, CS 131
# November 9, 2022

# Write a function that takes a string argument and
# returns a dictionary containing the number of times 
# each letter occurs in the string.

def count_letter(string) :
    letterCountDict = {}

    for i in string :
        if i not in letterCountDict and i.isalpha():
            letterCountDict[i] = 1
        elif i.isalpha() :
            letterCountDict[i] += 1

    return letterCountDict

def main() :
    phrase = "mathematician"

    letterOccurnce = count_letter(phrase)

    print("The number of times each letter occurs in the string \"", phrase, "\"")
    for item in letterOccurnce.items() :
        print(item[0], item[1])


main()
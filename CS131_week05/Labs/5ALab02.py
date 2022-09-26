# Dorje Pradhan
# Python 1, CS 131
# September 26, 2022

# Write a program that counts the number 
# of vowels in a string using while loop.

string = input("Please enter a string: ")
vowelCount = 0
idx = 0
VOWELS = "aeiou"


while idx < len(string) :
    if (string[idx].lower() in VOWELS) :
        vowelCount += 1
    idx += 1

print("The string,",string, ", has", vowelCount, "vowels in it.")
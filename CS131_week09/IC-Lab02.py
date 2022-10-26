# Dorje Pradhan
# October 246 2022
# Python 1, CS 131

# Write a program that asks the user for a file name
# and prints the number of characters, words, and lines
# in that file.

def main() :
    inFile = open(input("Please enter the file name: "), "r") 

    words = 0
    chars = 0
    lines = 0

    for line in inFile :
        lines += 1
        chars += len(line)

        lineArray = line.split()
        words += len(lineArray)
    
    print("The file conatins", chars, "characters,", words, "words,", lines, "lines")

main()
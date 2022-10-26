# Dorje Pradhan
# October 24, 2022
# Python 1, CS 131

# Write a program that reads a file containing two columns
# of floating-point numbers. Prompt the user for the file 
# name. Print the average of each column in an output file.

def main() :
    inFile = open(input("Enter the input file name: "), "r")
    outFile = open("output.txt", "w")

    line = inFile.readline()
    numbers = line.split()

    count = 0
    total1 = 0
    total2 = 0

    while line != "" :
        total1 += float(numbers[0])
        total2 += float(numbers[1])

        count += 1

        line = inFile.readline()
        numbers = line.split()

    inFile.close()
    total1 /= count
    total2 /= count

    outFile.write("Number of entries: %d \
                \nTotal column 1: %8.2f \
                \nTotal column 2: %8.2f\n" % (count * 2, total1, total2))
    outFile.close()

main()
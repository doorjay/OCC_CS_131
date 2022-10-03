# Dorje Pradhan
# Python 1, CS 131
# September 26, 2022

# Write a program that reads a number n from the user. The program will
# print out the first n triangular numbers.

value = int(input("Enter a positive integer: "))
sum = 0

for i in range(1, value + 1) :
    sum += i 
    print(i, "  ", sum)


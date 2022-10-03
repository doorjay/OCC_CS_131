# Dorje Pradhan
# Python 1, CS 131
# September 26, 2022

# Write a program that asks the user to enter 
# a positive integer n and print the multiplication
# table for the first n numbers.

value = int(input("Enter a positive integer: "))

print("  |", end = " ")
for i in range(1, value + 1) : 
    print(" ", i, end = " ")
print()
print("-----" * value)

for i in range(1, value + 1) :
    print(i, "|", end = " ")
    for j in range(1, value + 1) :
        product = i * j
        print("%3.0d" %product, end = " ")
    print("\n")
# Dorje Pradhan
# Python 1, CS 131
# September 26, 2022

# Write a while loop that prints all positive numbers
# that are divisble by 10 or 5 and less than a given 
# number n.

n = int(input("Enter an integer: "))
count = 0

while count < n :
    if count % 5 == 0 : # all nums divisble by 5 are divisble by 10
        print(count)
    count += 1
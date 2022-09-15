# Dorje Pradhan
# September 14, 2022
# Python 1, CS 131
# Write a program that helps a person decide
# whether or not to buy a hybrid car. 
# Inputs : 
    # cost of car, miles driven per year
    # gas price per gallon, efficiency in mpg
    # Resale value after 5 years
# Assume you will own the car for 5 years

# number of years owned
YEARS = 5

# User inputs information
carCost = int(input("Enter the cost of the car: "))
milesPerYear = int(input("How many miles will you drive each year? "))
gasPrice = int(input("Enter the price of gas per gallon: "))
mpg = int(input("Enter the fuel efficiency in mpg: "))
sellPrice = int(input("How much can you sell the car for after 5 years? "))

# Calculate the price after 5 years
fiveYearCost = carCost + YEARS * milesPerYear * gasPrice / mpg - sellPrice

# output the total cost
print("The total cost of ownership is %.2f" % fiveYearCost)
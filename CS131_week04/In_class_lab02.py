# Dorje Pradhan
# September 19, 2022
# Python 1, CS 131
# Write a program that calculates the shipping cost as shown in slide

# base cost is $10
shipping_price = 10

international = input("Are you shipping internationally (yes or no)? ")

if international.lower() == 'yes' :
    continental = input("Are you shipping continental (yes or no)? ")
    
    if continental.lower() == 'yes' :
        shipping_price = 5  # local cost

# output shipping rate, $ 2 decimals
print("The shipping rate is $%.2f" %shipping_price)
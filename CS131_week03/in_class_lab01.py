# Dorje Pradhan
# September 12, 2022
# Python 1, CS131
# You have an absurd amount of pennies and
# you want to tick off the chashier. Write a
# Program that divies up the proper changeS

# initial varaibles
my_money = 693    # money in pennies
owe = 411         # cost of item

change = my_money - owe

# how many dollars
dollars = change // 100
change = change % 100

# how many quartes
quarters = change // 25
change = change % 25

# how many dimes
dimes = change // 10
change = change % 10

# how many nickles
nickels = change // 5
change = change % 5

# output the change, dollars, quarters, dimes, nickles,
print ("The change is: \n", dollars, "dollars\n", quarters, "quarters\n", 
                            dimes, "dimes\n", nickels, "nickels\n", 
                            change, "pennies")
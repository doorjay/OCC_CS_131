# Dorje Pradhan
# September 26, 2022
# Python 1, CS 131
# Write an application to pre-sell a limited
# number of cinema tickets. Each buyer can buy 
# as many as 10 tickets. No more than 40 tickets
# can be sold. Implement a program that prompts 
# the user for the desired number of tickets and 
# then displays the number of remaining tickets. 
# Repeat until all tickets have been sold, and then 
# display the total number of buyers.

total_tix = 40
MAX_BUY = 10
total_buyers = 0

while total_tix > 0 :
    print("There are currently", total_tix, "tickets remaining.")

    valid_input = False
    while not valid_input :
        tix = int(input("How many tickets would you like to purchase? "))

        if tix <= MAX_BUY and tix > 0 and tix <= total_tix :
            valid_input = True
            total_buyers += 1
            total_tix -= tix
        else :
            print("Sorry, you can't buy that many.")
print("The total number of buyers was", total_buyers)
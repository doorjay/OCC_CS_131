# Dorje Pradhan
# October 13, 2022
# Python 1, CS 131
# Write a program and define a function named fund_sum
# to calculate the sum of numbers from 0 to n, where n 
# is a number entered by the user. 

def main() :
    num = int(input("Enter an integer: "))
    result = find_sum(num)
    print("The result is", result)

## Computes the sum of each integer from 0 to num
# @param num to add up to
# @return the total sum
#
def find_sum(num) :
    sum = num
    for i in range(num) :
        sum += i

    return sum 

main()
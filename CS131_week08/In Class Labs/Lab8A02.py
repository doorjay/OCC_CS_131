# Dorje Pradhan
# October 17, 2022
# CS 131, Python 1

# Compute the  alternating sum of all elements in a list.
# for example : 1 2 3 4 5 
#   1 - 2 + 3 - 4 + 5 = 3

def main() :
    userIn = input("Enter a value or leave blank to exit: ")
    sum = 0
    count = 0

    while userIn != " " :
        if count % 2 == 0 :
            sum += float(userIn)
        else :
            sum -= float(userIn)

        userIn = input("Enter a value of leave blank to exit: ")
        count += 1

    print("The alternating sum is %.1f" %sum)

main()
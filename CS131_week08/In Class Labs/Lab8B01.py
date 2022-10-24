# Dorje Pradhan
# October 19, 2022
# Python 1, CS 131

# Write a function def sameElements(a, b) that checks 
# whether two lists have the same elements in some order, 
# with the same multiplicities

def main() :
    list01 = [1, 3, 1, 1, 2]
    list02 = [1, 1, 1, 2, 1]

    print("List 1 is", list01)
    print("List 2 is", list02)
    print("The lists contain the same elements:", sameElements(list01, list02))

def sameElements(list01, list02) :
    list02.sort()
    list01.sort()
    return list02 == list01

main()
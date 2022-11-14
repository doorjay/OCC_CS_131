# Dorje Pradhan 
# Python 1, CS 131
# November 7, 2022

# Using lists, implements a function named lists_intersections
# that performs the intersection operator on two lists and 
# returns a new list with common elements

def lists_intersections(list1, list2):
    newList = []

    for i in list1 :
        if i not in newList and i in list2 :
            newList.append(i)

    return newList

def main():
    listA = ["red", "white", "red"]
    listB = ["green", "white", "yellow"]

    print("List A is", listA)
    print("List B is", listB)

    newList = lists_intersections(listA, listB)
    print("The intersection of two lists is", newList)

main()
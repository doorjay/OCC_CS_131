# Dorje Pradhan 
# Python 1, CS 131
# November 7, 2022
# create the union method using lists,
# remove duplicate values

def lists_union(list1, list2):
    newList = []

    for i in list1 + list2:
        if i not in newList :
            newList.append(i)

    return newList

def main():
    listA = [1, 5, 6, 8, 5]
    listB = [3, 4, 1, 5, 7]

    print("List A is", listA)
    print("List B is", listB)

    newList = lists_union(listA, listB)

    print("The union of the two lists is", newList)

    print()
    print("* " * 30)
    print()

    list1 = ["red", "white", "red"]
    list2 = ["green", "white", "yellow"]

    print("List 1 is", list1)
    print("List 2 is", list2)

    stringList = lists_union(list1, list2)
    print("The union of the two lists is", stringList)

main()
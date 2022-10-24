# Dorje Pradhan
# October 17, 2022
# CS 131, Python 1

# create a list with values [1, 2, 3, 4, 5, 6]
#   reverse the list and print it
# create a list [4, 6, 8, 6, 12]
#   remove all occurences of 6
# create a list [5, 10, 15, 200, 25, 50, 20]
#   search for the value 20 and replace it with 200
# Given 2 lists of strings:
#   list1 = ["M", "na", "i", "Ke"] 
#   list2 = ["y", "me", "s", "lly"]
#   Concatenate the two lists index-wise, so it becomes  
#   ['My', 'name', 'is', 'Kelly']

def reverse(list) :
    list[ :: -1]
    print(list)

def removeSix(list) :
    for i in list :
        if i == 6 :
            list.remove(i)

def replaceTwenty(list) :
    if 20 in list :
        list[list.index(20)] = 200

def mergeStr(list01, list02) :
    length = len(list01)
    temp = list01
    for i in range(length) :
        temp[i] = list01[i] + list02[i]

    return temp

def main() :
    list01 = [1, 2, 3, 4, 5, 6]
    reverse(list01)

    list02 = [4, 6, 8, 6, 12]
    removeSix(list02)
    print(list02)

    list03 = [5, 10, 15, 200, 25, 50, 20]
    replaceTwenty(list03)
    print(list03)

    strList01 = ["M", "na", "i", "Ke"]
    strList02 = ["y", "me", "s", "lly"]
    mergedStrList = mergeStr(strList01, strList02)
    print(mergedStrList)

main()
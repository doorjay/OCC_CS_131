# Dorje Pradhan
# October 19, 2022
# Python 1, CS 131

# magic square
# if all values in every row, column, and diagonals
# add up to the same number, its a magic square

def main() :
    row01 = [16, 3, 2, 13]
    row02 = [5, 10, 11, 8]
    row03 = [9, 6, 7, 12]
    row04 = [4, 15, 14, 1]

    square = [row01, row02, row03, row04]

    printSquare(square)

    if checkMagic(square) :
        print("It is a magic square.")
    else :
        print("It is not a magic square.")

# prints the 2D list
def printSquare(square) :
    for row in square :
        for num in row :
            print(num, end = " ")
        print()

# returns true if magic square, false otherwise
def checkMagic(square) :
    length = len(square[0])
    sum = 0
    for num in square[0] :
        sum += num

    lToR = square[length - 1][length - 1]
    rToL = square[0][0]
    rowSum = 0
    # check each row and add diagonals
    for idx in range(1, 4) :
        # diagonals
        lToR += square[idx - 1][idx - 1]
        rToL += square[-idx][-idx]

        # rows
        for num in square[idx] :
            rowSum += num

        # if any row sum != sum, return false
        if rowSum != sum :
            return False
        else :
            rowSum = 0 # fresh row

    # check diagonals
    if (lToR == rToL == sum) :
        return True
    else :
        print(lToR, rToL)
        return False

main()
# Dorje Pradhan
# October 10, 2022
# Python 1, CS 131
# Choose number between 1 and 20,
# until number == 1
#   divide the number by 2 if even
#   multiply by 3 if odd
# output the number of times looped

num = int(input("The value of n is "))
count = 0

while num > 1 :
    if num % 2 == 0 :
        num = num // 2
    else :
        num = num * 3 + 1
    count += 1
    print(num)

print("Total stopping time is", count)
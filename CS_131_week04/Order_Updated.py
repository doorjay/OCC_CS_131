# Dorje Pradhan
# September 19, 2022
# Python 1, CS 131
# Add a strict or lenient addition to your program

# should the decision making be strict or lenient
mode = input("Do you want strict or lenient? ")

# get numbers
one = int(input("Enter the first number: "))
two = int(input("Enter the second number: "))
three = int(input("Enter the third number: "))

# determine strict or lenient 
if mode == "strict" :
   if one < two < three :
      print("They are in increasing order.")
   elif one > two > three :
      print("They are in decreasing order.")
   else :
      print("They are neither in increasing order nor decreasing order.")
else :
   if one < two or two < three :
      print("They are in increasing order.")
   elif one > two or two > three :
      print("They are in decreasing order.")
   else :
      print("They are in both increasing order and decreasing order.")
      
# Dorje Pradhan
# September 19, 2022
# Python 1, CS 131
# Check several properties of a string.


string = input("Enter a string: ")

if string.isalpha() :
   print("The string contains only letters.")
if string.isupper() :
   print("All letters in the string are uppercase letters.")
if string.islower() :
   print("All letters in the string are lowercase letters.")
if string.isdigit() :
   print("The string contains only digits.")
if string[0].isupper() :
   print("The string starts with an uppercase letter.")
if string.endswith('.') :
   print("The string ends with a period.")
   


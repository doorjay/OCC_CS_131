# Dorje Pradhan
# October 18, 2022
# Python 1, CS 131

# Write a function that determines whether or not a string is a palindrome

def main() :
   str = input("Enter a string: ")
   isPalindrome(str)

def isPalindrome(str) :
   isPali = False
   length = len(str)
   
   for i in range(length) :
      endIdx = length - 1 -i
      if str[i] != str[endIdx] :
         print("That isn't a palindrome.")
         return
   print("That's a palindrome.")

main()
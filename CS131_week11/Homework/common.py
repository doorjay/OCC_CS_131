
# Dorje Pradhan
# November 14, 2022
# Python 1, CS 131

string1 = set(input("Enter the first string: ").lower().split())
string2 = set(input("Enter the second string: ").lower().split())

# need shared words, and words in str1 but not in str2 (and visa versa)
same_set = string1.intersection(string2) 
str1_diff = string1.difference(string2)
str2_diff = string2.difference(string1)


# print out shared words
print("The words that are in both strings: ")
for word in sorted(same_set) :
   print(word, end = " ")

# print different words
print("\nThe words in string 1 that are not in string 2: ")
for word in sorted(str1_diff) :
   print(word, end = " ")

print("\nThe words in string 2 that are not in string 1: ")
for word in sorted(str2_diff) :
   print(word, end = " ")


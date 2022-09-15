# Dorje Pradhan
# September 12, 2022
# Python 1, CS 131
# Print string length, 'a' with 'A' 
# Capitalize all, second char, last char, mid char

# get a word
word = input("Please enter a word: ")

# output 
print(len(word))                # length
print(word.replace('a', 'A'))   # capitalize 'a'
print(word.upper())             # ALL CAPS
print(word[1])                  # second letter
print(word[-1])                 # last letter

half = len(word) // 2           # middle index
print(word[half])               # middle letter
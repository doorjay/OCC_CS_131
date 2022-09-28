# Dorje Pradhan
# September 26, 2022
# Python 1, CS 131
# Write a program that reads a word and prints the word in reverse.
# MAKE SURE TO USE A LOOP THIS IS THE LOOP SECTION

word = input("Enter a word: ")
wordLen = len(word)
reverseWord = ""

idx = 0
while idx < wordLen :
    # add the letters to the front!
    reverseWord = word[idx] + reverseWord
    idx += 1    # increment

print(word, "reversed is", reverseWord)
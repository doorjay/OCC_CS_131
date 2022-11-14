# Dorje Pradhan 
# Python 1, CS 131
# November 9, 2022

# Write a function names is_unique that takes a string
# as  parameter and returns true if the string has unique 
# characters, if there are duplicates, returns false

def is_unique(string):
    return len(set(string)) == len(string)

# Write a function named is_pangram that takes a string as 
# a parameter and determines whether the string is a pangram.
# A pangram is a sentence containing every letter in the 
# English Alphabet.

def is_pangram(string) :
    alphabet = set("abcdefghijklmnopqrstuvwxyz")
    common = alphabet.intersection(string.lower())

    return len(common) == len(alphabet)

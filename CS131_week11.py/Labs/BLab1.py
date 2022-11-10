# Dorje Pradhan 
# Python 1, CS 131
# November 9, 2022

# write a function names is_unique that takes a string
# as  parameter and returns true if the string has unique 
# characters, if there are duplicates, returns false

def is_unique(string):
    for idx in range(0, len(string)) :
        if string[idx] in string[ idx + 1 : ] :
            return False

    # If cannot find any duplicates, return true!
    return True


def main():
    sentence = "abcdefghijk"
    hello = "Hello, World!"

    if is_unique(sentence) :
        print("Unique!")
    else :
        print("Not unique")

    if is_unique(hello) :
        print("Unique!")
    else :
        print("Not unique")

main()
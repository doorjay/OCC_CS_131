# Dorje Pradhan 
# Python 1, CS 131
# November 9, 2022
# Test the functions created in Functions.py!
import Functions 

def main() :
    sentence = "qwerty"
    hello = "goodBye world"

    # test is_unique 
    print(sentence, "is", end = " ")
    if Functions.is_unique(sentence) :
        print("unique!")
    else :
        print("not unique.")

    print(hello, "is", end = " ")
    if Functions.is_unique(hello) :
        print("unique!")
    else :
        print("not unique.")

    # space between
    print("* " * 20)

    # testing is_pangram
    allKeys = "qwertyuiopasdfghjklzxcvbnm"
    fox = "Oh no!"

    print(allKeys, "is", end = " ")
    if Functions.is_pangram(allKeys) :
        print("a panagram!")
    else :
        print("not a pangram.")

    print(fox, "is", end = " ")
    if Functions.is_pangram(fox) :
        print("a panagram!")
    else :
        print("not a pangram.")

main()
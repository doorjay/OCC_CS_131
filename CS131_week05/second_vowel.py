# Dorje Pradhan
# September 26, 2022
# Python 1, CS 131
# Print every second letter in a given string
# Print string with vowel replaced with _


line = input("Enter a string: ")
counter = 0
stringlen = len(line)
secondLetters = ""
noVowels = ""
VOWELS = "aeiou"

while counter < stringlen :

   if (counter % 2 == 0 and line[counter].isalpha()) :
      secondLetters += line[counter]
         
   if (line[counter].lower() in VOWELS) :
      noVowels += "_"
   else :
      noVowels += line[counter]
      
   counter += 1

print("The string with every second letter printed is:", secondLetters)
print("The string with every vowel replaced with  -  is: ", noVowels)

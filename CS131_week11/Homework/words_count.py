# Dorje Pradhan
# November 14, 2022
# Python 1, CS 131

word_array = str.lower().split()
word_bank = {}

for word in word_array :
   if word in word_bank :
      word_bank[word] += 1
   else :
      word_bank[word] = 1
      

for key in sorted(word_bank) :
   print(key + ":", word_bank[key])

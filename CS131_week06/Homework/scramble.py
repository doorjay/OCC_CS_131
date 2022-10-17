def main() :
   phrase = input("Enter a string (blank to quit): ")
   wordsArr = phrase.split()
   phrase = scramble(wordsArr)
   
   print ("THe scrambled version:", phrase)


def scramble(arr) :
   str = ""
   
   for word in arr :
      length = len(word)
      if length > 3 :
         for idx in range(1, length - 1) :
            temp = word[idx]
            word[idx] = word[idx + 1]
            word[idx + 1] = temp
            
      str += word + " "
      
   return str
               
         
main()
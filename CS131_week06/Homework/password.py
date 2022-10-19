# Dorje Pradhan
# October 18, 2022
# Python 1, CS 131

# Write a function that checks for a valid password

def main() :
   done = False
   while not done :
      
      password = input("Enter your password: ")
      done = isValidPassword(password)
      
   print("That pair of passwords will work.")
   
def isValidPassword(password) :
   repass = input("Re-enter your password: ")
      
   if password != repass :
      print("That passwords don't match")
      return False
      
   length = len(password)
      
   if length < 8 :
      print("That password didn't have the required properties.")
      return False
      
   upper = False
   lower = False
   hasDigit = False
   hasSpecial = False
   specialChars = "#@&"
   
   for i in range(length) :
      
      if not upper and password[i].isupper() :
         upper = True
      elif not lower and password[i].islower() :
         lower = True
         
      if not hasDigit and password[i].isdigit() :
         hasDigit = True
        
      if not hasSpecial and password[i] in specialChars :
         hasSpecial = True
         
      if upper and lower and hasDigit and hasSpecial :
         return True
         
   print("That password didn't have the required properties.")
   return False
            

main()
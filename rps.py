# First comes... ROCK!

from operator import truediv
import random


rps = ["r", "p", "s"]
notDone = True

print("Welcome to Rock Paper Scissors!")

while notDone:

  # user input
  invalid = True
  while invalid:
    print("Please choose Rock (r), Paper(p), or Scissors(s)") 
    choice = input()
    print("You chose",choice)

    if choice != "r" or choice != "p" or choice != "s": # invalid choice
      print("OOPS! Not a valid choice try again!")
    else:
      invalid = False 
  # end of while

bot = random.choice(rps)

if ( bot == 'r' and choice == 'r') or (bot == 's' and choice == 's') or (bot == 'p' and choice == 'p'):
  print("It's a tie! Both competitors chose", choice, "!")
elif (bot == 'r' and choice == 's') or (bot == 'p' and choice == 'r') or (bot == 's' and choice == 'p'):
  print("Oh no! You lost :(\nYou chose", choice, " and your opponent chose", bot)
else:
  print("You won! Congradulations! You chose", choice, "and your opponent chose", bot)

print("Would you like to play again? Yes(y) or No(n)")
cont = input()

if cont == 'y' or cont == 'yes' or cont == 'Yes':
  print("Excellent! Good luck!\n\n\n")
else:
  notDone = False
  print("Alright! See you next time!")
# end of main loop
# First comes... ROCK!
# Dorje Pradhan and Davis Arita
# CS 131, Python 1 project
# ROCK PAPER SCISSORS!!!

# loop the main game play
#   loop asking the user for input
#     if not a valid choice, ask again
# 
#   bot (opponent) chooses r, p, or s
#   
#   if its a tie, print Tie!
#   else if its a loss, print loss :(
#   else its a win, print win!
#   
#   ask to play again, if not end gmae loop

from operator import truediv
import random

RPS = ["r", "p", "s"]
notDone = True

print("Welcome to Rock Paper Scissors!")

while notDone:

  # user input
  invalid = True
  while invalid :
    print("Please choose Rock (r), Paper(p), or Scissors(s)") 
    choice = input()
    print("\nYou chose",choice)

    if choice != "r" and choice != "p" and choice != "s": # invalid choice
      print("OOPS! Not a valid choice try again!")
    else:
      invalid = False 
  # end of while

  # bot chooses r, p or s at random
  bot = random.choice(RPS)

  # A tie!
  if ( bot == 'r' and choice == 'r') or (bot == 's' and choice == 's') or (bot == 'p' and choice == 'p'):
    print("It's a tie!\nBoth competitors chose", choice, "!")

  # You lose!
  elif (bot == 'r' and choice == 's') or (bot == 'p' and choice == 'r') or (bot == 's' and choice == 'p'):
    print("Oh no! You lost :(\nYou chose", choice, "and your opponent chose", bot)

  # You win!
  else:
    print("You won! Congradulations!\nYou chose", choice, "and your opponent chose", bot)

  print("\n\nWould you like to play again? Yes(y) or No(n)?")
  cont= input()

  if cont.lower() == 'y' or cont.lower() == 'yes':
    print("\nExcellent! Good luck!\n\n")
  else:
    notDone = False
    print("Alright! See you next time!")
# end of main loop
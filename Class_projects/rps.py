# First comes... ROCK!
# Dorje Pradhan and Davis Arita
# CS 131, Python 1 project
# ROCK PAPER SCISSORS!!!

# loop the main game play
#   ask player 1 to choose r, p, or s
# 
#   player 2 chooses r, p, or s
#		
#		print the choices
#   
#   if its a tie, print Tie!
#   else if its a loss, print loss :(
#   else its a win, print win!
#   
#   ask to play again, if not end game loop

notDone = True

print("Let's play Rock, Paper, Scissors.")
print()

while notDone:

	# Player 1 input
	player01 = input("Player 1, Enter your choice: ").lower()

	# check player 1 input
	if player01 != "r" and player01 != "p" and player01 != "s": # invalid choice
		print("[ERROR:", player01, "not a valid move.]")
	else :

		if player01 == "r" :
			player01 = "Rock"
		elif player01 == "p" :
			player01 = "Paper"
		else :
			player01 = "Scissors"

		# Player 2 input
		player02 = input("Player 2, Enter your choice: ").lower()

		# check player 2 input
		if player02 != "r" and player02 != "p" and player02 != "s": # invalid choice
			player02 = "[ERROR: " + player02 + " not a valid move.]"
			print(player01, "v.", player02)
		else :
			# turn chars into words
			if player02 == "r" :
				player02 = "Rock"
			elif player02 == "p" :
				player02 = "Paper"
			else :
				player02 = "Scissors"

			# show choices
			print(player01, "v.", player02)

			# A tie!
			if (player01 == player02) :
				print("It's a TIE")

			# You lose!
			elif (player02 == 'Rock' and player01 == 'Scissors') or (
				  player02 == 'Paper' and player01 == 'Rock') or  \
				  (player02 == 'Scissors' and player01 == 'Paper'):
				print("Player 2 wins")

			# You win!
			else:
				print("Player 1 wins")

	# play again? 
	cont = input("\nagain? ")
	if cont.lower() == 'n' or cont.lower() == 'no':
		notDone = False
		print("Nice game!")
	else :
	   print()
# end of main loop
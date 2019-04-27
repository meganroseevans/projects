# A GAME OF HIGHER OR LOWER IN PYTHON by MeganRoseEvans

# NOTE: The cards are generated randomly and so are effectively pulled from an infinite pack. The probability of cards being picked is NOT affected by previously taken cards. Very open to suggestions and critique.

import numpy as np
import time

# Create the deck and set all other lists/variables we might need later
deck = ["Ace",2,3,4,5,6,7,8,9,10,"Jack","Queen","King"]
a_an = ["an","a","a","a","a","a","a","an","a","a","a","a","a"]
streak = 0
yes = {"hell yeah","hellyeah!","yep","yes","y","sure","why not?","why not","go on then","yeah"}
higher = {"higher","high","h","up","u"}
lower = {"lower","low","l","down","d"}

# Ask the player's name
print(" ")
print("Enter your name:")
x = input()

# Say hello and ask where they are from
time.sleep(1)
print(" ")
print("Hello,",x)
print("Where are you from?")
location = input()

# Chat and ask if they want to play a game
time.sleep(1)
print(" ")
print("Wow, I've never been to",location,"before")
time.sleep(1)
print(" ")
print("Wanna play a game?")
response = input()

# Create a while loop so only the response "hell yeah!" is accepted
while response.lower() not in ["hell yeah!","hell yeah"]:
	time.sleep(1)
	print(" ")
	print('Sorry... I only understand the response "hell yeah!"')
	time.sleep(1)
	print(" ")
	print("Wanna play a game?")
	response = input()

# Generate a random card value to simulate picking a card from a deck
position1 = np.random.randint(0,13)

time.sleep(1)
print(" ")
msg1 = "Great, I've pulled a card from my deck. It is {0} {1}!".format(a_an[position1],deck[position1])
print(msg1)

# Main code begins here. Users are returned to this point after losing if they want to play again
again = "yes"
while again.lower() in yes: #loop broken if user chooses not to continue
	
	streak += 1 # Increase streak by 1 each round
	
	# Ask for user input of higher or lower
	print("Higher or Lower?")
	guess = input()

	# Loop allows only answers within the higher or lower set
	while guess.lower() not in higher|lower:
		time.sleep(1)
		print(" ")
		print("Sorry, please select from either Higher or Lower")
		guess = input()
		
	# Pick next card
	position2 = np.random.randint(0,13)
	time.sleep(1)
	print(" ")
	msg2 = "The next card is {0} {1}!".format(a_an[position2],deck[position2])
	print(msg2)
	
	# Determine if player is correct or not.
	if position2 == position1:
		print("Oops, looks like it's a draw. Let's try again.")
	elif position2 > position1 and guess.lower() in higher:
		print("You win!")
	elif position2 < position1 and guess.lower() in lower:
		print("You win!")
	else:
		print("Sorry, you lose!")
		print("Your streak was",streak)
		streak = 0	# reset streak after losing
		time.sleep(1)
		print(" ")
		print("Wanna play again?") # Ask if player wants to go again
		again = input()
		
		# If player's response is NOT in yes set, double check.
		if again not in yes:
			print ("Are you sure? Say yes if you would like to go again.")
			again = input()
			
		# If players wants to go again, remind them of last card.
		if again in yes:
			time.sleep(1)
			print(" ")
			msg3 = "The last card was {0} {1}!".format(a_an[position2],deck[position2])
			print(msg3)
			time.sleep(1) # Wait before asking Higher or Lower again
			print(" ")
	
	# Save card value for next round
	position1 = position2
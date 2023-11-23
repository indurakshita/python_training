# import random
# import math
# # Taking Inputs
# lower = int(input("Enter Lower bound:- "))

# # Taking Inputs
# upper = int(input("Enter Upper bound:- "))

# # generating random number between
# # the lower and upper
# x = random.randint(lower, upper)

# print("\n\tYou've only ",
# 	round(math.log(upper - lower + 1)),
# 	" chances to guess the integer!\n")

# # Initializing the number of guesses.
# count = 0

# # for calculation of minimum number of
# # guesses depends upon range
# while count < math.log(upper - lower + 1, 2):
# 	count += 1

# 	# taking guessing number as input
# 	guess = int(input("Guess a number:- "))

# 	# Condition testing
# 	if x == guess:
# 		print("Congratulations you did it in ",
# 			count, " try")
# 		# Once guessed, loop will break
# 		break
# 	elif x > guess:
# 		print("You guessed too small!")
# 	elif x < guess:
# 		print("You Guessed too high!")

# # If Guessing is more than required guesses,
# # shows this output.
# if count >= math.log(upper - lower + 1, 2):
# 	print("\nThe number is %d" % x)
# 	print("\tBetter Luck Next time!")

# -----------------------------------------------------------------
import sys
import os
import random


if sys.platform == "win32":
    clear = lambda : os.system("cls")
else:
    clear = lambda : os.system("clear")


class GuessGame:
	clear()
	min_attempt =0
	max_attempt = 3
    
	def __init__(self,lower,higher):
		self.lower = lower
		self.higer = higher
		
		self.correct_value = random.randint(self.lower,self.higer)

	def guess(self):
		print("Hello! Welcome to guess the number game.......")
		print(f"Your maximum attempts are {self.max_attempt}")
		
		while self.min_attempt <self.max_attempt:
			user_value = int(input("enter the guessing number:"))
			self.min_attempt+=1
			if  user_value == self.correct_value:
				print("Your guess is correct")
				print("woooo!!!! Win the game")
				break
			elif  user_value > self.correct_value:

				print("Your guess is high")
			elif user_value < self.correct_value :
				print("Your guess is low")

		if self.min_attempt >=self.max_attempt:
			
			print("Sorry, Your attempt is out")
			

guess = GuessGame(1,10)
guess.guess()



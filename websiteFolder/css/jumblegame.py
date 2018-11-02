# word Jumble
#
# The computer picks a random word and then "jumbles" it
#The player has to guess the original word


import random


#Create a sequence of words to choose from

WORDS = ("python","Jumble","Treek","easy", "difficult")


#pick one word randomly from the sequence

word = random.choice(WORDS)

# create a variable to use later to see if the guess is correct

correct = word

#create a jumble version of the world

jumble =""

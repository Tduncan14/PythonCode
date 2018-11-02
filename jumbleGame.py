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

while word:
     position = random.randrange(len(word))
     # creates a new version of jumble
     jumble += word[position]
     # creates a new version of word
     word = word[:position] + word[(position + 1):]


# start the game

print("""

  Welcome to Word Jumble

  Unscramble the letters to make a word

  """)

print(" The jumble is : " , jumble)


guess = input("\nYour guess: " )

while guess != correct and guess != "" :
  print("Sorry, that's not it.")
  guess = input("Your guess: ")


if guess == correct:
    print = input("Your guess is correct. Pet yourself on the back")

print("Thanks for playing")


input("\n\nPress \ the enter key to exit")

                  
    

     
     

#Guess my number
##
#The computer picks a random number between 1 and 100
#The player tries to guess it and the computer lets
#The player on guessing the numner is too high, too low
# or right on the money


import random

print("\tWelcome to 'Guess My Number'!")
print("\n I'm thinking of a number between 1 and 100.")
print("Try to guess it in as few attempts as possible. \n")

# set the intial values

the_number = random.randint(1,2)
guess = int(input("Take a guess: "))
tries = 1

# guessing loop

while guess != the_number :
    if guess > the_number :
      print("guess lower") 
    else:
      print("Higher...")

      guess = int(input("Take a guess: "))
      tries += 1
      

print("You guessed it! The number was", the_number)
print("And it only took you:" ,tries  ," tries")

input("press enter to exit the code")

      
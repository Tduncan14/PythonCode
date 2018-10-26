#Random acess
#Demonstration string indexing

# imports the random module
import random

word ="index"

print("The word is: ",word,"\n")

#shows the length of thew word
high=len(word)
low = -len(word)

for i in range(10):
 position =random.randrange(low, high)
 print("word[",position,"]\t",word[position])


input("\n\nPress the enter key to exit.")




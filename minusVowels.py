#no vowels
#Demonstrates creating new strings with a for loop

message = input("Enter a message")

new_message =""

Vowels = "aeiou"

print()
for letter in message:
     if letter.lower() not in Vowels:
       new_message += letter
       print("A new string has been created:", new_message)


print("\n your message without vowels is:", new_message)

input("\n\n press enter to close the game")

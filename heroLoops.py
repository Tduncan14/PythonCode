#create a tuple with some items

inventory =("sword","shield","armor","healing potion")

# print the tuple

print("\n The tuple inventory is: ")
print(inventory)

#print each element in the tuple

print("\nYour items:")
for item in inventory:
    print (item)

#get the length of a tuple

if "healing potion" in inventory :
 print("You will live to fight another day")


print("You have", len(inventory),"items in your possession.")
print("\n\nPress the enter key to exit.")
    

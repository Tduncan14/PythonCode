gi# Exclusive Network
 # Demonstrates logical operators and compound conditions

print("\t Exclusive Computer Network ")
print("\t\tMember only\n")

security = 0

username =""
while not username:
    username = input("Username: ")

password =""
while not password:
     password = input("Password: ")


if username == "M.Dawson" and password == "secret":
    print("Hi. Mike. ")
    security = 5

elif username == "S.Meir" and password == "civilization":
    print("Hey, Sid.")
    security = 3


else:
    print("Login failed. You're not so exclusive. \n")

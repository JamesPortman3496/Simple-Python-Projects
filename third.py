import random

die1 = random.randint(1,6)
die2 = random.randrange(6) + 1 

print("you rolled a", die1,"and a", die2, "for a total of", die1 + die2)

input("\n\nPress enter to exit.")


#password program 

password = input("Enter your password: ")

if password == "secret":
    print("Access granted")
else:
    print("Access denied")
input("\n\nPress the enter key to exit")
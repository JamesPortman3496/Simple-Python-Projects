#hangman game
import random

#constants
HANGMAN = [7, 6, 5, 4, 3, 2, 1, 0]
MAX_WRONG = len(HANGMAN) - 1
WORDS = ("HANNAH", "JAMES", "PYTHON", "BRISTOL", "WATER", "CHOCOLATE")

#initialse variables
word = random.choice(WORDS)
so_far = "-" * len(word)
wrong = 0
used = []

print("welcome to hangman, good luck")

while wrong < MAX_WRONG and so_far != word:
    print("you have", HANGMAN[wrong], "lives left")
    print("\nYou've used the follownig letters:\n", used)
    print("\nSo far, the word is:\n", so_far)

    guess = input("\n\nEnter your guess: ")
    guess = guess.upper()

    while guess in used:
        print("You've alrewady guessed the letter", guess)
        guess = input("Enter your guess: ")
        guess = guess.upper()
    
    used.append(guess)

    if guess in word:
        print("\nYES!", guess, "is in the word!")

        new = ""
        for i in range(len(word)):
            if guess == word[i]:
                new += guess
            else:
                new += so_far[i]
        so_far = new

    else:
        print("\nSorry,", guess, "isn't in the word.")
        wrong += 1
    
if wrong == MAX_WRONG:
    print("youve been hanged")
else:
    print("you guessed it")

print("the word was", word)

input("\n\nPress enter to exit")
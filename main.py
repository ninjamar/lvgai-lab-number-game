import random

n = random.randint(1, 100)

guesses = 0
while True:
    guess = int(input("Guess the number between 1 and 100: "))
    guesses += 1
    if guess == n:
        print("You guessed it!")
        print("You guessed it in", guesses, "guesses")
        break
    elif guess < n:
        print("Too low")
    else:
        print("Too high")

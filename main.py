import random

n = random.randint(1, 100)

min_guesses = float("inf")
guesses = 0
while True:

    guess = int(input("Guess the number between 1 and 100: "))
    guesses += 1
    if guess == n:
        print("You guessed it!")
        print("You guessed it in", guesses, "guesses")

        if guesses < min_guesses:
            min_guesses = guesses
        if min_guesses < float("inf"):
            print("Best score: ", min_guesses)

        play_again = input("Would you like to play again? (yes/no): ")
        if play_again.lower() != "yes":
            break


        n = random.randint(1, 100)
        guesses = 0
    elif guess < n:
        print("Too low")
    else:
        print("Too high")

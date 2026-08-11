import random

secret_number = random.randint(1, 100)
attempts_left = 7
guess = None  # starts as "nothing guessed yet"

while guess != secret_number and attempts_left > 0:
    guess = int(input("Guess a number between 1-100: "))
    
    if guess < secret_number:
        print("Too low!")
    elif guess > secret_number:
        print("Too high!")
    else:
        print("Correct! You win!")
    
    attempts_left = attempts_left - 1

if guess != secret_number:
    print("Out of attempts! The number was", secret_number)
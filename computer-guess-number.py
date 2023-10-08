import random

def guess_the_number(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f"Enter your guess as an integer between 1 and {x}: "))
        if guess < random_number:
            print("Too low.")
        elif guess > random_number:
            print("Too high.")
    print(f"Your guess is correct! The secret number is {random_number}")

guess_the_number(100)
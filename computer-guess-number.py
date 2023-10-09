import random


# def user_guess_num(x):
#     random_number = random.randint(1, x)
#     guess = 0
#     while guess != random_number:
#         guess = int(input(f"Enter your guess as an integer between 1 and {x}: "))
#         if guess < random_number:
#             print("Too low.")
#         elif guess > random_number:
#             print("Too high.")
#     print(f"Your guess is correct! The secret number is {random_number}!")
#

def computer_guess_num(x):
    low = 1
    high = x
    feedback = ""  # empty string
    while feedback != "c":
        if low != high:
            guess = random.randint(low, high)  # let the computer generate a random guess number
        else:
            guess = high  # or low
        feedback = input(f"Is {guess} too high (H), too low (L), or correct (C): ").lower()
        if feedback == "h":
            high = guess - 1
        elif feedback == "l":
            low = guess + 1

    print(f"{guess} is the correct number!")


computer_guess_num(1000)
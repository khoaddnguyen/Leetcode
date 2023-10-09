import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_images = [rock, paper, scissors]

user = int(input("Enter 0 for Rock, 1 for Paper, 2 for Scissors: \n"))
computer = random.randint(0, 2)

if user >= 3 or user < 0:
    print("You typed an invalid number. You lose!")
else:
    print(f"Computer choose: {computer}" + game_images[computer])
    if user == 0 and computer == 2:
        print("You win!")
    elif user == 2 and computer == 2:
        print("You lose.")
    elif user < computer:
        print("You lose.")
    elif user > computer:
        print("You win!")
    elif user == computer:
        print("Tie!")

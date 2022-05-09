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
list_of_choices = [rock, paper, scissors]

user_choice = int(input("What do you choose? 0 - Rock, 1 - Paper, 2 - Scissors.\n"))
if user_choice >=3 or user_choice < 0:
    print("Invalid number. You lose")
else:
    print(list_of_choices[user_choice])
    computer_choice = random.randint(0, 2)
    print(list_of_choices[computer_choice])

    if user_choice == 2 and computer_choice == 0:
        print("You lose")
    elif user_choice == 0 and computer_choice == 2:
        print("You win!")
    elif computer_choice > user_choice:
        print("You lose")
    elif user_choice > computer_choice:
        print("You win!")
    elif user_choice == computer_choice:
        print("It's a draw")


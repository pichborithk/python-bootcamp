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

#Write your code below this line 👇
map = [rock, paper, scissors]

your_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors\n"))

print(map[your_choice])

computer_choice = random.randint(0,2)

print(map[computer_choice])

if your_choice == computer_choice:
    print("It's a draw")
elif (your_choice == 2 and computer_choice == 0) or (your_choice == 1 and computer_choice == 2) or (your_choice == 0 and computer_choice == 1):
    print("You lose")
else:
    print("You win")
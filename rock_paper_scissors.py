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
asciiDesign = [rock, paper, scissors]

user_decision = int(input("Please select 0: Rock, 1: Paper, 2: Scissors"))

computer_decision = random.randint(1,3)

if user_decision >= 3 or user_decision < 0:
    print("Invalid input received ")
else: 
    if user_decision == 0 and computer_decision == 2:
        print(f"You win, you choose {asciiDesign[user_decision]} and computer choose {asciiDesign[computer_decision]}") 
    elif user_decision == 2 and computer_decision == 0:
        print(f"You loose, you choose {asciiDesign[user_decision]} and computer choose {asciiDesign[computer_decision]}") 
    elif user_decision > computer_decision:
        print(f"You win, you choose {asciiDesign[user_decision]} and computer choose {asciiDesign[computer_decision]}") 
    elif user_decision == computer_decision:
        print(f"This is a draw, you choose {asciiDesign[user_decision]} and computer choose {asciiDesign[computer_decision]}")
    else: 
        print(f"You loose, you choose {asciiDesign[user_decision]} and computer choose {asciiDesign[computer_decision]}")


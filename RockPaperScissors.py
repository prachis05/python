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
---'    ____)____
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


users_choice = int(input("What do you choose? Type 0 for rock,1 for paper or 2 for scissors "))
if users_choice == 0:
    print(rock)
elif users_choice == 1:
    print(paper)
elif users_choice == 2:
    print(scissors) 

computers_choice  = random.randint(0,2)
if computers_choice == 0:
    print(f"COmputers choice{rock}")
elif computers_choice == 1:
    print(f"COmputers choice{paper}")
elif computers_choice == 2:
    print(f"COmputers choice{scissors}") 

if computers_choice == 0 and users_choice == 0:
    print("DRAW")
elif computers_choice == 1 and users_choice == 1:
    print("DRAW")
elif computers_choice == 2 and users_choice == 2:
    print("DRAW0")
elif computers_choice == 0 and users_choice == 1:
    print("You won!!!")
elif computers_choice == 0 and users_choice == 2:
    print("Computer won") 
elif computers_choice == 1 and users_choice == 0:
    print("Computer won!!!")
elif computers_choice == 1 and users_choice == 2:
    print("You wonn")
elif computers_choice == 2 and users_choice == 1:
    print("Computer won")
elif computers_choice == 2 and users_choice == 0:
    print("You wonn!!!")


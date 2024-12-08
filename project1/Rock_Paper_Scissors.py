#Rock wins against scissors
#Scissors wins aginst paper
#Paper wins against Rock

#0 for Rock; 1 for Paper; 2 for Scissors
#Two players; computer and an individual
import random

Rock = '''   _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
Paper ='''    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''
Scissors ='''   _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
User_choice = int(input("Instruction:Type 0 for Rock, 1 for Paper,2 for Scissors.\nEnter your choice: "))
print(User_choice)
 
if User_choice >= 3 or User_choice < 0:
    print("Your input is INVALID.Kindly check the instruction")
else:
    game_image = [Rock,Paper,Scissors]
    print(game_image[User_choice])
    Computer_choice = random.randint(0,2)
    print(game_image[Computer_choice])
    if Computer_choice == 0 and  User_choice == 2:
        print("You Lose 😞")
    elif User_choice == 0 and  Computer_choice == 2:
        print("You Won 👏")
    elif Computer_choice == 1 and User_choice == 0:
        print("You loose 😞")
    elif User_choice == 1 and  Computer_choice == 0:
        print("You Won 👏")
    elif Computer_choice == 2 and User_choice == 1:
        print("You loose 😞")
    elif User_choice == 2 and  Computer_choice == 1:
        print("You Won 👏")
    elif Computer_choice > User_choice:
        print("You lose 😞")
    elif Computer_choice < User_choice:
        print("You Won 👏")
    elif Computer_choice == User_choice:
        print("It is a draw 🥵")
     
    





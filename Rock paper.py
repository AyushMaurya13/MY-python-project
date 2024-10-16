import random # Please Check and understand it 

rock = '''
    ________
___'    ____)
        (____)
        (____)
        (____)
        (___)
---.____
'''
paper = '''
    ________
___'    ____)____
        (________)
        (__________)
        (_______)
        (______)
---.____
'''

scissors = '''
    ________
___'    ____)____
        (________)
        (__________)
        (_____)
        (____)
---.____
'''

game_images = [rock ,paper,scissors]


user_choice = int(input("What do you choose ? Type 0 for Rock 1 for paper or 2 for Scissors\n"))
print(f"You Chose {user_choice} ")
print(game_images[user_choice])


compuer_choice = random.randint(0,2)
print(f"Computer Chose {compuer_choice}  ")
print(game_images[compuer_choice])


if user_choice >= 3 or compuer_choice < 0:
    print("You type an invalid Number You lose ")

elif user_choice == 0 and compuer_choice == 2:
    print("You win")

elif compuer_choice == 0 and user_choice == 2:
    print("you lose ")

elif compuer_choice > user_choice:
    print("You Lose!")

elif user_choice > compuer_choice:
    print("You win")

elif compuer_choice == user_choice:
    print("It's Draw")

else:
    print("You type invalid number")
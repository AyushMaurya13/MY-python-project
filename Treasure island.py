print('''*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************''')
print("Welcome to Treasure island Your mission is to find the treasure.")

choice_1 = input('where you want to go "Left" or "Right" ').lower()#lower() method is used to convert all uppercase characters in a string to lowercase
if choice_1 == "left":
    choice_2 = input('You want to "Wait " or"swim" ').lower()#lower() method is used to convert all uppercase characters in a string to lowercase
    if choice_2 == "wait":
        choice_3 = input("Select the Door Red , Blue or Yellow ").lower()#lower() method is used to convert all uppercase characters in a string to lowercase
        if choice_3 == "red":#there is lowercase 
            print("Burned by fire Game over")
        elif choice_3 == "blue":# == operator in Python is used to compare two values for equality1. ''''It returns True if the values are equal, and False otherwise''''''
            print("Eaten by beasts Game over")

        elif choice_3 == "yellow":
            print("You win")

        else:
            print("Game over")
    else:
        print("Attacked by trout Game Over")

else:
    print("Fall into a hole Game over .")        

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
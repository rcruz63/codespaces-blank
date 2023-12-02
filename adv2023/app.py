"""This is the main application file for the adv2023 package. """
from adv2023.dia1.dia1 import dia1_1, dia1_2


def run():
    """This is the main function for the adv2023 package. """
    # Use a loop to keep representing a menu until the user chooses to exit
    while True:
        # Print the menu
        print("Welcome to the menu")
        print("1. Dia 1")
        print("Q. Exit")

        # Ask the user for a choice
        choice = input("What would you like to do? ")
        # If the user chooses option 1, call option1()
        if choice == "1":
            dia1_1("data1_1.txt")
            dia1_2("data1_2.txt")
        # If the user chooses Q, exit the loop
        elif choice.upper() == "Q":
            break
        else:
            print("That is not a valid option")

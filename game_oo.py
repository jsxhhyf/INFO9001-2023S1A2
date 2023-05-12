"""
Write your answer for the full OO version of the game here.

Author:
SID:
Unikey:
"""
from datetime import datetime

from game_final import display_title, run_setup, personalization
from hunter import Hunter
from interface import Interface
from setup import installation
from train import train
from trap import Trap


def main():
    # 1. Check setup
    # master = "/home/master/"
    master = "/Users/philliphu/Documents/TUTOR/INFO9001/2023S1/Assignment2/master/"
    timestamp = datetime.now().strftime("%d %b %Y %H:%M:%S ")

    tempered: bool = False
    if run_setup(master, timestamp):
        user_input = input("Do you want to repair the game? ")
        if user_input != "yes" and user_input != "YES":
            print("Game may malfunction and personalization will be locked.")
            user_confirm = input("Are you sure you want to proceed? ")
            if user_confirm == "yes" or user_confirm == "YES":
                print("You have been warned!!!")
                tempered = True
            else:
                installation(master, timestamp)
        else:
            installation(master, timestamp)

    print("Launching game")
    print(".")
    print(".")
    print(".")

    # 2. Display title
    display_title()

    # 3. Get a proper player name
    hunter_name = personalization(tempered)

    # 4. Training process
    trap_name, enchanted = train()
    trap = Trap(name=trap_name, enchant=enchanted)
    hunter = Hunter(name=hunter_name, trap=trap)

    # 5. Game process
    interface = Interface(hunter)

    while True:
        print(interface.get_menu())
        player_input = input("Enter a number between 1 and 4: ")
        print("")
        if player_input.isdigit():
            player_input = int(player_input)
            if player_input < 1 or player_input > 4:
                print("Must be between 1 and 4.")
                continue
            status = interface.move_to(player_input)
            if status == 0:
                break
        else:
            print("Sorry, input is invalid")


if __name__ == "__main__":
    main()

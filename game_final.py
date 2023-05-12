"""
Answer for Question 7 - PIAT: Improved Full Game.

Author:
SID:
Unikey:
"""
from datetime import datetime

import name
import train
from art import BROWN
from setup import verification, installation


def run_setup(master, timestamp) -> bool:
    logs = verification(master, timestamp)
    if logs[-1] == "Abnormalities detected...":
        return True


def display_title():
    print("Mousehunt")
    print(BROWN)
    print("Inspired by Mousehunt© Hitgrab")
    print("Programmer - An INFO1110/COMP9001 Student")
    print("Mice art - Joan Stark and Hayley Jane Wakenshaw\n")


def get_hunter_name() -> str:
    """
    Ask the user to input a name
    Returns
    -------
    str:
    """
    player_input = input("What's ye name, Hunter? ")
    return player_input


def personalization(temper_flag: bool) -> str:
    if temper_flag:
        print("Welcome to the Kingdom, Hunter Bob!")
        return "Bob"

    num_attempts = 1
    hunter_name = get_hunter_name()

    if not name.is_valid_name(hunter_name):
        print("That's not nice!")
        print(f"I'll give ye 3 attempts to get it right or I'll name ye!")
        print("let's try again...")
        i = 0
        while i < 3:
            hunter_name = get_hunter_name()
            if not name.is_valid_name(hunter_name):
                if num_attempts < 3:
                    print(f"Nice try. Strike {num_attempts}")
                    num_attempts += 1
                    i += 1
                else:
                    print("I told ye to be nice!!!")
                    hunter_name = name.generate_name(hunter_name)
                    print(f"Welcome to the Kingdom, Hunter {hunter_name}!")
                    return hunter_name

            else:
                print(f"Welcome to the Kingdom, Hunter {hunter_name}!")
                return hunter_name

    else:
        print(f"Welcome to the Kingdom, Hunter {hunter_name}!")
        return hunter_name


def welcome_hunter() -> str:
    """
    returns trap from training or cardboard and hook trap if skipped
    """

    print("Before we begin, let's train you up!")
    # player_input -----> '' = start training / 'skip' = start game
    player_input = input('Press "Enter" to start training or "skip" to Start Game: ')

    while player_input != "" and player_input != "skip" and not player_input.startswith("\x1b"):
        print("Sorry did not understand!\n")
        player_input = input('Press "Enter" to start training or "skip" to Start Game: ')

    if player_input == "":
        print("")
        trap, e_flag = train.repeat_training()
        print("")
        return trap if not e_flag else "One-time Enchanted " + trap
    elif player_input == "skip" or player_input.startswith("\x1b"):
        print("")
        trap = "Cardboard and Hook Trap"
        return trap


def get_game_menu(hunter_name: str) -> str:
    """
    Returns a string displaying all possible actions at the game menu.
    """

    menu = [
        f"What do ye want to do now, Hunter {hunter_name}?",
        "1. Exit game",
        "2. Join the Hunt",
        "3. The Cheese Shop",
        "4. Change Cheese",
    ]
    return "\n".join(menu)


if __name__ == "__main__":

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

    display_title()

    hunter_name = personalization(tempered)

    trap = welcome_hunter()

    while True:
        print(get_game_menu(hunter_name))
        pl_menu_input = input("Enter a number between 1 and 4. \n")
        if pl_menu_input == "1":
            break
        elif pl_menu_input == "2":
            # cheese = consume_cheese(to_eat, cheese)
            gold, points = hunt(gold, cheese, trap_cheese, points)
        elif pl_menu_input == "3":
            gold_used, cheese = game_shop_function(trap, gold, cheese)
            cheddar_num = cheese[0][1]
            marble_num = cheese[1][1]
            swiss_num = cheese[2][1]
            gold -= gold_used
            cheese = [
                ("cheddar", cheddar_num),
                ("marble", marble_num),
                ("swiss", swiss_num),
            ]
        elif pl_menu_input == "4":
            trap_status, trap_cheese = change_cheese(hunter_name, trap, cheese, e_flag)
        elif pl_menu_input.isdigit() and (int(pl_menu_input) < 1 or int(pl_menu_input) > 4):
            print("Must be between 1 and 4.")
        else:
            print("Sorry, input is invalid")
            print("")

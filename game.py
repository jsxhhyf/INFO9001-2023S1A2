"""
This file should borrow code from your Assignment 1.
However, it will require some modifications for this assignment.

Author:
SID:
Unikey:
"""
from art import BROWN
from shop import shop

"""
Keep this line!
"""
import random

"""
We recommend you import your 'name', 'train' and 'shop' modules to complete this 
question. It will save trouble in needing to copy and paste code from previous 
questions. However if you wish not to, you are free to remove the imports below.
Feel free to import other modules that you have written.
"""
import name
import train


# you can make more functions or global read-only variables here if you please!


def display_title():
    print("Mousehunt")
    print(BROWN)
    print("Inspired by Mousehunt© Hitgrab")
    print("Programmer - An INFO1110/COMP9001 Student")
    print("Mice art - Joan Stark and Hayley Jane Wakenshaw\n")


def get_hunter_name():
    player_input = input("What's ye name, Hunter?\n")
    if name.is_valid_name_a1(player_input):
        return player_input
    else:
        return "Bob"


def get_game_menu(hunter_name) -> str:
    """
    untouched
    Returns a string displaying all possible actions at the game menu.
    """

    menu = (
        f"What do ye want to do now, Hunter {hunter_name}?",
        "1. Exit game",
        "2. Join the Hunt",
        "3. The Cheese Shop",
        "4. Change Cheese",
    )
    return "\n".join(menu)


def display_inventory(
    trap: str, gold: int, cheese: list
) -> None:  # display function -----> gold, cheese, trap are parameters
    cheddar, marble, swiss = cheese
    cheddar_num = cheddar[1]
    marble_num = marble[1]
    swiss_num = swiss[1]
    print(f"Gold - {gold}")
    print(f"Cheddar - {cheddar_num}")
    print(f"Marble - {marble_num}")
    print(f"Swiss - {swiss_num}")
    print(f"Trap - {trap}")


def change_cheese(hunter_name: str, trap: str, cheese: list, e_flag: bool = False) -> tuple:
    """
    Handles the inputs and ouputs of the change cheese feature.
    Parameters:
        hunter_name: str,        the name of the player.
        trap:        str,        the trap name.
        cheese:      list,       all the cheese and its quantities the player
                                 currently possesses.
        e_flag:      bool,       if the trap is enchanted, this will be True.
                                 default value is False.
    Returns:
        trap_status: bool,       True if armed and False otherwise.
        trap_cheese: str | None, the type of cheese in the trap. if player
                                 exits the function without  arming
                                 trap successfully, this value is None.
    """
    # available_cheeses = ['cheddar', 'marble', 'swiss']
    trap_status = False
    trap_cheese = None
    num_cheddar, num_marble, num_swiss = cheese[0][1], cheese[1][1], cheese[2][1]

    while True:
        print(f"Hunter {hunter_name}, you currently have:")
        print(f"Cheddar - {num_cheddar}")
        print(f"Marble - {num_marble}")
        print(f"Swiss - {num_swiss}")
        print("")
        pl_cheese_choice_input = input("Type cheese name to arm trap: ").strip().lower()

        if pl_cheese_choice_input == "back":
            print("")
            return trap_status, trap_cheese

        if pl_cheese_choice_input == "cheddar":
            if num_cheddar == 0:
                print("Out of cheese!")
            else:
                pl_confirm_change_input = input("Do you want to arm your trap with Cheddar? ").strip().lower()
                if pl_confirm_change_input == "yes":
                    print(f"{trap} is now armed with Cheddar!")
                    print("")
                    trap_status = True
                    trap_cheese = "cheddar"
                    break
                elif pl_confirm_change_input == "back":
                    print("")
                    break
                else:
                    print("")

        elif pl_cheese_choice_input == "marble":
            if num_marble == 0:
                print("Out of cheese!")
            else:
                pl_confirm_change_input = input("Do you want to arm your trap with Marble? ").strip().lower()
                if pl_confirm_change_input == "yes":
                    print(f"{trap} is now armed with Marble!")
                    print("")
                    trap_status = True
                    trap_cheese = "marble"
                    break
                elif pl_confirm_change_input == "back":
                    print("")
                    break
                else:
                    print("")

        elif pl_cheese_choice_input == "swiss":
            if num_swiss == 0:
                print("Out of cheese!")
            else:
                pl_confirm_change_input = input("Do you want to arm your trap with Swiss? ").strip().lower()
                if pl_confirm_change_input == "yes":
                    print(f"{trap} is now armed with Swiss!")
                    print("")
                    trap_status = True
                    trap_cheese = "swiss"
                    break
                elif pl_confirm_change_input == "back":
                    print("")
                    break
                else:
                    print("")

        else:
            print("No such cheese!")

    return trap_status, trap_cheese


def consume_cheese(to_eat: str, cheese: list) -> None:
    """
    Handles the consumption of cheese.
    Will modify the cheese list, if required.
    Parameters:
        to_eat:    str,        the type of cheese to consume during the hunt.
        cheese:    list,       all the cheeses and quantities the player
                               currently possesses.
    """
    if to_eat == "Cheddar" or to_eat == "Marble" or to_eat == "Swiss":
        i = 0
        while i < len(cheese):
            if cheese[i][0] == to_eat:
                cheese[i] = (cheese[i][0], cheese[i][1] - 1)
                break
            else:
                i += 1
    else:
        print("Wrong name of cheese!")


def hunt(gold: int, cheese: list, trap_cheese: str | None, points: int) -> tuple:
    """
    Handles the hunt mechanic.
    It includes the inputs and outputs of sounding the horn, the result of
    the hunt, the gold and points earned, and whether users want to continue
    after failing consecutively.
    The function will modify the cheese list, if required.
    Parameters:
        gold:        int,        the quantity of gold the player possesses.
        cheese:      list,       all the cheese and quantities the player
                                 currently possesses.
        trap_cheese: str | None, the type of cheese that the trap is currently
                                 armed with. if it's not armed, value is None.
        points:      int,        the quantity of points that the player
                                 currently possesses.
    Returns:
        gold:        int,        the updated quantity of gold after the hunt.
        points:      int,        the updated quantity of points after the hunt.
    """

    cheese_num = 0
    num_fails = 0

    while True:
        # get the number of cheese armed
        i = 0
        while i < len(cheese):
            if cheese[i][0] == trap_cheese:
                cheese_num = cheese[i][1]
                break
            else:
                i += 1
        if cheese_num == 0:
            print("Nothing happens. You are out of cheese!")
            continue

        random_value = random.random()
        print("Sound the horn to call for the mouse...")
        pl_horn_input = input('Sound the horn by typing "yes": ').strip().lower()
        print("")

        if pl_horn_input == "stop hunt":
            print("")
            return gold, points

        if pl_horn_input != "yes":
            print("invalid input")
            print("")

        if cheese_num > 0:
            consume_cheese(trap_cheese, cheese)
            if random_value > 0.5:
                num_fails = 0
                gold += 125
                points += 115
                print("Caught a Brown mouse!")
                print(f"My gold: {gold}, My points {points}")
                print("")
            else:
                num_fails += 1
                print("Nothing happens")
                print(f"My gold: {gold}, My points {points}")
                print("")
        else:
            num_fails += 1
            print("Nothing happens. You are out of cheese!")
            print(f"My gold: {gold}, My points: {points}")
            print("")

        if num_fails == 5:
            pl_confirm = input("Do you want to continue to hunt? ").strip().lower()
            if pl_confirm != "yes":
                return gold, points
            else:
                num_fails = 0


def main():
    # 1. display game title
    display_title()

    # 2. get a proper name for the player
    hunter_name = get_hunter_name()
    print(f"Welcome to the Kingdom, Hunter {hunter_name}!")

    # 3. training process
    trap, enchant = train.train()

    # 4. Game process
    cheese = [("Cheddar", 0), ("Marble", 0), ("Swiss", 0)]
    trap_cheese = None
    gold = 125
    points = 0

    while True:
        print(get_game_menu(hunter_name))
        pl_menu_input = input("")
        if pl_menu_input == "1":
            break
        elif pl_menu_input == "2":
            gold, points = hunt(gold, cheese, trap_cheese, points)
        elif pl_menu_input == "3":
            gold, cheese = shop(trap, gold, cheese)
        elif pl_menu_input == "4":
            trap_status, trap_cheese = change_cheese(hunter_name, trap, cheese, enchant)
            if isinstance(trap_cheese, str):
                trap_cheese = trap_cheese.capitalize()
        else:
            print("Sorry, input is invalid")
            print("")


if __name__ == "__main__":
    main()

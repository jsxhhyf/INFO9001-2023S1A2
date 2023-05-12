"""
Write your solution to 1. Upgraded Cheese Shop here.
It should borrow code from Assignment 1.

Author:
SID:
Unikey:
"""

CHEESE_MENU = (("Cheddar", 10), ("Marble", 50), ("Swiss", 100))


# you can make more functions or global read-only variables here if you please!


def greet():
    greets = [
        "Welcome to the Cheese Shop!",
        f"{CHEESE_MENU[0][0]} - {CHEESE_MENU[0][1]}",
        f"{CHEESE_MENU[1][0]} - {CHEESE_MENU[1][1]}",
        f"{CHEESE_MENU[2][0]} - {CHEESE_MENU[2][1]}",
    ]
    print("\n".join(greets) + "\n")


def get_shop_menu():
    menu = [
        "How can I help ye?",
        "1. Buy cheese",
        "2. View inventory",
        "3. Leave shop",
    ]
    return "\n".join(menu)


def buy_cheese(gold: int) -> tuple:
    """
    Feature for players to buy cheese from shop
    Parameters:
        gold:           int,    amount of gold that player has
    Returns:
        gold_spent:     int,    amount of gold spent
        cheese_bought:  tuple,  amount of each type of cheese bought
    """

    if not isinstance(gold, int):
        print("Invalid argument!\nThe argument gold must be an integer.")
        return 0, (0, 0, 0)

    gold_used = 0
    cheese_bought = (0, 0, 0)

    while True:
        print(f"You have {gold} gold to spend.")
        pl_cheese_input = input("State [cheese quantity]: ").split()
        if len(pl_cheese_input) == 0:
            print("Invalid command.")
            continue

        cheese_name = pl_cheese_input[0].strip().lower()
        if cheese_name == "back":
            break

        if not cheese_name[0].isalpha() or (
            cheese_name != "cheddar" and cheese_name != "marble" and cheese_name != "swiss"
        ):
            print(f"We don't sell {cheese_name}")
            continue

        if len(pl_cheese_input) == 1:
            print("Missing quantity.")
            continue
        else:
            quantity = pl_cheese_input[1]

        if not quantity.isdigit():
            print("Invalid quantity.")
            continue
        elif int(quantity) <= 0:
            print("Must purchase positive amount of cheese.")
            continue
        else:
            quantity = int(quantity)

        if cheese_name == "cheddar":
            if gold >= 10 * quantity:
                cheese_bought = (cheese_bought[0] + quantity, cheese_bought[1], cheese_bought[2])
                gold_used += 10 * quantity
                gold -= 10 * quantity
                print(f"Successfully purchase {quantity} cheddar.")
            else:
                print("Insufficient gold.")
                continue
        elif cheese_name == "marble":
            if gold >= 50 * quantity:
                cheese_bought = (cheese_bought[0], cheese_bought[1] + quantity, cheese_bought[2])
                gold_used += 50 * quantity
                gold -= 50 * quantity
                print(f"Successfully purchase {quantity} marble.")
            else:
                print("Insufficient gold.")
                continue
        elif cheese_name == "swiss":
            if gold >= 100 * quantity:
                cheese_bought = (cheese_bought[0], cheese_bought[1], cheese_bought[2] + quantity)
                gold_used += 100 * quantity
                gold -= 100 * quantity
                print(f"Successfully purchase {quantity} swiss.")
            else:
                print("Insufficient gold.")
                continue

    return gold_used, cheese_bought


def display_inventory(trap: str, gold: int, cheese: list) -> None:
    """
    Displays contents of inventory
    Parameters:
        gold:   int,  amount of gold that player has
        cheese: list, amount of each type of cheese that player has
        trap:   str,  name of trap that player has
    """

    # cheddar, marble, swiss = cheese[0][1], cheese[1][1], cheese[2][1]

    print(f"Gold - {gold}")
    print(f"Cheddar - {cheese[0][1]}")
    print(f"Marble - {cheese[1][1]}")
    print(f"Swiss - {cheese[2][1]}")
    print(f"Trap - {trap}")


def shop(trap: str, gold: int, cheese: list[tuple, tuple, tuple]) -> tuple[int, list]:
    """
    shop function
    :param trap: trap name
    :type trap: str
    :param gold: amount of gold player has when entering shop
    :type gold: int
    :param cheese: number different types of cheese player has
    :type cheese: list[tuple, tuple, tuple]
    :return: amount of money left after shopping and the updated cheese numbers
    :rtype: tuple[int, list]
    """
    # gold = 125
    # gold_used = 0
    # cheese = [("cheddar", 0), ("marble", 0), ("swiss", 0)]
    # trap = "Cardboard and Hook Trap"

    # 1. greet
    greet()

    while True:
        # 2. display the menu
        print(get_shop_menu())
        player_input = input("")
        # 3. buy cheese
        if player_input == "1":
            gold_used, cheese_bought = buy_cheese(gold)
            gold -= gold_used
            cheese = [
                ("Cheddar", cheese[0][1] + cheese_bought[0]),
                ("Marble", cheese[1][1] + cheese_bought[1]),
                ("Swiss", cheese[2][1] + cheese_bought[2]),
            ]
        # 4. view inventory
        elif player_input == "2":
            display_inventory(trap, gold, cheese)
        # 5. leave shop
        elif player_input == "3":
            break
        else:
            print("I did not understand.")
    return gold, cheese


def main():
    trap = "Cardboard and Hook Trap"
    gold = 125
    cheese = [("cheddar", 0), ("marble", 0), ("swiss", 0)]
    shop(trap, gold, cheese)


if __name__ == "__main__":
    main()

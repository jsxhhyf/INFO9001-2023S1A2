"""
Write your solution for the class CheeseShop here.
This is your answer for Question 8.3.

Author:
SID:
Unikey:
"""
from hunter import Hunter


class CheeseShop:
    def __init__(self):
        self.cheeses = {"Cheddar": 10, "Marble": 50, "Swiss": 100}
        self.menu = {"1": "Buy cheese", "2": "View inventory", "3": "Leave shop"}

    def get_cheeses(self) -> str:
        ret = [
            f"Cheddar - {self.cheeses['Cheddar']}",
            f"Marble - {self.cheeses['Marble']}",
            f"Swiss - {self.cheeses['Swiss']}",
        ]
        return "\n".join(ret)

    def get_menu(self) -> str:
        ret = [
            f"1. - {self.menu['1']}",
            f"2. - {self.menu['2']}",
            f"3. - {self.menu['3']}",
        ]
        return "\n".join(ret)

    def greet(self) -> str:
        return "Welcome to the cheese shop!\n" + self.get_cheeses() + "\n"

    def buy_cheese(self, gold: int) -> tuple[int, tuple]:
        """
        Buy cheeses
        Parameters
        ----------
        gold : the amount of gold player has

        Returns
        -------
        tuple[int, list]: the amount of gold left and the list of cheeses player has bought from the shop
        """
        bought = {"cheddar": 0, "marble": 0, "swiss": 0}

        if not isinstance(gold, int):
            print("Invalid argument!\nThe argument gold should be an integer.")
            return gold, tuple(bought.values())

        print(f"You have {gold} gold to spend.")
        while True:
            player_request: list = input("State [cheese quantity]: ").split()
            if len(player_request) == 0:
                print("Invalid input.")
                continue

            cheese_name = player_request[0]

            if cheese_name.strip().lower() == "back":
                return gold, tuple(bought.values())

            if not cheese_name.isalpha() or (
                cheese_name != "cheddar" and cheese_name != "marble" and cheese_name != "swiss"
            ):
                print(f"We don't sell {player_request[0]}!")
                continue

            if len(player_request) == 1:
                print("Missing quantity.")
                continue
            else:
                quantity = player_request[1]

            # if quantity is invalid
            if not quantity.isdigit():
                print("Invalid quantity.")
                continue
            # if quantity is not positive
            elif int(quantity) <= 0:
                print("Must purchase positive amount of cheese.")
                continue
            else:
                quantity = int(quantity)
                # insufficient gold
                if quantity * self.cheeses[cheese_name.capitalize()] > gold:
                    print("Insufficient gold.")
                    continue
                else:
                    gold -= quantity * self.cheeses[cheese_name.capitalize()]
                    print(f"Successfully purchase {quantity} {cheese_name}.")
                    bought[cheese_name] += quantity
                    continue

    def move_to(self, hunter: Hunter) -> None:
        while True:
            print("How can I help ye?")
            print(self.get_menu())

            player_request: str = input("")

            # invalid input
            if len(player_request) == 0 or player_request[0].isalpha():
                print("I did not understand.")
                continue

            try:
                if player_request.isdigit():
                    selection = int(player_request)
                    # beyond range between 1 and 3
                    if selection < 1 or selection > 3:
                        raise ValueError("Selection out of range.")
                    else:
                        if selection == 1:
                            gold, cheese = self.buy_cheese(hunter.get_gold())
                            if cheese:
                                hunter.update_cheese(cheese)
                                hunter.set_gold(gold)
                        elif selection == 2:
                            print(hunter.display_inventory())
                        elif selection == 3:
                            return
            except ValueError:
                continue

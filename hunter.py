"""
Write your solution for the class Hunter here.
This is your answer for Question 8.2.

Author:
SID:
Unikey:
"""
from name import is_valid_name
from trap import Trap


class Hunter:
    def __init__(self, name: str = "Bob", trap: Trap = Trap()):
        self.name = name
        self.cheese = [["Cheddar", 0], ["Marble", 0], ["Swiss", 0]]
        self.trap = trap
        self.gold = 125
        self.points = 0

    # setters and getters
    def set_name(self, player_name) -> None:
        if is_valid_name(player_name):
            self.name = player_name

    def set_cheese(self, cheese_amount: tuple[int, int, int]) -> None:
        if not isinstance(cheese_amount, tuple):
            print("Invalid argument!\nThe argument cheese_amount should be a tuple of three integers.")
            return
        if (
            not isinstance(cheese_amount[0], int)
            or not isinstance(cheese_amount[1], int)
            or not isinstance(cheese_amount[2], int)
        ):
            print("Invalid argument!\nThe argument cheese_amount should be a tuple of three integers.")
            return
        self.cheese[0][1] = cheese_amount[0]
        self.cheese[1][1] = cheese_amount[1]
        self.cheese[2][1] = cheese_amount[2]

    def set_gold(self, gold_amount: int) -> None:
        if not isinstance(gold_amount, int):
            print("Invalid argument!\nThe argument gold_amount should be an integer.")
            return
        self.gold = gold_amount

    def set_points(self, points_amount: int) -> None:
        if not isinstance(points_amount, int):
            print("Invalid argument!\nThe argument points_amount should be an integer.")
            return
        self.points = points_amount

    def get_name(self) -> str:
        return self.name

    def get_cheese(self) -> str:
        ret = [
            f"{self.cheese[0][0]} - {self.cheese[0][1]}",
            f"{self.cheese[1][0]} - {self.cheese[1][1]}",
            f"{self.cheese[2][0]} - {self.cheese[2][1]}",
        ]
        return "\n".join(ret)

    def get_gold(self) -> int:
        return self.gold

    def get_points(self) -> int:
        return self.points

    def get_trap(self) -> Trap:
        return self.trap

    # other functions required
    def update_cheese(self, cheese_amount: tuple[int, int, int]) -> None:
        if not isinstance(cheese_amount, tuple):
            print("Invalid argument!\nThe argument cheese_amount should be a tuple of three integers.")
            return
        if (
            not isinstance(cheese_amount[0], int)
            or not isinstance(cheese_amount[1], int)
            or not isinstance(cheese_amount[2], int)
        ):
            print("Invalid argument!\nThe argument cheese_amount should be a tuple of three integers.")
            return
        self.cheese[0][1] += cheese_amount[0]
        self.cheese[1][1] += cheese_amount[1]
        self.cheese[2][1] += cheese_amount[2]

    def consume_cheese(self, cheese: str) -> None:
        if cheese == "Cheddar":
            self.cheese[0][1] = self.cheese[0][1] - 1 if self.cheese[0][1] > 0 else 0
        elif cheese == "Marble":
            self.cheese[1][1] = self.cheese[1][1] - 1 if self.cheese[1][1] > 0 else 0
        elif cheese == "Swiss":
            self.cheese[2][1] = self.cheese[2][1] - 1 if self.cheese[2][1] > 0 else 0
        else:
            print("Invalid cheese name provided!")
            return

    def have_cheese(self, cheese: str | None = None) -> int:
        if not isinstance(cheese, str) and cheese is not None:
            print("Invalid argument!\nThe argument cheese should be a string.")
            return 0
        if cheese is None or cheese == "Cheddar":
            return self.cheese[0][1]
        elif cheese == "Marble":
            return self.cheese[1][1]
        elif cheese == "Swiss":
            return self.cheese[2][1]
        else:
            print("Invalid cheese name provided!")
            return 0

    def display_inventory(self) -> str:
        gold = f"Gold - {self.gold}"
        trap = f"Trap - {self.trap}"
        return "\n".join([gold, self.get_cheese(), trap])

    def arm_trap(self, trap_cheese: str) -> None:
        if self.have_cheese(trap_cheese) > 0:
            self.trap.set_trap_cheese(trap_cheese)
            self.trap.set_arm_status()
        else:
            self.trap.set_trap_cheese(None)
            self.trap.set_arm_status()

    def update_gold(self, amount: int) -> None:
        if not isinstance(amount, int):
            print("Invalid argument!\nThe argument amount should be an int.")
            return
        self.gold += amount

    def update_points(self, amount: int) -> None:
        if not isinstance(amount, int):
            print("Invalid argument!\nThe argument amount should be an int.")
            return
        self.points += amount

    def __str__(self):
        ret = [f"Hunter {self.name}", f"Gold - {self.gold}", f"Points - {self.points}"]
        s1 = "\n".join(ret)
        return "\n".join([s1, self.get_cheese(), f"Trap - {self.trap}"])

"""
Write your solution for the class Trap here.
This is your answer for Question 8.1.

Author:
SID:
Unikey:
"""


class Trap:
    def __init__(self, name: str = "", enchant: bool = False):
        self.trap_name = name
        self.trap_cheese = None
        self.arm_status = False
        self.one_time_enchantment = enchant

    def __str__(self):
        return f"One-time Enchanted {self.trap_name}" if self.one_time_enchantment else self.trap_name

    def set_trap_name(self, name: str) -> None:
        if name != "Cardboard and Hook Trap" and name != "High Strain Steel Trap" and name != "Hot Tub Trap":
            print("Invalid trap name, set trap name to empty.")
            self.trap_name = ""
        else:
            self.trap_name = name

    def set_trap_cheese(self, cheese: str | None) -> None:
        if cheese is None:
            self.trap_cheese = cheese
        elif cheese != "Cheddar" and cheese != "Swiss" and cheese != "Marble":
            print("Invalid trap cheese, set trap cheese to None.")
            self.trap_cheese = None
        else:
            self.trap_cheese = cheese

    def set_arm_status(self) -> None:
        if self.trap_cheese is None or self.trap_name == "":
            self.arm_status = False
        else:
            self.arm_status = True

    def set_one_time_enchantment(self, status) -> None:
        if self.trap_name == "Cardboard and Hook Trap":
            print("Cardboard and Hook Trap cannot be enchanted.")
            self.one_time_enchantment = False
        else:
            self.one_time_enchantment = status

    def get_trap_name(self) -> str:
        return self.trap_name

    def get_trap_cheese(self) -> str:
        return self.trap_cheese

    def get_armm_status(self) -> bool:
        return self.arm_status

    def get_one_time_enchantment(self) -> bool:
        return self.one_time_enchantment

    @staticmethod
    def get_benefit(cheese: str) -> list:
        """
        Return the benefit for each type of cheese
        :param cheese: the cheese name
        :type cheese: str
        :return: the specific benefit
        :rtype: list
        """
        if cheese == "Cheddar":
            return [25, "points", "Brown"]
        elif cheese == "Swiss":
            return [0.25, "rate", "Tiny"]
        elif cheese == "Marble":
            return [25, "gold", "Brown"]

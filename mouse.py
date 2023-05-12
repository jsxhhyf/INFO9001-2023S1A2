"""
Write solutions to 3. New Mouse Release here.

Author:
SID:
Unikey:
"""
from random import random

from art import BROWN, FIELD, GREY, WHITE, TINY

"""
Keep this line!
"""

TYPE_OF_MOUSE = (None, "Brown", "Field", "Grey", "White", "Tiny")


def generate_probability(cheese_type: str, enchant: bool = False) -> tuple[float, float, float, float, float, float]:
    """
    Generate the probability for each combination of cheese type and mouse
    :param cheese_type: the name of cheese
    :type cheese_type: str
    :param enchant: if the trap is enchanted
    :type enchant: bool
    :return: probability of generating a mouse and individual probabilities for each type of mouse
    :rtype: tuple
    """
    if cheese_type == "Cheddar":
        return 0.5, 0.1, 0.15, 0.1, 0.1, 0.05
    elif cheese_type == "Marble":
        return 0.4, 0.05, 0.2, 0.05, 0.02, 0.08
    elif cheese_type == "Swiss":
        if enchant:
            return 0.55, 0.01, 0.05, 0.05, 0.05, 0.4
        else:
            return 0.3, 0.01, 0.05, 0.05, 0.04, 0.15


def generate_mouse(cheese: str = "Cheddar", enchant: bool = False) -> str | None:
    """
    Spawn a random mouse during a hunt depending on cheese type
    Hint: You should be using TYPE_OF_MOUSE in this function.
    Parameters:
        cheese:      str, name of cheese
        enchant:     bool, if the trap is enchanted
    Returns:
        spawn_mouse: str | None, type of mouse
    """
    random_value = random()
    mouse_idx = -1

    probs = generate_probability(cheese, enchant)
    p1 = probs[0]
    p2 = p1 + probs[1]
    p3 = p2 + probs[2]
    p4 = p3 + probs[3]
    p5 = p4 + probs[4]

    if random_value < p1:
        mouse_idx = 0
    elif p1 <= random_value < p2:
        mouse_idx = 1
    elif p2 <= random_value < p3:
        mouse_idx = 2
    elif p3 <= random_value < p4:
        mouse_idx = 3
    elif p4 <= random_value < p5:
        mouse_idx = 4
    elif p5 <= random_value < 1:
        mouse_idx = 5

    return TYPE_OF_MOUSE[mouse_idx]


def generate_coat(mouse: str | None) -> str:
    """
    generate the art of mouse
    :param mouse: name of mouse
    :type mouse: str | None
    :return: the art of mouse
    :rtype: str
    """
    if mouse is None:
        return ""

    if mouse == "Brown":
        return BROWN
    elif mouse == "Field":
        return FIELD
    elif mouse == "Grey":
        return GREY
    elif mouse == "White":
        return WHITE
    elif mouse == "Tiny":
        return TINY


def loot_lut(mouse_type: str | None) -> tuple:
    """
    Look-up-table for gold and points for different types of mouse
    Parameter:
        mouse_type: str | None, type of mouse
    Returns:
        gold:       int, amount of gold reward for mouse
        points:     int, amount of points given for mouse
    """
    if mouse_type is None:
        return 0, 0
    elif mouse_type == "Brown":
        return 125, 115
    elif mouse_type == "Field":
        return 200, 200
    elif mouse_type == "Grey":
        return 125, 90
    elif mouse_type == "White":
        return 100, 70
    elif mouse_type == "Tiny":
        return 900, 200


class Mouse:
    def __init__(self, cheese: str = "Cheddar", enchant: bool = False):
        self.name = generate_mouse(cheese, enchant)
        self.gold, self.points = loot_lut(self.name)
        self.coat = generate_coat(self.name)

    def __str__(self) -> str:
        return self.name if self.name else "None"

    def get_name(self) -> str:
        return self.name

    def get_gold(self) -> int:
        return self.gold

    def get_points(self) -> int:
        return self.points

    def get_coat(self) -> str:
        return self.coat


if __name__ == "__main__":
    main()

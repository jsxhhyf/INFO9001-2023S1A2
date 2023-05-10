'''
Write solutions to 3. New Mouse Release here.

Author:
SID:
Unikey:
'''

'''
Keep this line!
'''
import random

TYPE_OF_MOUSE = (None, "Brown", "Field", "Grey", "White", "Tiny")

def generate_mouse() -> str | None:
    '''
    Spawn a random mouse during a hunt depending on cheese type
    Hint: You should be using TYPE_OF_MOUSE in this function.
    Returns:
        spawn_mouse: str | None, type of mouse
    '''
    random_value = random.random()

    if random_value < 0.5:
        return None
    elif 0.5 <= random_value < 0.6:
        return "Brown"
    elif 0.6 <= random_value < 0.75:
        return "Field"
    elif 0.75 <= random_value < 0.85:
        return "Grey"
    elif 0.85 <= random_value < 0.95:
        return "White"
    elif 0.95 <= random_value < 1:
        return "Tiny"

    return TYPE_OF_MOUSE[random_value]


def loot_lut(mouse_type: str | None) -> tuple:
    '''
    Look-up-table for gold and points for different types of mouse
    Parameter:
        mouse_type: str | None, type of mouse
    Returns:
        gold:       int, amount of gold reward for mouse
        points:     int, amount of points given for mouse
    '''
    if mouse_type == None:
        return (0, 0)
    elif mouse_type == "Brown":
        return (125, 115)
    elif mouse_type == "Field":
        return (200, 200)
    elif mouse_type == "Grey":
        return (125, 90)
    elif mouse_type == "White":
        return (100, 70)
    elif mouse_type == "Tiny":
        return (900, 200)


class Mouse:

    def __init__(self):
        self.name = generate_mouse()
        self.gold, self.points = loot_lut(self.name) 

    def __str__(self) -> str:
        return self.name if self.name else "None"

    def get_name(self) -> str:
        return self.name

    def get_gold(self) -> int:
        return self.gold
    
    def get_points(self) -> int:
        return self.points


if __name__ == "__main__":
    main()

"""
Answer for Question 5 - The Training Again from Assignment 1.

Author:
SID:
unikey:
"""

TYPE_OF_TRAPS = ("Cardboard and Hook Trap", "High Strain Steel Trap", "Hot Tub Trap")


def train() -> tuple[str, bool]:
    """
    The training process
    :return: the trap player gets and if it is enchanted
    :rtype: tuple[str, bool]
    """
    trap = TYPE_OF_TRAPS[0]

    print("Before we begin, let's train you up!")
    player_input = input('Press "Enter" to start training or "skip" to Start Game: ')
    print("")
    if player_input == "skip":
        return trap, False

    # if not skip
    # travel to meadow
    print("Larry: I'm Larry. I'll be your hunting instructor.")
    print("Larry: Let's go to the Meadow to begin your training!")
    player_input = input("Press Enter to travel to the Meadow...").strip().lower()
    if player_input.startswith("\x1b"):
        return trap, False
    print("Travelling to the Meadow...")

    while True:
        # set up trap
        print("Larry: This is your camp. Here you'll set up your mouse trap.")
        print("Larry: Let's get your first trap...")
        player_input = input("Press Enter to view traps that Larry is holding...").strip().lower()
        if player_input.startswith("\x1b"):
            return trap, False

        # display Larry's traps
        print("Larry is holding...")
        print("Left: High Strain Steel Trap")
        print("Right: Hot Tub Trap")
        player_input = input('Select a trap by typing "left" or "right": ').strip().lower()
        if player_input.startswith("\x1b"):
            return trap, False
        elif player_input == "left":
            trap = TYPE_OF_TRAPS[1]
            print("Larry: Excellent choice.")
            print('Your "High Strain Steel Trap" is now set!')
            print("Larry: You need cheese to attract a mouse.")
            print("Larry places one cheddar on the trap!")
        elif player_input == "right":
            trap = TYPE_OF_TRAPS[2]
            print("Larry: Excellent choice.")
            print('Your "Hot Tub Trap" is now set!')
            print("Larry: You need cheese to attract a mouse.")
            print("Larry places one cheddar on the trap!")
        else:
            print("Invalid command! No trap selected.")
            print("Larry: Odds are slim with no trap!")

        # sound the horn
        print("Sound the horn to call for the mouse...")
        player_input = input('Sound the horn by typing "yes": ').strip().lower()
        if player_input.startswith("\x1b"):
            return trap, False

        # Catch mice
        if trap != TYPE_OF_TRAPS[0]:
            print("Caught a Brown mouse!")
            print("Congratulations. Ye have completed the training.")
            print("Good luck~")
            print("")
        else:
            print("Nothing happens.")
            print("To catch a mouse, you need both trap and cheese!")
            print("")

        # if continue training
        player_input = input('Press Enter to continue training and "no" to stop training: ').strip().lower()
        print("")
        if player_input.startswith("\x1b") or player_input == "no":
            return trap, True


def main():
    """
    Implement your code here.
    """
    train()


if __name__ == "__main__":
    main()

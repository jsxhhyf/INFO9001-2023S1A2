'''
Answer for Question 4 - The Training

Name:
SID:
unikey:

'''

# q4.py
def intro():
    print("Larry: I'm Larry. I'll be your hunting instructor.")
    return True 

def travel_to_camp():
    print('Travelling to the Meadow...')
    print('Larry: This is your camp. Here you\'ll set up your mouse trap.')
    print('Larry: Let\'s get your first trap...')
    print('Press Enter to view traps that Larry is holding...', end='')
    choice = input()
    if choice.startswith('\x1b'):
        print('Skipping training...')
        return



def open_choice():
    print("Larry: Let's get your first trap...")
    choices = input("Press Enter to view traps that Larry is holding...")
    if choices == "":
        print("Larry is holding...", "Left: High Strain Steel Trap", "Right: Hot Tub Trap", sep = '\n')
        return True

def setup_trap(cheddar):
    print('Larry is holding...')
    print('Left: High Strain Steel Trap')
    print('Right: Hot Tub Trap')
    print('Select a trap by typing "left" or "right": ', end='')
    choice = input()
    if choice.startswith('\x1b'):
        print('Skipping training...')
        return (None, 0)
    elif choice.lower() == 'left':
        return (('High Strain Steel Trap', 1), cheddar + 1)
    elif choice.lower() == 'right':
        return (('Hot Tub Trap', 2), cheddar + 2)
    else:
        print('Invalid command! No trap selected.')
        return setup_trap(cheddar)

def eqtrap(setup):
    print('Larry is holding...')
    print('Left: ' + setup[0][0])
    print('Right: ' + setup[0][1])
    print('Select a trap by typing "left" or "right": ', end='')
    choice = input()
    if choice.startswith('\x1b'):
        return 'Skipping training...'
    elif choice.lower() == 'left':
        return setup[0][0]
    elif choice.lower() == 'right':
        return setup[0][1]
    else:
        print('Invalid command! No trap selected.')
        return eqtrap(setup)


def sound_horn():
    print('Sound the horn to call for the mouse...')
    print('Sound the horn by typing "yes": ', end='')
    choice = input()
    if choice.startswith('\x1b'):
        return 'Skipping training...'
    elif choice.lower() == 'yes':
        return True
    else:
        print('Invalid command! Please try again.')
        return sound_horn()



def basic_hunt(cheddar: int, horn: str) -> bool:  
    # if horn_input == "yes" and cheddar == 1:
    if cheddar >= 1 and horn == 'yes': 
        print("Caught a Brown mouse!", "Congratulations. Ye have completed the training.", sep = "\n")
        return True
    elif cheddar >= 1 and horn != 'yes':
        print("Nothing happens.")
        print("To catch a mouse, you need both trap and cheese!", sep = "\n")
        return False
    elif cheddar < 1 and horn == 'yes':
        print("Nothing happens.")
        print("To catch a mouse, you need both trap and cheese!", sep = "\n")
        return False
    else:
        print("Nothing happens.")
        return False 

def end(hunt_status):
    if hunt_status == True:
        print("Good luck~")
        return True
    else:
        return False

def input_gold(gold, hunt_status):
    if hunt_status == True:
        gold = gold + 125 
        return gold
    else:
        gold = gold + 0
        return gold


def question4():
    gold = 0
    cheddar = 0
    i = intro()
    travel = travel_to_camp()
    cho = open_choice()
    setup = setup_trap(cheddar)
    horn = sound_horn()
    trap = eqtrap(setup)
    cheddar = setup[1]
    hunt_status = basic_hunt(cheddar, horn)
    end1 = end(hunt_status)
    goldfin = input_gold(gold, hunt_status)
    return end1

def main():
    quest4 = question4()


if __name__ == '__main__':
    main()

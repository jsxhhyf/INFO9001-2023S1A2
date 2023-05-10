'''
Answer for Question 5 - The Training Again from Assignment 1.

Author:
SID:
unikey:
'''

def travel_to_meadow() -> bool: # skip1 (skip, travel)
    print("Larry: I'm Larry. I'll be your hunting instructor.")
    print("Larry: Let's go to the Meadow to begin your training!")
    player_input = input("Press Enter to travel to the Meadow...")   #^[
    if player_input.startswith('\x1b'):
        return True
    else:
        print('Travelling to the Meadow...')
        return False


def intro_to_camp() -> bool:
    # print("Larry: This is your camp. Here you'll set up your mouse trap.")
    print("Larry: Let's get your first trap...")
    player_input = input("Press Enter to view traps that Larry is holding...")
    if player_input.startswith('\x1b'):
        return True
    else:
        return False


def choose_trap() -> tuple[bool, str]:
    print("Larry is holding...")
    print("Left: High Strain Steel Trap")
    print("Right: Hot Tub Trap")
    player_input = input('Select a trap by typing "left" or "right": ')
    player_input_lc = player_input.lower()
    if player_input.startswith('\x1b'):
        trap = 'Cardboard and Hook Trap'
        return (True, trap)
    elif player_input_lc.strip() == 'left':
        print('Larry: Excellent choice.')
        print('Your "High Strain Steel Trap" is now set!')
        print('Larry: You need cheese to attract a mouse.')
        print('Larry places one cheddar on the trap!')
        trap = 'High Strain Steel Trap'
        return (False, trap)
    elif player_input_lc.strip() == 'right':
        print('Larry: Excellent choice.')
        print('Your "Hot Tub Trap" is now set!')
        print('Larry: You need cheese to attract a mouse.')
        print('Larry places one cheddar on the trap!')
        trap = 'Hot Tub Trap'
        return (False, trap)
    else:
        print('Invalid command! No trap selected.')
        print('Larry: Odds are slim with no trap!')
        trap = 'Cardboard and Hook Trap'
        return (False, trap)


def sound_horn() -> tuple[bool, bool]:
    print('Sound the horn to call for the mouse...')
    player_input = input('Sound the horn by typing "yes": ') #^[
    player_input_lc = player_input.lower()
    if player_input.startswith('\x1b'):
        return True, False
    elif player_input_lc.strip() == 'yes':
        return False, True
    else:
        return False, False



def what_happens(trap: str, horn: bool):
    #have trap and horn
    trap_status = trap =='High Strain Steel Trap' or trap == 'Hot Tub Trap'
    if trap_status and horn:
        print("Caught a Brown mouse!")
        print("Congratulations. Ye have completed the training.")
        print('Good luck~')
        print('')
    #does not have trap nor horn
    elif not trap_status and not horn:
        print("Nothing happens.")
        print('')
    # have trap but does not have horn
    # or does not have trap but have horn
    else:
        print("Nothing happens.")
        print("To catch a mouse, you need both trap and cheese!")
        print('')


def repeat_training(): #continues with training unless player inputs esc(^[)
    # set default trap to Cardboard
    trap = "Cardboard and Hook Trap"
    if travel_to_meadow():
        return trap
    print("Larry: This is your camp. Here you'll set up your mouse trap.")
    if intro_to_camp():
        return trap
    skip, trap = choose_trap()
    if skip:
        return trap
    skip, horn = sound_horn()
    if skip:
        return trap
    what_happens(trap, horn) 

    player_input = input('Press Enter to continue training and "no" to stop training: ')
    player_input_lw = player_input.lower()
    while player_input_lw.strip() != 'no' and not player_input.startswith('\x1b'):
        if intro_to_camp():
            return trap
        skip, trap = choose_trap()
        if skip:
            return trap
        skip, horn = sound_horn()
        if skip:
            return trap
        what_happens(trap, horn)
        player_input = input('Press Enter to continue training and "no" to stop training: ')
        player_input_lw = player_input.lower()

    return trap



def main():
    repeat = repeat_training()
    
    '''
    Implement your code here.
    '''



# def change_cheese(hunter_name: str, trap: str, cheese: list, e_flag: bool = False) -> tuple:
#     '''
#     Handles the inputs and ouputs of the change cheese feature.
#     Parameters:
#         hunter_name: str,        the name of the player.
#         trap:        str,        the trap name.
#         cheese:      list,       all the cheese and its quantities the player 
#                                  currently possesses.
#         e_flag:      bool,       if the trap is enchanted, this will be True. 
#                                  default value is False.
#     Returns:
#         trap_status: bool,       True if armed and False otherwise.
#         trap_cheese: str | None, the type of cheese in the trap. if player 
#                                  exits the function without without arming 
#                                  trap succesfully, this value is None.
#     '''
#     pass

if __name__ == '__main__':
    main()

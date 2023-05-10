'''
This file should borrow code from your Assignment 1.
However, it will require some modifications for this assignment.

Author:
SID:
Unikey:
'''

'''
Keep this line!
'''
import random

'''
We recommend you import your 'name', 'train' and 'shop' modules to complete this 
question. It will save trouble in needing to copy and paste code from previous 
questions. However if you wish not to, you are free to remove the imports below.
Feel free to import other modules that you have written.
'''
import name
import train
import shop

# you can make more functions or global read-only variables here if you please!

def game_title():
    '''
    prints game title
    '''

    #Title
    print('Mousehunt''\n')
    #Logo
    print("       ____()()","      /      @@","`~~~~~\_;m__m._>o"'\n', sep = '\n')
    #Author
    # print("An INFO1110/COMP9001 Student")
    #Credits
    print("Inspired by Mousehunt© Hitgrab","Programmer - An INFO1110/COMP9001 Student","Mice art - Joan Stark", sep = '\n')
    print('')



def hunter_name_input():

    '''
    return hunter_name
    '''

    hunter_name = name.player_name()

    if name.is_valid_name(hunter_name):
        return hunter_name
    else:
        return 'Bob'


def welcome_hunter(hunter_name) -> str:

    '''
    returns trap from training or carboard and hook trap if skipped
    '''

    print(f'Welcome to the Kingdom, Hunter {hunter_name}!')
    print("Before we begin, let's train you up!")
    #player_input -----> '' = start training / 'skip' = start game
    player_input = input('Press "Enter" to start training or "skip" to Start Game: ')

    while player_input != '' and player_input != 'skip' and not player_input.startswith('\x1b'):
        print('Sorry did not understand!\n')
        player_input = input('Press "Enter" to start training or "skip" to Start Game: ')

    if player_input == '':
        print('')
        trap = train.repeat_training()
        print('')
        return trap
    elif player_input == 'skip' or player_input.startswith('\x1b'):
        print('')
        trap = 'Cardboard and Hook Trap'
        return trap

        

def get_game_menu(hunter_name) -> str:

    '''
    Returns a string displaying all possible actions at the game menu.
    '''

    menu = (f'What do ye want to do now, Hunter {hunter_name}?', '1. Exit game', '2. Join the Hunt', '3. The Cheese Shop', '4. Change Cheese')
    return '\n'.join(menu)



def display_inventory(trap: str, gold: int, cheese: list) -> None: #display function -----> gold, cheese, trap are parameters
    cheddar, marble, swiss = cheese
    cheddar_num = cheddar[1]
    marble_num = marble[1]
    swiss_num = swiss[1]
    print (f'Gold - {gold}')
    print (f'Cheddar - {cheddar_num}')
    print (f'Marble - {marble_num}')
    print (f'Swiss - {swiss_num}')
    print (f'Trap - {trap}')



def game_shop_function(trap, gold, cheese):

    '''
    Shop Function
    '''
    
    gold_used = 0

    print('Welcome to The Cheese Shop!', 'Cheddar - 10 gold', 'Marble - 50 gold', 'Swiss - 100 gold', sep = '\n')
    cheddar, marble, swiss = cheese
    cheddar_num = cheddar[1]
    marble_num = marble[1]
    swiss_num = swiss[1]
    while True:
        print('')
        intro = shop.shopintro()
        if intro == '1':
            gold_used, cheese_bought = shop.buy_cheese(gold)
            cheddar_num += cheese_bought[0]
            marble_num += cheese_bought[1]
            swiss_num += cheese_bought[2]
            gold -= gold_used
            cheese = ([('cheddar', cheddar_num), ('marble', marble_num), ('swiss', swiss_num)])
        elif intro == '2':
            display_inventory(trap, gold, cheese)
        elif intro == '3':
            # print('Thank you for visiting The Cheese Shop!')
            print('')
            return gold_used, cheese
            break
        else:
            print('Invalid input, please try again.')



def change_cheese(hunter_name: str, trap: str, cheese: list, e_flag: bool = False) -> tuple:

    '''
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
                                 exits the function without without arming 
                                 trap succesfully, this value is None.
    '''
    # available_cheeses = ['cheddar', 'marble', 'swiss']
    trap_status = False
    trap_cheese = None
    cheddar, marble, swiss = cheese
    cheddar_num = cheddar[1]
    marble_num = marble[1]
    swiss_num = swiss[1]

    while True:
        print(f'Hunter {hunter_name}, you currently have:')
        print(f'Cheddar - {cheddar_num}')
        print(f'Marble - {marble_num}')
        print(f'Swiss - {swiss_num}')
        print('')
        pl_cheese_choice_input = input('Type cheese name to arm trap: ').strip().lower()

        if pl_cheese_choice_input == 'back':
            print('')
            return (trap_status, trap_cheese)

        if pl_cheese_choice_input == 'cheddar':
            if cheddar_num == 0:
                print("Out of cheese!")
            else:
                pl_confirm_change_input = input('Do you want to arm your trap with Cheddar? ').strip().lower()
                if pl_confirm_change_input == 'yes':
                    print(f'{trap} is now armed with Cheddar!')
                    print('')
                    trap_status = True
                    trap_cheese = 'cheddar'
                    break
                elif pl_confirm_change_input == 'back':
                    print('')
                    break
                else:
                    print('')

        elif pl_cheese_choice_input == 'marble':
            if marble_num == 0:
                print("Out of cheese!")
            else:
                pl_confirm_change_input = input('Do you want to arm your trap with Marble? ').strip().lower()
                if pl_confirm_change_input == 'yes':
                    print(f'{trap} is now armed with Marble!')
                    print('')
                    trap_status = True
                    trap_cheese = 'marble'
                    break
                elif pl_confirm_change_input == 'back':
                    print('')
                    break
                else:
                    print('')

        elif pl_cheese_choice_input == 'swiss':
            if swiss_num == 0:
                print("Out of cheese!")
            else:
                pl_confirm_change_input = input('Do you want to arm your trap with Swiss? ').strip().lower()
                if pl_confirm_change_input == 'yes':
                    print(f'{trap} is now armed with Swiss!')
                    print('')
                    trap_status = True
                    trap_cheese = 'swiss'
                    break
                elif pl_confirm_change_input == 'back':
                    print('')
                    break
                else:
                    print('')

        else:
            print("No such cheese!")
    # print(trap_status, trap_cheese)
    return (trap_status, trap_cheese)



def consume_cheese(to_eat: str, cheese: list) -> None:
    '''
    Handles the consumption of cheese.
    Will modify the cheese list, if required.
    Parameters:
        to_eat:    str,        the type of cheese to consume during the hunt.
        cheese:    list,       all the cheeses and quantities the player 
                               currently posseses.
    '''
    if to_eat == 'cheddar' or to_eat == 'marble' or to_eat == 'swiss':
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
    '''
    Handles the hunt mechanic.
    It includes the inputs and outputs of sounding the horn, the result of 
    the hunt, the gold and points earned, and whether users want to continue 
    after failing consecutively.
    The function will modify the cheese list, if required.
    Parameters:
        gold:        int,        the quantity of gold the player possesses.
        cheese:      list,       all the cheese and quantities the player 
                                 currently posseses.
        trap_cheese: str | None, the type of cheese that the trap is currently 
                                 armed with. if its not armed, value is None.
        points:      int,        the quantity of points that the player 
                                 currently posseses.
    Returns:
        gold:        int,        the updated quantity of gold after the hunt.   
        points:      int,        the updated quantity of points after the hunt.
    '''

    i = 0
    j = 0
    cheese_num = 0

    while i < len(cheese):
        if cheese[i][0] == trap_cheese:
            # cheese_type = cheese[i][0]
            cheese_num = cheese[i][1]
            break
        else:
            i += 1

    while True: #loop hunt
        random_value = random.random()
        print('Sound the horn to call for the mouse...')
        pl_horn_input = input('Sound the horn by typing "yes": ').strip().lower()
        print('')

        if cheese_num > 0 and pl_horn_input == 'yes':
            consume_cheese(trap_cheese, cheese)
            if random_value > 0.5: 
                j = 0
                cheese_num -= 1
                gold += 125
                points += 115
                print ('Caught a Brown mouse!')
                print (f'My gold: {gold}, My points {points}')
                print('')

            elif random_value <= 0.5:
                j += 1
                cheese_num -= 1
                print ('Nothing happens')
                print (f'My gold: {gold}, My points {points}')
                print('')

        elif cheese_num > 0 and pl_horn_input != 'yes':
            print('invalid input')
            print('')

        elif cheese_num == 0 and pl_horn_input == 'yes':
            j += 1
            print('Nothing happens. You are out of cheese!')
            print(f'My gold: {gold}, My points: {points}')
            print('')

        elif pl_horn_input == 'stop hunt':
            print('')
            return gold, points  

        if j > 0 and (j + 1) % 5 == 0:
            pl_confirm = input('Do you want to continue to hunt? ').strip().lower()
            if pl_confirm != 'yes':
                return gold, points
            else:
                j = 0


def main():

    game_title()

    hunter_name = hunter_name_input()

    trap = welcome_hunter(hunter_name)

    cheese = [('cheddar', 0), ('marble', 0), ('swiss', 0)]
    cheddar, marble, swiss = cheese
    cheddar_num = cheddar[1]
    marble_num = marble[1]
    swiss_num = swiss[1]

    #change_cheese(hunter_name, trap, cheese, e_flag)
    trap_status = False
    trap_cheese = None
    e_flag = False

    #hunt(gold, cheese, trap_cheese, points)
    gold = 125
    points = 0

    while True:
        print(get_game_menu(hunter_name))
        pl_menu_input = input('')
        if pl_menu_input == '1':
            break
        elif pl_menu_input == '2':
            # cheese = consume_cheese(to_eat, cheese)
            gold, points = hunt(gold, cheese, trap_cheese, points)
        elif pl_menu_input == '3':
            gold_used, cheese = game_shop_function(trap, gold, cheese)
            cheddar_num = cheese[0][1]
            marble_num = cheese[1][1]
            swiss_num = cheese[2][1]
            gold -= gold_used
            cheese = [('cheddar', cheddar_num), ('marble', marble_num), ('swiss', swiss_num)]       
        elif pl_menu_input == '4':
            trap_status, trap_cheese = change_cheese(hunter_name, trap, cheese, e_flag)
        else:
            print('Sorry, input is invalid')
            print('')
            # print(get_game_menu(hunter_name))
            # return main_menu(hunter_name, gold, trap, cheese, e_flag)


if __name__ == '__main__':
    main()

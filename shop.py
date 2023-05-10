'''
Write your solution to 1. Upgraded Cheese Shop here.
It should borrow code from Assignment 1.

Author:
SID:
Unikey:
'''


CHEESE_MENU = (("Cheddar", 10), ("Marble", 50), ("Swiss", 100))
# you can make more functions or global read-only variables here if you please!


def shopintro(): #introducing shop, types of cheese, prices of each cheese -----> return pl_option_input
    print('How can I help ye?', '1. Buy cheese', '2. View inventory', '3. Leave shop', sep = '\n')
    pl_option_input = input('')
    return pl_option_input


def buy_cheese(gold: int) -> tuple:
    
    '''
    returns gold_used_final, cheese
    '''

    gold_used_final = 0
    cheese_bought = (0, 0, 0)
    cheddar, marble, swiss = cheese_bought
    while True:
        gold_used = 0
        print(f'You have {gold} gold to spend.')
        pl_cheese_input = input('State [cheese quantity]: ')

        if pl_cheese_input[0].isalpha():
            pl_cheese_input = pl_cheese_input.lower()
        else:
            print('Invalid command.')

        if pl_cheese_input.startswith('cheddar '):
            number_of_cheese = pl_cheese_input.split()[1]
            if number_of_cheese != '':
                if number_of_cheese.isdigit():
                    integer_of_cheese = int(number_of_cheese)
                    if integer_of_cheese > 0:
                        if gold >= 10 * integer_of_cheese:
                            cheddar += integer_of_cheese
                            cheese_bought = (cheddar, marble, swiss)
                            gold_used += 10 * integer_of_cheese
                            gold_used_final += gold_used
                            gold -= gold_used
                            print(f'Successfully purchase {integer_of_cheese} cheddar.')
                            continue
                        else:
                            print('Insufficient gold.')
                    else:
                        print('Must purchase positive amount of cheese.')
                else:
                    print('Invalid quantity.')
            else:
                print('Missing quantity.')

        elif pl_cheese_input.startswith('marble '):
            number_of_cheese = pl_cheese_input.split(' ')[1]
            if number_of_cheese != '':
                if number_of_cheese.isdigit():
                    integer_of_cheese = int(number_of_cheese)
                    if integer_of_cheese > 0:
                        if gold >= 50 * integer_of_cheese:
                            marble += integer_of_cheese
                            cheese_bought = (cheddar, marble, swiss)
                            gold_used += 50 * integer_of_cheese
                            gold_used_final += gold_used
                            gold -= gold_used
                            print(f'Successfully purchase {integer_of_cheese} marble.')
                            continue
                        else:
                            print('Insufficient gold.')
                    else:
                        print('Must purchase positive amount of cheese.')
                else:
                    print('Invalid quantity.')
            else:
                print('Missing quantity.')

        elif pl_cheese_input.startswith('swiss '):
            number_of_cheese = pl_cheese_input.split(' ')[1]
            if number_of_cheese != '':
                if number_of_cheese.isdigit():
                    integer_of_cheese = int(number_of_cheese)
                    if integer_of_cheese > 0:
                        if gold >= 100 * integer_of_cheese:
                            swiss += integer_of_cheese
                            cheese_bought = (cheddar, marble, swiss)
                            gold_used += 100 * integer_of_cheese
                            gold_used_final += gold_used
                            gold -= gold_used
                            print(f'Successfully purchase {integer_of_cheese} swiss.')
                            continue
                        else:
                            print('Insufficient gold.')
                    else:
                        print('Must purchase positive amount of cheese.')
                else:
                    print('Invalid quantity.')
            else:
                print('Missing quantity.')

        elif pl_cheese_input == 'back':
            return (gold_used_final, cheese_bought)
        else:
            print(f"We don't sell {pl_cheese_input.split(' ')[0]}!")



def display_inventory(trap: str, gold: int, cheese: list) -> None: #display function -----> gold, cheese, trap are parameters
    # cheddar, marble, swiss = cheese[0][1], cheese[1][1], cheese[2][1]
    
    # print(cheddar)
    print (f'Gold - {gold}')
    print (f'Cheddar - {cheese[0][1]}')
    print (f'Marble - {cheese[1][1]}')
    print (f'Swiss - {cheese[2][1]}')
    print (f'Trap - {trap}')



def shop_function():
    gold = 125
    gold_used = 0
    cheese = [('cheddar', 0), ('marble', 0), ('swiss', 0)]
    trap = 'Cardboard and Hook Trap'
    print('Welcome to The Cheese Shop!', 'Cheddar - 10 gold', 'Marble - 50 gold', 'Swiss - 100 gold', sep = '\n')
    cheddar, marble, swiss = cheese
    cheddar_num = cheddar[1]
    marble_num = marble[1]
    swiss_num = swiss[1]
    while True:
        print('')
        intro = shopintro()
        if intro == '1':
            buyingcheese = buy_cheese(gold)
            gold_used = buyingcheese[0]
            cheese_bought = buyingcheese[1]
            cheddar, marble, swiss = cheese
            cheddar_num += cheese_bought[0]
            marble_num += cheese_bought[1]
            swiss_num += cheese_bought[2]
            gold -= gold_used
            cheese = ([('cheddar', cheddar_num), ('marble', marble_num), ('swiss', swiss_num)])
        elif intro == '2':
            display = display_inventory(trap, gold, cheese)
        elif intro == '3':
            # print('Thank you for visiting The Cheese Shop!')
            return gold_used, cheese
        else:
            print('Invalid input, please try again.')

def main():
    game_shop = shop_function()
    # print(game_shop)



if __name__ == "__main__":
    main()



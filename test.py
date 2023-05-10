'''
Write solutions to 4. New Mouse Release here.

Author:
SID:
Unikey:
'''


def test_buy_cheese():
    #positive
    # Test buying 1 of each cheese type
    assert buy_cheese(350) == (160, (1, 1, 1))
    # Test buying 2 cheddar
    assert buy_cheese(20) == (20, (2, 0, 0))

    #negative 
    #buying cheddar with invalid quantity
    assert buy_cheese(100) == (0, ('one', 0, 0))
    #buying cheddar and then buying cheddar with no quantity
    assert buy_cheese(300) == (100, ('', 0, 1))
    
    #edge
    # Test buying 50 marble
    assert buy_cheese(2500) == (2500, (0, 50, 0))
    # Test buying no cheese
    assert buy_cheese(0) == (0, (0, 0, 0))

def test_change_cheese():
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
    # Positive
    # Test selecting cheddar and arming trap successfully
    assert change_cheese('Player1', 'Cardboard and Hook Trap', [('Cheddar', 2), ('Marble', 1), ('Swiss', 5)], False) == (True, 'cheddar')
    # Test selecting marble and arming trap successfully 
    assert change_cheese('Player2', 'Cardboard and Hook Trap', [('Cheddar', 2), ('Marble', 0), ('Swiss', 1)], False) == (True, 'marble')
    
    # Negative
    # Test selecting invalid cheese and not arming trap
    assert change_cheese('Player3', 'Cardboard and Hook Trap', [('Cheddar', 3), ('Marble', 2), ('Swiss', 0)], False) == (False, None)
    # Test selecting cheddar but not confirming change
    assert change_cheese('Player4', 'Cardboard and Hook Trap', [('Cheddar', 0), ('Marble', 0), ('Swiss', 1)], False) == (False, None)
    
    # Edge
    # Test selecting cheddar when player has 0 cheddar
    assert change_cheese('Player5', 'Cardboard and Hook Trap', [('Cheddar', 0), ('Marble', 0), ('Swiss', 1)], False) == (False, None)
    # Test selecting marble when player has 0 marble
    assert change_cheese('Player6', 'Cardboard and Hook Trap', [('Cheddar', 1), ('Marble', 0), ('Swiss', 5)], False) == (False, None)


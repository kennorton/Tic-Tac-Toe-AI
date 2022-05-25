""" A file for most supporting functions 
    Please add tests for functions added in the testing.py file """


from numpy import array

def input():
    """ Get user input and store information,
    possibly combine with update function? 
    Args: None?
    Return: User data """
    pass

def update():
    """ Update data for game to use 
    Args: Data to update, Board(s) to update
    Return: Updated Board(s) """
    pass

def print_board(board: array):
    """ prints 2d array with space seperating columns.
    '\\n' seperateing rows, with '\\n' at end of array.
    """
    print('\n'.join([''.join([col for col in row])
        for row in board])) # Prints a 2D Array
""" A file for most supporting functions 
    Please add tests for functions added in the testing.py file """

from numpy import array



def print_board(board: array):
    print('\n'.join([''.join([col for col in row])
        for row in board])) # Prints a 2D Array

def take_move(data: array, player: int, move: int):
    """ Get user input, check if valid and update data if True
    Args: Data of board, which players move (1 == 'X', 2 == 'O'),
    Return: Updated board data """
    if data[move-1] == 0:
        data[move-1] = player
    return data

def update():
    """ Update data for game to use 
    Args: Data to update, Board(s) to update
    Return: Updated Board(s) """
    pass

def win_check():
    # Only needs to be used 5 moves in
    pass

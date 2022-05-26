""" A file for most supporting functions 
    Please add tests for functions added in the testing.py file """

from numpy import array



def print_board(board: array):
    print('\n'.join([''.join([col for col in row])
        for row in board])) # Prints a 2D Array

def take_move(data: array, type: int):
    """ Get user input, check if valid 
    Args: Data of board, which players move (1 == X, 2 == O) 
    Return: Updated board data """
    user = int(input()) -1
    if data[user] == 0:
        data[user] = type
    return data

def update():
    """ Update data for game to use 
    Args: Data to update, Board(s) to update
    Return: Updated Board(s) """
    pass

def win_check():
    pass

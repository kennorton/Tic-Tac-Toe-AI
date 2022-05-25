from numpy import array, array_equal

def make_board() -> array:
    """ Make a board formatted as a 2d array.
    TODO: Positions can be referenced through board[y][x]
    """

    board = [[' ', ' ', ' ', ' ', ' ', '|', ' ', ' ', ' ', ' ', ' ', '|', ' ', ' ', ' ', ' ', ' '],
             [' ', ' ', ' ', ' ', ' ', '|', ' ', ' ', ' ', ' ', ' ', '|', ' ', ' ', ' ', ' ', ' '],
             ['_', '_', '_', '_', '_', '|', '_', '_', '_', '_', '_', '|', '_', '_', '_', '_', '_'],
             [' ', ' ', ' ', ' ', ' ', '|', ' ', ' ', ' ', ' ', ' ', '|', ' ', ' ', ' ', ' ', ' '],
             [' ', ' ', ' ', ' ', ' ', '|', ' ', ' ', ' ', ' ', ' ', '|', ' ', ' ', ' ', ' ', ' '],
             ['_', '_', '_', '_', '_', '|', '_', '_', '_', '_', '_', '|', '_', '_', '_', '_', '_'],
             [' ', ' ', ' ', ' ', ' ', '|', ' ', ' ', ' ', ' ', ' ', '|', ' ', ' ', ' ', ' ', ' '],
             [' ', ' ', ' ', ' ', ' ', '|', ' ', ' ', ' ', ' ', ' ', '|', ' ', ' ', ' ', ' ', ' '],
             [' ', ' ', ' ', ' ', ' ', '|', ' ', ' ', ' ', ' ', ' ', '|', ' ', ' ', ' ', ' ', ' ']]
    
    return board

# Can possibly combine with update function to make one engine function?
# Maybe just use Engine function to handle input, update, and print sequence
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
        for row in board]))

def engine():
    # TODO
    pass


def main() -> None:
    board = make_board()
    print_board(board)

if __name__ == "__main__":
    main()

#testing comment

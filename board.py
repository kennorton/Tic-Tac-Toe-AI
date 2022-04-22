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

def print_board(board: array):
    """ prints 2d array with space seperating columns.
    '\\n' seperateing rows, with '\\n' at end of array.
    """
    print('\n'.join([''.join([col for col in row])
        for row in board]))

"""
    print("\n")
    print("\t     |     |     ")
    print("\t     |     |     ")
    print('\t_____|_____|_____')
    print("\t     |     |     ")
    print("\t     |     |     ")
    print('\t_____|_____|_____')
    print("\t     |     |     ")
    print("\t     |     |     ")
    print("\t     |     |     ")
    print("\n")
"""

def main() -> None:
    board = make_board()
    print_board(board)

if __name__ == "__main__":
    main()

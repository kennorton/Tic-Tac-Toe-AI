def check_winner(board,sign):
    return((board[1]== sign and board[2]==  sign and board[3]== sign )or #for row1 

            (board[4]== sign and board[5]== sign and board[6]== sign )or #for row2

            (board[7]== sign and board[8]== sign and board[9]== sign )or #for row3

            (board[1]== sign and board[4]== sign and board[7]==  sign )or#for Colm1 

            (board[2]== sign and board[5]== sign and board[8]== sign )or #for Colm 2

            (board[3]== sign and board[6]== sign and board[9]== sign )or #for colm 3

            (board[1]== sign and board[5]== sign and board[9]== sign )or #daignole 1

            (board[3]== sign and board[5]== sign and board[7]== sign )) #daignole 2

from Tic_Tac_Toe_Support import TicTacToe

TicTacToe()

"""
    The Classic Game of Tic tac toe

    Note: this game will not have an exit funtion,
          it wont need one.

    
"""


board = ["#", " ", " ", " ", " ", " ", " ", " ", " ", " "]

turn = TicTacToe.who_goes_fist()

player1, player2 = TicTacToe.X_or_O(turn)

game_on = True

while game_on == True:

    if turn == "Player1":

        display = TicTacToe.displayboard(board)

        tie = TicTacToe.tiecheck(board)

        if tie == True:

            game_on = False

            break

        check_occupance = False

        while check_occupance == False:

            index_position = TicTacToe.position_marking(board, player1)

            check_occupance = TicTacToe.position_check(board, index_position)

            print(
                "That position is already occupied, please select a different position\n"
            )

        if check_occupance == True:

            board[index_position] = player1

            TicTacToe.displayboard(board)

        if_win = TicTacToe.win_check(board, player1)

        if if_win == True:

            display = TicTacToe.displayboard(board)

            print("Congratulations Player 1 !!! You won the Game")

            game_on = False

        else:
            turn = "Player2"

    if turn == "Player2":

        display = TicTacToe.displayboard(board)

        tie = TicTacToe.tiecheck(board)

        if tie == True:

            game_on = False

            break

        check_occupance = False

        while check_occupance == False:

            index_position = TicTacToe.position_marking(board, player2)

            check_occupance = TicTacToe.position_check(board, index_position)

            print(
                "That position is already occupied, please select a different position\n"
            )

        if check_occupance == True:

            board[index_position] = player2
            TicTacToe.displayboard(board)

        if_win = TicTacToe.win_check(board, player2)

        if if_win == True:

            display = TicTacToe.displayboard(board)

            print("Congratulations Player 2 !!! You won the Game")

            game_on = False

        else:
            turn = "Player1"

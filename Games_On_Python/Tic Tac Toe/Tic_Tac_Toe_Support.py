from random import randint


class TicTacToe:
    """
    The Classic Tic tac toe

    """

    def __init__(self):  # innit function
        print("Welcome to :")
        print(
            " _________  ___  ________          _________  ________  ________          _________  ________  _______      "
        )
        print(
            "|\___   ___\\  \|\   ____\        |\___   ___\\   __  \|\   ____\        |\___   ___\\   __  \|\  ___ \     "
        )
        print(
            "\|___ \  \_\ \  \ \  \___|        \|___ \  \_\ \  \|\  \ \  \___|        \|___ \  \_\ \  \|\  \ \   __/|    "
        )
        print(
            "     \ \  \ \ \  \ \  \                \ \  \ \ \   __  \ \  \                \ \  \ \ \  \\\  \ \  \_|/__  "
        )
        print(
            "      \ \  \ \ \  \ \  \____            \ \  \ \ \  \ \  \ \  \____            \ \  \ \ \  \\\  \ \  \_|\ \ "
        )
        print(
            "       \ \__\ \ \__\ \_______\           \ \__\ \ \__\ \__\ \_______\           \ \__\ \ \_______\ \_______\\"
        )
        print(
            "        \|__|  \|__|\|_______|            \|__|  \|__|\|__|\|_______|            \|__|  \|_______|\|_______|"
        )

    def displayboard(board):  # ground work on board
        print("\n" * 100)
        print(board[7] + " |", board[8] + " |", board[9])
        print("----------")
        print(board[4] + " |", board[5] + " |", board[6])
        print("----------")
        print(board[1] + " |", board[2] + " |", board[3])

    def who_goes_fist():  # toss a coin like feature to randomly select first player

        coin_flip = randint(0, 1)

        if coin_flip == 0:
            return "Player1"

        else:
            return "Player2"

    def X_or_O(turn):  # to let player choose "X" or "O"

        if turn == "Player1":

            userin = ""

            while not (userin == "X" or userin == "O"):
                userin = input(
                    "Player 1, you are going first please choose 'X' or 'O'\n"
                ).upper()

            if userin == "X":
                return ("X", "O")

            else:
                return ("O", "X")

        else:

            if turn == "Player2":

                userin2 = ""

            while not (userin2 == "X" or userin2 == "O"):
                userin2 = input(
                    "Player 2, you are going first please choose 'X' or 'O'\n"
                ).upper()

            if userin2 == "X":
                return ("O", "X")

            else:
                return ("X", "O")

    def position_marking(board, player):  # to let the user select a position

        position = "0"

        while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:

            position = input(
                f"Player {player}, please enter your mark Potision in range of 1 to 9\n"
            )

        else:

            position = int(position)

            return position

    def win_check(board, mark):  # for checking if a player has won
        return (
            (board[7] == mark and board[8] == mark and board[9] == mark)
            or (board[4] == mark and board[5] == mark and board[6] == mark)
            or (board[1] == mark and board[2] == mark and board[3] == mark)
            or (board[1] == mark and board[5] == mark and board[9] == mark)
            or (board[1] == mark and board[4] == mark and board[7] == mark)
            or (board[8] == mark and board[5] == mark and board[2] == mark)
            or (board[3] == mark and board[6] == mark and board[9] == mark)
            or (board[7] == mark and board[5] == mark and board[3] == mark)
        )

    def position_check(board, position):  # returns boolean for availability check

        return board[position] == " "

    def tiecheck(board):  # to check wether all the places have been marked

        if " " not in board:

            print("Its a Tie!! Start again.")

            return True

        else:

            return False

if __name__ == "__main__":
    TicTacToe()
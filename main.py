import random
import keyboard

name1 = ""
name2 = ""

player1_name = str(input("please enter player 1 name: " + name1))
player2_name = str(input("please enter player 2 name: " + name2))

player1_score = 0
player2_score = 0
count = 0

game = True  # if game not end
winner = None  # who is a winner
current_player = "X"  # who's turn is it

board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]


def init_board():  # initial board
    board[0] = "-"
    board[1] = "-"
    board[2] = "-"
    board[3] = "-"
    board[4] = "-"
    board[5] = "-"
    board[6] = "-"
    board[7] = "-"
    board[8] = "-"


def display_board():  # display board
    print(board[0] + "|" + board[1] + "|" + board[2])
    print(board[3] + "|" + board[4] + "|" + board[5])
    print(board[6] + "|" + board[7] + "|" + board[8])


def play_game():  # play game
    display_board()
    global player1_score, player2_score, count, game
    stop = ""

    while count <= 10:
        # game loop
        while game:
            handle_turn(current_player)
            check_if_game_over()

            if winner == "X":
                print("********************")
                print("The winner is: " + player1_name)
                player1_score += 2

            elif winner == "O":
                player2_score += 2
                print("********************")
                print("The winner is: " + player2_name)

            elif winner is None:
                check_if_tie()

        count += 1
        print("********************")
        print("Starting a new round...\n")
        show_score()
        stop = input("Press (y) if you want to quit!\nor 'any key' to continue\n")
        if stop == "y":
            game = False
            print("Bye Bye!")
            break
        else:
            game = True
            init_board()
            display_board()
    print("Game Over!")
    game = False


def check_winner():
    global winner
    row_winner = check_row()
    col_winner = check_col()
    diagonal_winner = check_diagonal()
    if row_winner:
        winner = row_winner
    elif col_winner:
        winner = col_winner
    elif diagonal_winner:
        winner = diagonal_winner
    else:
        winner = None
    return


def check_row():
    global game
    row_1 = board[0] == board[1] == board[2] != "-"
    row_2 = board[3] == board[4] == board[5] != "-"
    row_3 = board[6] == board[7] == board[8] != "-"
    # if there is a match in one of the rows
    if row_1 or row_2 or row_3:
        game = False
    if row_1:
        return board[0]
    if row_2:
        return board[3]
    if row_3:
        return board[6]
    return


def check_col():
    global game
    col_1 = board[0] == board[3] == board[6] != "-"
    col_2 = board[1] == board[4] == board[7] != "-"
    col_3 = board[2] == board[5] == board[8] != "-"
    # if there is a match in one of the columns
    if col_1 or col_2 or col_3:
        game = False
    if col_1:
        return board[0]
    if col_2:
        return board[1]
    if col_3:
        return board[2]
    return


def check_diagonal():
    global game
    diagonal_1 = board[0] == board[4] == board[8] != "-"
    diagonal_2 = board[6] == board[4] == board[2] != "-"
    # if there is a match in one of the diagonals
    if diagonal_1 or diagonal_2:
        game = False
    if diagonal_1:
        return board[0]
    if diagonal_2:
        return board[6]
    return


def check_if_tie():
    global player1_score, player2_score, game
    if "-" not in board:
        game = False
        print("********************")
        print("Tie!")
        player1_score += 1
        player2_score += 1
    return


def show_score():
    global player1_score, player2_score
    score = input("Type 'ShowScore' in order to see score status\nor 'any key' to continue\n")
    if score == "ShowScore":
        print("Table Score:")
        print(player1_name + ":" + player2_name)
        print(str(player1_score) + " : " + str(player2_score) + "\n")
    else:
        return
    return


def flip_player():
    global current_player
    if current_player == 'X':
        print(player1_name + "'s turn.")
        current_player = 'O'
    elif current_player == 'O':
        print(player2_name + "'s turn.")
        current_player = 'X'
    return


def check_if_game_over():
    check_winner()


def handle_turn(player):
    flip_player()
    position = input("Choose a position from 1-9: ")
    # board is 0-8 so subtract 1 from position

    flag = False
    while not flag:
        while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            # only these numbers in the list are valid
            position = input("Choose a position from 1-9: ")
        position = int(position) - 1

        # if position is caught
        if board[position] == '-':
            flag = True
        else:
            print("This position already taken. please try again! ")
    board[position] = player
    display_board()


play_game()

# Computer Vs Human
boxes = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
HUMAN = 'X'
COMPUTER = '0'
first_player = HUMAN
turn = 1
winning_combos = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6],
                  [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]


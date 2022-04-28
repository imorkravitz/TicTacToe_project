import random

name1 = ""
name2 = ""
player1_name = input("please enter player 1 name: " + name1)
player2_name = input("please enter player 2 name: " + name2)

player1_score = 0
player2_score = 0
count = 0

board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]


def display_board():
    print(board[0] + "|" + board[1] + "|" + board[2])
    print(board[3] + "|" + board[4] + "|" + board[5])
    print(board[6] + "|" + board[7] + "|" + board[8])


# if game not end
game_time = True

# who is a winner
winner = None

# who's turn is it
current_player = 'X'


def play_game():
    global player1_score
    global player2_score
    global count
    # display initial board

    display_board()
    # game loop
    while game_time:
        handle_turn(current_player, player1_name or player2_score)

        check_if_game_over()

        flip_player()

        if winner == "X" and player1_name:
            print("The winner is: " + player1_name)
            player1_score += 1
            show_winner_table()
        elif winner == "O" and player2_name:
            player2_score += 1
            print("The winner is: " + player2_name)
            show_winner_table()
        elif winner is None:
            check_if_tie()
            show_winner_table()


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
    global game_time
    row_1 = board[0] == board[1] == board[2] != "-"
    row_2 = board[3] == board[4] == board[5] != "-"
    row_3 = board[6] == board[7] == board[8] != "-"
    # if there is a match in one of the rows
    if row_1 or row_2 or row_3:
        game_time = False
    if row_1:
        return board[0]
    if row_2:
        return board[3]
    if row_3:
        return board[6]
    return


def check_col():
    global game_time
    col_1 = board[0] == board[3] == board[6] != "-"
    col_2 = board[1] == board[4] == board[7] != "-"
    col_3 = board[2] == board[5] == board[8] != "-"
    # if there is a match in one of the columns
    if col_1 or col_2 or col_3:
        game_time = False
    if col_1:
        return board[0]
    if col_2:
        return board[1]
    if col_3:
        return board[2]
    return


def check_diagonal():
    global game_time
    diagonal_1 = board[0] == board[4] == board[8] != "-"
    diagonal_2 = board[6] == board[4] == board[2] != "-"
    # if there is a match in one of the diagonals
    if diagonal_1 or diagonal_2:
        game_time = False
    if diagonal_1:
        return board[0]
    if diagonal_2:
        return board[6]
    return


def check_if_tie():
    global game_time
    if "-" not in board:
        game_time = False
        print("Tie!")
    return


def show_winner_table():
    global player1_score
    global player2_score
    print(player1_name + "   " + player2_name)
    print(str(player1_score) + " : " + str(player2_score))
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
    check_if_tie()


def handle_turn(player, player_name):
    check_winner()

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

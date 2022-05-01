import random


def play_vs_computer():
    global game_time, human_score, computer_score, board
    print_board(board)
    while game_time:
        while not (is_board_full(board)):
            if not (is_winner(board, "O")):
                player_move()
                print_board(board)
            else:
                print("Human Lose!")
                computer_score += 2
                game_time = False
                break
            if not (is_winner(board, "X")):
                move = computer_move()
                if move is None:
                    print("-")
                else:
                    insert_letter("O", move)
                    print("Computer placed 'O' at position:", move)
                    print_board(board)
            else:
                print("You Win!")
                human_score += 2
                game_time = False
                break
        if is_board_full(board) and not is_winner(board, "O") and not is_winner(board, "X"):
            human_score += 1
            computer_score += 1
            print("Tie!")

    print("********************")
    print("Starting a new round...\n")
    show_score2()

    choice = "y"
    while choice == "y" or choice == "Y":
        board = ["-" for x in range(10)]
        print("\n")
        choice = input("if want to  play again press (y) or (n) to quit!")
        if choice == 'y' or choice == 'Y':
            game_time = True
            play_vs_computer()
        elif choice == "n" or choice == "N":
            game_time = False
            print("Game Over!")
            break
    print("Bye Bye")


# play game
def play_game():
    display_board()
    global player1_score, player2_score, count, game
    stop = ""

    # game loop
    while game:
        handle_turn(current_player)
        check_if_game_over()

        if winner == "X":
            print("********************")
            print("The winner is: " + player1_name)
            player1_score += 2

        elif winner == "O":
            print("********************")
            print("The winner is: " + player2_name)
            player2_score += 2

        elif winner is None:
            check_if_tie()

    print("********************")
    print("Starting a new round...\n")
    show_score()

    choice = "y"
    while choice == "y" or choice == "Y":
        init_board()
        print("\n")
        choice = input("if want to  play again press (y) or (n) to quit!")
        if choice == 'y' or choice == 'Y':
            game = True
            play_game()
        elif choice == "n" or choice == "N":
            game = False
            print("Game Over!")
            break
    print("Bye Bye")


# initial board
def init_board():
    board[0] = "-"
    board[1] = "-"
    board[2] = "-"
    board[3] = "-"
    board[4] = "-"
    board[5] = "-"
    board[6] = "-"
    board[7] = "-"
    board[8] = "-"


# display board player vs player
def display_board():
    print(board[0] + "|" + board[1] + "|" + board[2])
    print(board[3] + "|" + board[4] + "|" + board[5])
    print(board[6] + "|" + board[7] + "|" + board[8])


# display board player vs computer
def print_board(b):
    print(b[1] + "|" + b[2] + "|" + b[3])
    print(b[4] + "|" + b[5] + "|" + b[6])
    print(b[7] + "|" + b[8] + "|" + b[9])


# check winner func for player vs player
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


# if there is a match in one of the rows
def check_row():
    global game
    row_1 = board[0] == board[1] == board[2] != "-"
    row_2 = board[3] == board[4] == board[5] != "-"
    row_3 = board[6] == board[7] == board[8] != "-"
    if row_1 or row_2 or row_3:
        game = False
    if row_1:
        return board[0]
    if row_2:
        return board[3]
    if row_3:
        return board[6]
    return


# if there is a match in one of the columns
def check_col():
    global game
    col_1 = board[0] == board[3] == board[6] != "-"
    col_2 = board[1] == board[4] == board[7] != "-"
    col_3 = board[2] == board[5] == board[8] != "-"
    if col_1 or col_2 or col_3:
        game = False
    if col_1:
        return board[0]
    if col_2:
        return board[1]
    if col_3:
        return board[2]
    return


# if there is a match in one of the diagonals
def check_diagonal():
    global game
    diagonal_1 = board[0] == board[4] == board[8] != "-"
    diagonal_2 = board[6] == board[4] == board[2] != "-"
    if diagonal_1 or diagonal_2:
        game = False
    if diagonal_1:
        return board[0]
    if diagonal_2:
        return board[6]
    return


# tie situation
def check_if_tie():
    global player1_score, player2_score, game
    if "-" not in board:
        game = False
        print("********************")
        print("Tie!")
        player1_score += 1
        player2_score += 1
    return


# option to check table score status by typing ShowScore player vs player
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


# option to check table score status by typing ShowScore of player vs computer
def show_score2():
    global HUMAN, COMPUTER
    score = input("Type 'ShowScore' in order to see score status\nor 'any key' to continue\n")
    if score == "ShowScore":
        print("Table Score:")
        print("    " + str(human_score) + ":    " + str(computer_score))
        print(HUMAN + " : " + COMPUTER + "\n")
    else:
        return
    return


# iterate turn of player
def flip_player():
    global current_player
    if current_player == 'X':
        print(player1_name + "'s turn.")
        current_player = 'O'
    elif current_player == 'O':
        print(player2_name + "'s turn.")
        current_player = 'X'
    return


# check if someone won the game
def check_if_game_over():
    check_winner()


# this function get a position of player and fill the board as player selected
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


# computer move func
def computer_move():
    possible_move = [x for x, letter in enumerate(board) if letter == "-" and x != "X"]
    i = 0
    for let in ["O", "X"]:
        for i in possible_move:
            board_copy = board[:]
            board_copy[i] = let
            if is_winner(board, i):
                move = i
                return move
    corner = []
    edges = []

    if 5 in possible_move:
        move = 5
        return move

    if i in [4, 2, 6, 8]:
        edges.append(i)
        if len(edges) > 0:
            move = select_random(edges)
            return move
    if i in [1, 3, 7, 9]:
        corner.append(i)
        if len(corner) > 0:
            move = select_random(corner)
            return move


# check if there is a free space in the board
def free_space(pos):
    return board[pos] == "-"


# inserting letter in the board
def insert_letter(letter, pos):
    board[pos] = letter


# check if board is full
def is_board_full(b):
    if b.count('-') > 1:
        return False
    else:
        return True


# player move func of player vs computer game
def player_move():
    run = True
    while run:
        move = input("Choose a position from 1-9: ")
        try:
            move = int(move)
            if 0 < move < 10:
                if free_space(move):
                    run = False
                    insert_letter("X", move)
                else:
                    print("This position already taken. please try again!")
            else:
                print("Choose a position from 1-9: ")
        except:
            print("Enter a number")


# random func for player vs computer func
def select_random(position):
    rand = len(position)
    r = random.randrange(0, rand)
    return position[r]


# search for the winner in player vs computer game
def is_winner(b, i):
    return ((b[1] == i and b[2] == i and b[3] == i) or
            (b[4] == i and b[5] == i and b[6] == i) or
            (b[7] == i and b[8] == i and b[9] == i) or
            (b[1] == i and b[4] == i and b[7] == i) or
            (b[2] == i and b[5] == i and b[8] == i) or
            (b[3] == i and b[6] == i and b[9] == i) or
            (b[1] == i and b[5] == i and b[9] == i) or
            (b[7] == i and b[5] == i and b[3] == i))


# choose whether you prefer to play with computer or with friend
game_option = input("Choose (1) to play  >>> player Vs player\n"
                    "Choose (2) to play >>> player Vs computer\n:")

# if option 1 chosen the game will be player vs player
if int(game_option) == 1:
    name1 = ""
    name2 = ""
    player1_name = str(input("please enter player 1 name: " + name1))
    player2_name = str(input("please enter player 2 name: " + name2))
    player1_score = 0
    player2_score = 0
    game = True  # if game not end
    winner = None  # who is a winner
    current_player = "X"  # who's turn is it

    board = ["-", "-", "-",
             "-", "-", "-",
             "-", "-", "-"]
    play_game()


# else prefer to play game vs computer
elif int(game_option) == 2:
    # Computer Vs Human
    HUMAN = "Human"
    COMPUTER = " Computer"
    human_score = 0
    computer_score = 0
    # humanN = ""
    game_time = True
    # human_nam = str(input("please enter your name: " + humanN))

    board = ['-' for x in range(10)]
    play_vs_computer()

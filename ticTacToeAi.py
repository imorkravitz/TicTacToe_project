import random

board = {1: ' ', 2: ' ', 3: ' ',
         4: ' ', 5: ' ', 6: ' ',
         7: ' ', 8: ' ', 9: ' '}


#  print the board
def print_b(board):
    print('\n')
    print(board[1] + '|' + board[2] + '|' + board[3])
    print('-+-+-')
    print(board[4] + '|' + board[5] + '|' + board[6])
    print('-+-+-')
    print(board[7] + '|' + board[8] + '|' + board[9])
    print('\n')


#  initial the board
def init_board():
    board[1] = ' '
    board[2] = ' '
    board[3] = ' '
    board[4] = ' '
    board[5] = ' '
    board[6] = ' '
    board[7] = ' '
    board[8] = ' '
    board[9] = ' '


#  check if there is an empty space in the board
def space_is_free(position):
    if board[position] == ' ':
        return True
    else:
        return False


#  check if there is a Tie between players
def check_for_tie():
    for i in board.keys():
        # still available space
        if board[i] == ' ':
            return False
    return True


#  check win function for player Vs player game
def check_is_win():
    if board[1] == board[2] and board[1] == board[3] and board[1] != ' ':
        return True
    elif board[4] == board[5] and board[4] == board[6] and board[4] != ' ':
        return True
    elif board[7] == board[8] and board[7] == board[9] and board[7] != ' ':
        return True
    elif board[1] == board[4] and board[1] == board[7] and board[1] != ' ':
        return True
    elif board[2] == board[5] and board[2] == board[8] and board[2] != ' ':
        return True
    elif board[3] == board[6] and board[3] == board[9] and board[3] != ' ':
        return True
    elif board[1] == board[5] and board[1] == board[9] and board[1] != ' ':
        return True
    elif board[7] == board[5] and board[7] == board[3] and board[7] != ' ':
        return True
    else:
        return False


#  check win function for player Vs computer game
def check_which_pos_won(pos):
    if board[1] == board[2] and board[1] == board[3] and board[1] == pos:
        return True
    elif board[4] == board[5] and board[4] == board[6] and board[4] == pos:
        return True
    elif board[7] == board[8] and board[7] == board[9] and board[7] == pos:
        return True
    elif board[1] == board[4] and board[1] == board[7] and board[1] == pos:
        return True
    elif board[2] == board[5] and board[2] == board[8] and board[2] == pos:
        return True
    elif board[3] == board[6] and board[3] == board[9] and board[3] == pos:
        return True
    elif board[1] == board[5] and board[1] == board[9] and board[1] == pos:
        return True
    elif board[7] == board[5] and board[7] == board[3] and board[7] == pos:
        return True
    else:
        return False


flag2 = False  # this flag is to make sure after Tie the game will continue and not break


# this function insert a letter 'X' or 'O' at the position if there is a space in the position given in the board
# every move will print the board and check who win or tie and increase the score as requested
def insert_letter(letter, position):
    global player1_score, player2_score, computer_score, flag, human_score, flag2, flag3
    if space_is_free(position):
        board[position] = letter
        print_b(board)
        if check_for_tie():
            print("***********************")
            print("\t Tie!")
            flag2 = True
            if int(game_option) == 1:  # player vs player
                player1_score += 1
                player2_score += 1
            elif int(game_option) == 2:  # player vs computer
                computer_score += 1
                human_score += 1
            flag = False
            init_board()
            flag3 = True  # for random first move of computer
            return

        elif check_is_win():
            if letter == 'X':
                if int(game_option) == 1:  # player vs player
                    print("***********************")
                    print("\t\t" + player1_name + " Win!")
                    player1_score += 2
                elif int(game_option) == 2:  # player vs computer
                    print("***********************")
                    print("\t Player Win!")
                    human_score += 2
                flag = False
                return
            else:
                if int(game_option) == 1:  # player vs player
                    print("***********************")
                    print("\t\t" + player2_name + " Win!")
                    player2_score += 2
                elif int(game_option) == 2:  # player vs computer
                    print("***********************")
                    print("\t Computer Win!")
                    computer_score += 2
                flag = False
                return
    else:
        print("this position is taken, try again!")
        position = int(input("Enter a new position (1-9): "))
        insert_letter(letter, position)
    return


# declare X players
player1 = 'X'
human = 'X'
##
# declare O players
player2 = 'O'
computer = 'O'

# counters for the score
player1_score = 0
player2_score = 0
##
human_score = 0
computer_score = 0


def player_move():
    position = int(input(player1_name + "'s turn. Enter the position for 'X' (1-9) :"))
    insert_letter(player1, position)
    return


def human_move():
    position = int(input("Human. Enter the position for 'X' (1-9) :"))
    insert_letter(human, position)
    return


def player2_move():
    position = int(input(player2_name + "'s turn. Enter the position for 'O' (1-9) :"))
    insert_letter(player2, position)
    return


flag3 = True  # this flag is to make sure the computer start first move with random library. like a Singleton we want
# to make sure it happens once in each iteration


# computer move function
def computer_move():
    best_score = -1000
    best_move = 0
    global flag3

    if flag3:
        x = random.randint(1, 9)
        insert_letter(computer, x)
        flag3 = False
    else:
        for i in board.keys():
            if board[i] == ' ':
                board[i] = computer
                score = minimax(board, 0, False)
                board[i] = ' '
                if score > best_score:
                    best_score = score
                    best_move = i
        insert_letter(computer, best_move)
    return


# minimax algorithm - a recursive algorithm. this function is a tree dealing with gains in order to maximize the
# minimum gain.
# time complexity = O(b^m), b = number of legal moves at each point and m = the maximum depth of the tree
# the depth is not necessary in tic tac toc game case because of the limited number of iterations
def minimax(board, depth, isMaximzing):
    if check_which_pos_won(computer):
        return 100
    elif check_which_pos_won(human):
        return -100
    elif check_for_tie():
        return 0

    if isMaximzing:  # higher score
        best_score = -1000
        for i in board.keys():
            if board[i] == ' ':
                board[i] = computer
                score = minimax(board, 0, False)
                board[i] = ' '
                if score > best_score:
                    best_score = score
        return best_score

    else:  # lower score
        best_score = 800
        for i in board.keys():
            if board[i] == ' ':
                board[i] = human
                score = minimax(board, 0, True)
                board[i] = ' '
                if score < best_score:
                    best_score = score
        return best_score


# option to check table score status by typing ShowScore player vs player
def show_score():
    score = input("Type 'ShowScore' in order to see score status\nor 'any key' to continue:\n")
    if score == "ShowScore":
        print("\n Table Score")
        print(" ------------")
        print("\t" + player1_name + ":" + player2_name)
        print("\t" + str(player1_score) + " : " + str(player2_score) + "\n")
    else:
        return
    return


# option to check table score status by typing ShowScore of player vs computer
def show_score2():
    score = input("Type 'ShowScore' in order to see score status\nor 'any key' to continue:\n")
    if score == "ShowScore":
        print("\n Table Score")
        print(" ------------")
        print("Human : Computer")
        print("\t" + str(human_score) + " : " + str(computer_score) + "\n")
    else:
        return
    return


print("\n** WELCOME TO TIC TAC TOE GAME! **\n")

game_option = input("Choose (1) to play  ->\tplayer VS player\n"
                    "Choose (2) to play  ->\tplayer VS computer:\t")

flag = True  # this flag is to ensure that the game not ended yet, and it allows the player continue make moves on board


# game player Vs player function
def play_game1():
    while not check_is_win():
        player_move()
        if flag is not False:
            player2_move()
    return


# game player Vs computer function
def play_game2():
    global flag2, flag
    while not check_is_win():  # while game is true == there is no winner do
        if flag2:
            flag = True
        computer_move()
        if flag is not False:
            human_move()
    return


# if choose to play game player Vs player
if int(game_option) == 1:
    # take input names of players
    name1 = ""
    name2 = ""
    player1_name = str(input("please enter player 1 name: " + name1))
    player2_name = str(input("please enter player 2 name: " + name2))
    choice = "y"
    while choice == "y" or choice == "Y":  # an option to continue play
        print_b(board)
        play_game1()
        print("***********************")
        print("\nStarting a new round...\n")
        show_score()
        choice = input("if want to  play again press (y) or (n) to quit : \t")
        if choice == 'y' or choice == 'Y':
            flag = True
            init_board()

        elif choice == "n" or choice == "N":
            game_time = False
            print("\n\tG A M E   O V E R!\n")
            exit()

# if choose to play game player Vs computer
if int(game_option) == 2:
    choice = "y"
    while choice == "y" or choice == "Y":
        play_game2()
        print("***********************")
        print("\nStarting a new round...\n")
        show_score2()
        choice = input("if want to  play again press (y) or (n) to quit: \t")  # an option to continue play
        if choice == 'y' or choice == 'Y':
            flag = True
            init_board()
            flag3 = True

        elif choice == "n" or choice == "N":
            game_time = False
            print("\n\tG A M E   O V E R!\n")
            exit()

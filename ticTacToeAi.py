board = {1: ' ', 2: ' ', 3: ' ',
         4: ' ', 5: ' ', 6: ' ',
         7: ' ', 8: ' ', 9: ' '}


def print_b(board):
    print(board[1] + '|' + board[2] + '|' + board[3])
    print('-+-+-')
    print(board[4] + '|' + board[5] + '|' + board[6])
    print('-+-+-')
    print(board[7] + '|' + board[8] + '|' + board[9])
    print('\n')


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


def space_is_free(position):
    if board[position] == ' ':
        return True
    else:
        return False


def check_for_tie():
    for i in board.keys():
        # still available space
        if board[i] == ' ':
            return False
        elif check_is_win():
            return False
    return True


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


def check_which_pos_won(pos):
    if board[1] == board[2] and board[1] == board[3] and board[1] != pos:
        return True
    elif board[4] == board[5] and board[4] == board[6] and board[4] != pos:
        return True
    elif board[7] == board[8] and board[7] == board[9] and board[7] != pos:
        return True
    elif board[1] == board[4] and board[1] == board[7] and board[1] != pos:
        return True
    elif board[2] == board[5] and board[2] == board[8] and board[2] != pos:
        return True
    elif board[3] == board[6] and board[3] == board[9] and board[3] != pos:
        return True
    elif board[1] == board[5] and board[1] == board[9] and board[1] != pos:
        return True
    elif board[7] == board[5] and board[7] == board[3] and board[7] != pos:
        return True
    else:
        return False


def insert_letter(letter, position):
    global player1_score, player2_score, computer_score, flag, human_score
    if space_is_free(position):
        board[position] = letter
        print_b(board)
        if check_for_tie():
            print("Tie!")
            if int(game_option) == 1:
                player1_score += 1
                player2_score += 1
            elif int(game_option) == 2:
                computer_score += 1
                human_score += 1
            flag = False
            init_board()

        elif check_is_win():
            if letter == 'X':
                if int(game_option) == 1:
                    print(player1_name + " Win!")
                    player1_score += 2
                elif int(game_option) == 2:
                    print("Player Win!")
                    human_score += 2
                flag = False
            else:
                if int(game_option) == 1:
                    print(player2_name + " Win!")
                    player2_score += 2
                elif int(game_option) == 2:
                    print("Computer Win!")
                    computer_score += 2
                flag = False
    else:
        print("this position is taken, try again!")
        position = int(input("Enter a new position (1-9): "))
        insert_letter(letter, position)
    return


player1 = 'X'
player2 = 'O'
computer = 'O'
human = 'X'

human_score = 0
player1_score = 0
player2_score = 0
computer_score = 0


def player_move():
    position = int(input(player1_name + "'s turn. Enter the position for 'X' :"))
    insert_letter(player1, position)
    return


def human_move():
    position = int(input("Human. Enter the position for 'X' :"))
    insert_letter(human, position)
    return


def player2_move():
    position = int(input(player2_name + "'s turn. Enter the position for 'O' :"))
    insert_letter(player2, position)
    return


def computer_move():
    best_score = -1000
    best_move = 0

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


def minimax(board, depth, isMaximzing):
    if check_which_pos_won(computer):
        return 100
    elif check_which_pos_won(player1):
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
        best_score = -1000
        for i in board.keys():
            if board[i] == ' ':
                board[i] = computer
                score = minimax(board, 0, True)
                board[i] = ' '
                if score > best_score:
                    best_score = score
        return best_score


# option to check table score status by typing ShowScore player vs player
def show_score():
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
    score = input("Type 'ShowScore' in order to see score status\nor 'any key' to continue\n")
    if score == "ShowScore":
        print("\nTable Score:")
        print("Human : Computer")
        print(str(human_score) + " : " + str(computer_score) + "\n")
    else:
        return
    return


game_option = input("Choose (1) to play  >>> player Vs player\n"
                    "Choose (2) to play >>> player Vs computer\n:")

flag = True


def play_game1():
    while not check_is_win():
        player_move()
        if flag is not False:
            player2_move()
    return


def play_game2():
    while not check_is_win():
        computer_move()
        if flag is not False:
            human_move()
    return


if int(game_option) == 1:
    name1 = ""
    name2 = ""
    player1_name = str(input("please enter player 1 name: " + name1))
    player2_name = str(input("please enter player 2 name: " + name2))

    choice = "y"
    while choice == "y" or choice == "Y":
        play_game1()
        print("********************")
        print("Starting a new round...\n")
        show_score()
        choice = input("if want to  play again press (y) or (n) to quit!")
        if choice == 'y' or choice == 'Y':
            flag = True
            init_board()
            check_is_win() == False

        elif choice == "n" or choice == "N":
            game_time = False
            print("Game Over!")
            break
    print("Bye Bye")

if int(game_option) == 2:
    choice = "y"
    while choice == "y" or choice == "Y":
        play_game2()
        print("********************")
        print("Starting a new round...\n")
        show_score2()
        choice = input("if want to  play again press (y) or (n) to quit!")
        if choice == 'y' or choice == 'Y':
            flag = True
            init_board()
            check_is_win() == False

        elif choice == "n" or choice == "N":
            game_time = False
            print("Game Over!")
            break
    print("Bye Bye")




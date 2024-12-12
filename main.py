
import random

turn = ''

def display_board(board):
    ''' displays the formatted board '''
    
    print("\n" * 100)
    if turn == 'Player One':
        print('Player One:')
    else:
        print('Player Two:')

    print("   |   |")
    print(" " + board[7] + " | " + board[8] + " | " + board[9])
    print("   |   |")
    print("----------")
    print("   |   |")
    print(" " + board[4] + " | " + board[5] + " | " + board[6])
    print("   |   |")
    print("----------")
    print("   |   |")
    print(" " + board[1] + " | " + board[2] + " | " + board[3])
    print("   |   |")

def win_check(board, mark):
    ''' returns True or False if there is a winning line '''

    return ((board[7] == board[8] == board[9] == mark) or 
            (board[4] == board[5] == board[6] == mark) or 
            (board[1] == board[2] == board[3] == mark) or
            (board[7] == board[4] == board[1] == mark) or
            (board[8] == board[5] == board[2] == mark) or
            (board[9] == board[6] == board[3] == mark) or
            (board[7] == board[5] == board[3] == mark) or
            (board[9] == board[5] == board[1] == mark))

def choose_marker():
    ''' returns a tuple with marks for players '''
    marker = ''
    while marker != 'X' and marker != 'O':
        marker = input('Player One, what do you want, X or O? (X/O): ').upper()
        if marker not in ("X" , "O"):
            print("Invalid option! ('X' or 'O')")
    if marker == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')

def set_turn():
    ''' returns a random choice between players '''
    if random.randint(0, 1) == 0:
        return 'Player One'
    else:
        return 'Player Two'   

def check_free_space(board, position):
    ''' returns True if there is a free space on board '''
    return board[position] == ' '

def check_full_board(board):
    ''' returns True or False if the board is full '''
    for i in range(1, 10):
        if check_free_space(board, i):
            return False
    return True

def choose_position(board):
    ''' choose a position for placing the marker '''
    position = ''
    while position not in range(1, 10) or not check_free_space(board, position):
        position = int(input("Choose a position on the board (1-9): "))
    return position

def place_marker(board, position, marker):
    ''' places the marker on board '''
    board[position] = marker

def tic_tac_toe():
    ''' will run the game '''
    global turn
    game_board = [' ' for _ in range(0, 10)]
    player_one_marker, player_two_marker = choose_marker()
    turn = set_turn()
    print(turn + ' will go first!')
    ready = input('Ready to play? (y/n): ')
    if ready.lower()[0] =='y':
        game_on = True
    else:
        game_on = False

    while game_on:
        if turn == 'Player One':
            display_board(game_board)
            position = choose_position(game_board)
            place_marker(game_board, position, player_one_marker)

            if win_check(game_board, player_one_marker):
                display_board(game_board)
                print("Congratulations Player One!")
                game_on = False

            elif check_full_board(game_board):
                display_board(game_board)
                print("It's a draw!")
                game_on = False

            else:
                turn = 'Player Two'

        else:
            display_board(game_board)
            position = choose_position(game_board)
            place_marker(game_board, position, player_two_marker)

            if win_check(game_board, player_two_marker):
                display_board(game_board)
                print("Congratulations Player Two!")
                game_on = False

            elif check_full_board(game_board):
                display_board(game_board)
                print("It's a draw!")
                game_on = False

            else:
                turn = 'Player One'


while input('Do you want to play a game of Tic Tac Toe? (Y/N): ').lower() == 'y':
    tic_tac_toe()
    



















































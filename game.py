import random
from IPython.display import clear_output

def player_input():
    
    '''
    OUTPUT = (Player1 marker, Player2 marker)
    '''
    
    marker = ''

    while(marker != 'X' and marker != 'O'):
        marker = input('Player1: X or O: ').upper()
    
    if(marker == 'X'):
        return ('X', 'O')
    else:
        return ('O', 'X')


def player_choose():
     
    flip = random.randint(0,1)

    if(flip == 0):
        return 'Player 1'
    else:
        return 'Player 2'


def print_board(board):
    
    print('\n')

    print('\t ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('\t---+---+---')
    print('\t ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('\t---+---+---')
    print('\t ' + board[1] + ' | ' + board[2] + ' | ' + board[3])

    print('\n')


def space_check(board, position):
    return board[position] == ' '


def position_choose(board, current_player):

    position = 0

    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board, position):
        position = int(input(f'{current_player} Enter position (1-9): '))

    return position

def set_marker(board, marker, position):
    board[position] = marker

def win_check(board, marker):
    return ((board[1] == marker and board[2] == marker and board[3] == marker) or   # across bottom
            (board[4] == marker and board[5] == marker and board[6] == marker) or   # across middle
            (board[7] == marker and board[8] == marker and board[9] == marker) or   # across top
            (board[1] == marker and board[4] == marker and board[7] == marker) or   # down left
            (board[2] == marker and board[5] == marker and board[8] == marker) or   # down middle
            (board[3] == marker and board[6] == marker and board[9] == marker) or   # down right
            (board[1] == marker and board[5] == marker and board[9] == marker) or   # diagonal
            (board[3] == marker and board[5] == marker and board[7] == marker)      # diagonal
        )

def full_board_check(board):

    for i in range(1, 10):
        if(space_check(board, i)):
            return False

    return True

def replay():
    play_again = input('Play Again (Y/N): ').lower()

    return play_again == 'y'

print('_____________')
print(' Tic Tac Toe\n')

while True:

    p1_marker, p2_marker = player_input()

    print('The game is starting ->->->->->');

    current_player = player_choose()
    print(f'{current_player} will play first\n')

    board = [' ']*10
    
    play_game = input('Ready to play? (Y or N): ')

    if(play_game.lower() == 'y'):
        game_on = True
    else:
        game_on = False

    while game_on:
        
        print_board(board)

        if(current_player == 'Player 1'):
            # Choose position to place marker
            position = position_choose(board, current_player)

            # Place marker     
            set_marker(board, p1_marker, position)

            # Check if the player has won
            if win_check(board, p1_marker):
                print_board(board)
                print('PLAYER 1 HAS WON')
                game_on = False
            # Check if board is full
            else:
                if(full_board_check(board)):
                    print_board(board)
                    print('TIE GAME')
                    game_on = False
                else:
                    current_player = 'Player 2'

        else:
            # Choose position to place marker
            position = position_choose(board, current_player)

            # Place marker     
            set_marker(board, p2_marker, position)

            # Check if the player has won
            if win_check(board, p2_marker):
                print_board(board)
                print('PLAYER 2 HAS WON')
                game_on = False
            # Check if board is full
            else:
                if(full_board_check(board)):
                    print_board(board)
                    print('TIE GAME')
                    game_on = False
                else:
                    current_player = 'Player 1'


    if not replay():
        break
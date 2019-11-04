# Create a dictionary with nine keys to represent the nine slots on a
# tic-tac-toe board.

the_board = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
            'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
            'low-L': ' ', 'low-M': ' ', 'low-R': ' '}

def print_board(board):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-----')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-----')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])

turn = 'X'
for i in range(9):
    print_board(the_board) # print the board at start of each turn
    move = input('Turn for ' + turn + '. Move on which space? ')
    the_board[move] = turn
    # switch the active player
    if turn == 'X':
        turn = 'O'
    else:
        turn = 'X'

print_board(the_board)

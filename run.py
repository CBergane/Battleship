
from random import randint

"""
Creates a board 8*8 
"""
board = []

for x in range(0, 8):
    board.append(['O']* 8)

def print_board(board):
    """
    Stack on top of each other and cleans up the board
    """
    for row in board:
        print(' '.join(row))

print_board(board)

"""
Places CPUs ship on the board
"""
def random_row(board):
    return randint(0, len(board) - 1)

def random_col(board):
    return randint(0, len(board) - 1)
        
ship_row = random_row(board)
ship_col = random_col(board)

"""
Player makes a shoot
"""
guess_row = int(input('Guess row: '))
guess_col = int(input('Guess column: '))

print(ship_row)
print(ship_col)

"""Hit or no hit"""
if guess_row == ship_row and guess_col == ship_col:
    print('Good shoot you hit my ship')
else:
    print('Bad shoot you missed my ship')
    board[guess_row][guess_col] = 'x'
    print_board(board)
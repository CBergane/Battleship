
from random import randint

SHOTS = 8
BOARD_SIZE_X = 8
BOARD_SIZE_Y = 8


"""
Creates a board 8*8 
"""
board = []

for i in range(0, 8):
    board.append(['O']* 8)

def print_board(board):
    """
    Stack on top of each other and cleans up the board
    """
    for i in board:
        print (' '.join(i))
        
def player_guess():
    """Reads a valid guess from the player"""
    
    while True:
        # read the guess of the rows and columns
        guess_rwo = read_int("Guess rwo: ")
        guess_col = read_int("Guess column: ")

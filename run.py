"""
Creates a board 8*8 
"""
board = []

for i in range(0, 8):
    board.append(['O']* 8)

def print_board(board):
    for i in board:
        print(i)
        
        
print_board(board)
    
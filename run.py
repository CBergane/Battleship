from random import randint

"""
Defines the boards
"""

#Board for holding ship locations
CPU_BOARD = [[' '] * 8 for x in range(8)]
# Board for displaying hits and misses
PLAYER_BOARD = [[' '] * 8 for x in range(8)]

  
letters_to_numbers = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5, "G": 6,"H": 7}
    
def make_board(board):
      print("  A B C D E F G H")
      print("  ---------------")
      row_num = 1
      for row in board:
          print("%d|%s|" % (row_num, "|".join(row)))
          row_num += 1
             


def make_ships(board):
    """
    CPU makes five ships
    """
    for ship in range(5):
        ship_row, ship_column = randint(0,7), randint(0,7)
        while board[ship_row][ship_column] == 'X':
            ship_row, ship_column = randint(0,7), randint(0,7)
        board[ship_row][ship_column] = 'X'
        
def locate_ship():
    """
    Makes the player set its ships
    """
    row = input('Set your ship row on the battlefield 1-8')
    while row not in '12345678':
        print('Set our ship on the board')
        row = input('Set your ship row on the battlefield 1-8')
    column = input('Set your ship row on the battlefield A-H').upper()
    while column not in 'ABCDEFGH':
        print('Set our ship on the board')
        column = input('Set your ship row on the battlefield A-H').upper()
        
    return int(row) -1, letters_to_numbers[column]
        

def ships_hit_count(board):
    count = 0
    for row in board:
        for column in row:
            if column == 'X':
                count += 1
    return count


make_ships(CPU_BOARD)
turns = 10
make_board(CPU_BOARD)
make_board(PLAYER_BOARD)
# while turns > 0:
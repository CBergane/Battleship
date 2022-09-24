import random

"""
Defines the boards
"""

# Board for holding ship locations
CPU_BOARD = [[' '] * 8 for x in range(8)]
# Board for displaying hits and misses
PLAYER_BOARD = [[' '] * 8 for x in range(8)]

# A way to make you choose letters and convert them to numbers
letters_to_numbers = {"A": 0, "B": 1, "C": 2, "D": 3,
                      "E": 4, "F": 5, "G": 6, "H": 7}


def make_board(board):
        """
        Create a board
        """
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
        ship_row, ship_column = random.randint(0, 7), random.randint(0, 7)
        while board[ship_row][ship_column] == 'X':
            ship_row, ship_column = random.randint(0, 7), random.randint(0, 7)
        board[ship_row][ship_column] = 'X'


def locate_ship():
    """
    Makes the player make there shots
    """
    row = input('Place coordinates row on the board 1-8: ')
    while row not in '12345678':
        print('Coordinates is out of range')
        row = input('Place coordinates row on the board 1-8: ')
    column = input('Place coordinates row on the board A-H: ').upper()
    while column not in 'ABCDEFGH':
        print('Coordinates is out of range')
        column = input('Place coordinates row on the board A-H: ').upper()

    return int(row)-1, letters_to_numbers[column]


def ships_hit_count(board):
    count = 0
    for row in board:
        for column in row:
            if column == 'X':
                count += 1
    return count


if __name__ == '__main__':
    make_ships(CPU_BOARD)
    print('Battleship...')
    print('Welcome to the battlefield!')
    turns = 15
    while turns > 0:
        make_board(PLAYER_BOARD)
        row, column = locate_ship()
        if PLAYER_BOARD[row][column] == '-':
            print('You have already guessed there...')
        elif CPU_BOARD[row][column] == 'X':
            print('It is a hit!')
            PLAYER_BOARD[row][column] = 'X'
            turns -= 1
        else:
            print('You missed!')
            PLAYER_BOARD[row][column] = '-'
            turns -= 1
        if ships_hit_count(PLAYER_BOARD) == 5:
            print(' Victory! All ships have been hit!\n')
            break
        print('You have ' + str(turns) + 'turns remaining')
        if turns == 0:
            print('Game over!')
            break
        

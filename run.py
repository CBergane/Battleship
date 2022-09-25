import random

"""
Defines the boards
"""


# Board for holding ship locations
CPU_BOARD = [[" "] * 8 for x in range(8)]
# Board for displaying hits and misses
PLAYER_BOARD = [[" "] * 8 for x in range(8)]

# A way to make you choose letters and convert them to numbers
letters_to_numbers = {"A": 0, "B": 1, "C": 2, "D": 3,
                      "E": 4, "F": 5, "G": 6, "H": 7}

class BattleField():
    def __init__(self, board):
        self.board = board
        
        
    def make_board(self):
            """
            Create a board
            """
            board = []
            for x in range(8):
                board.append(["[ ]"] * 8)

            def print_board(board):
                print("  ", " | ".join("12345678"))
                for letter, row in zip("ABCDEFGH", board):
                    print(letter, "|".join(row))
            print_board(board)


class main():
    def __init__(self, board):
        self.board = board
        

    def make_ships(self):
        """
        CPU makes five ships
        """
        for ship in range(5):
            self.x_row, self.y_col = random.randint(0, 7), random.randint(0, 7)
            while self.board[self.x_row][self.y_col] == "X":
                self.x_row, self.y_col = random.randint(0, 7), random.randint(0, 7)
            self.board[self.x_row][self.y_col] = "X"
        return self.board
            # ship_row, ship_column = random.randint(0, 7), random.randint(0, 7)
            # while board[ship_row][ship_column] == "X":
            #     ship_row, ship_column = random.randint(0, 7), random.randint(0, 7)
            # board[ship_row][ship_column] = "X"
            

    def locate_ship(self):
        """
        Makes the player make a shots
        """
        try:
            x_row = input("Mark the row you are aiming for, A-H: ")
            while x_row not in "ABCDEFGH":
                print("Out of range, please try again")
                x_row = input("Mark the row you are aiming for, A-H: ")
            
            y_col = input("Mark the column you are aiming for, 1-8: ")
            while y_col not in "12345678":
                print("Out of range, please try again")
                y_col = input("Mark the column you are aiming for, 1-8: ")
        except ValueError and KeyError:
            print('Not a valid cordinate')
            return self.locate_ship
        # column = input("Place coordinates column on the board 1-8: ")
        # while column not in "12345678":
        #     print("Coordinates is out of range")
        #     column = input("Place coordinates column on the board 1-8: ")
        # row = input("Place coordinates row on the board A-H: ").upper()
        # while row not in "ABCDEFGH":
        #     print("Coordinates is out of range")
        #     row = input("Place coordinates row on the board A-H: ").upper()

        # return int(column)-1, letters_to_numbers[row]


    def ships_hit_count(self):
        count = 0
        for column in self.board:
            for row in column:
                if row == "X":
                    count += 1
        return count

    
def Game():
    main(CPU_BOARD)
    print(CPU_BOARD)
    print("Battleship...")
    print("Welcome to the battlefield!")
    turns = 15
    while turns > 0:
        BattleField(PLAYER_BOARD)
        row, column = locate_ship()
        if PLAYER_BOARD[row][column] == "-":
            print("You have already guessed there...")
        elif CPU_BOARD[row][column] == "X":
            print("It is a hit!")
            PLAYER_BOARD[row][column] = "X"
            turns -= 1
        else:
            print("You missed!")
            PLAYER_BOARD[row][column] = "-"
            turns -= 1
        if ships_hit_count(PLAYER_BOARD) == 5:
            print(" Victory! All ships have been hit!\n")
            break
        print("You have " + str(turns) + "turns remaining")
        if turns == 0:
            print("Game over!")
            break
    

if __name__ == "__main__":
    Game()

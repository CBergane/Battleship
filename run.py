import random
import time

class BattleField():
    """
    Defines the BattleField
    """
    def __init__(self, board):
        self.board = board
    
    # A way to make you choose letters and convert them to numbers
    def letters(self):
        letters_to_numbers = {"A": 0, "B": 1, "C": 2, "D": 3,
                              "E": 4, "F": 5, "G": 6, "H": 7}
        return letters_to_numbers
    
    def make_board(self):
        """
        Create a board
        """
        print("  A B C D E F G H")
        print("  +-+-+-+-+-+-+-+")
        row_number = 1
        for row in self.board:
            print("%d|%s|" % (row_number, "|".join(row)))
            row_number += 1



class main():
    def __init__(self, board, y_col, x_row):
        self.board = board
        self.y_col = y_col
        self.x_row = x_row
        

    def make_ships(self):
        """
        CPU makes five ships, and makes sure not to put it in the same location.
        """
        for i in range(5):
            self.x_row, self.y_col = random.randint(0, 7), random.randint(0, 7)
            while self.board[self.x_row][self.y_col] == "X":
                self.x_row, self.y_col = random.randint(0, 7), random.randint(0, 7)
            self.board[self.x_row][self.y_col] = "X"
        return self.board
            

    def locate_ship(self):
        """
        Makes the player make a shots, need to ba a valid input to continue.
        """
        while True:
            try:
                x_row = input("Mark the row you are aiming for, 1-8: ")
                while x_row not in '12345678':
                    print("Out of range, please try again")
                    x_row = input("Mark the row you are aiming for, 1-8: ")
                
                y_col = input("Mark the column you are aiming for, A-H: ").upper()
                while y_col not in "ABCDEFGH":
                    print("Out of range, please try again")
                    y_col = input("Mark the column you are aiming for, A_H: ").upper()
                return int(x_row) - 1, BattleField.letters(self)[y_col]
            except ValueError:
                print('Not a valid coordinates')


    def ships_hit_count(self):
        count = 0
        for column in self.board:
            for row in column:
                if row == "X":
                    count += 1
        return count

    
def Game():
    cpu_board =  BattleField([[" "] * 8 for x in range(8)])
    player_board = BattleField([[" "] * 8 for x in range(8)])
    main.make_ships(cpu_board)
    print("Battleship...")
    print("Welcome to the battlefield!")
    turns = 15
    while turns > 0:
        BattleField.make_board(cpu_board)
        BattleField.make_board(player_board)
        # Get users coordinates
        user_x_row, user_y_col = main.locate_ship(object)
        # Make sure no double shots
        while player_board.board[user_x_row][user_y_col] == "-" or player_board.board[user_x_row][user_y_col] == "X":
            print("Target already marked")
            user_x_row, user_y_col = main.locate_ship(object)
        # Check if is a hit
        if cpu_board.board[user_x_row][user_y_col] == "X":
            print("You sunk a ship!")
            player_board.board[user_x_row][user_y_col] = "X"
        else:
            print("You missed! Try again!")
            player_board.board[user_x_row][user_y_col] = "-"
        # Check if the player wins or loses
        if main.ships_hit_count(player_board) == 5:
            print("You won!")
            restart()
        else:
            turns -= 1
            print(f"You have {turns} remaining to win")
            if turns == 0:
                print("You have lost!")
                BattleField.make_board(player_board)
                time.sleep(2)
                restart()

def restart():
    player_choice = input("Would you like to try again? Type 'Yes' or 'No' \n\n")
    
    if player_choice.lower == "No":
        return False

    elif player_choice.lower == "Yes":
        return True
    

if __name__ == "__main__":
    Game()

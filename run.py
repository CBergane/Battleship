"""
Import library functions
"""
import random
import time
import sys

SHOTS = 0
LETTER_NUM = {"A": 0, "B": 1, "C": 2, "D": 3,
              "E": 4, "F": 5, "G": 6}

def welcome():
    """
    Welcomes the player to the game, gives choice of rules or just play the game.
    """
    print("Welcome to Battleships!")
    time.sleep(1.5)
    print("Do you want to play the game or have a look at the rules?")
    print("Type 'G' for game and 'R' for rules.")
    player_choice = input(" \n").upper()
    while player_choice != "G" and player_choice != "R":
        print("Type 'G' for game and 'R' for rules.")
        player_choice = input(" \n").upper()
    if player_choice == 'G':
        difficulty_level()
    elif player_choice == 'R':
        rules()


def rules():
    """
    Explanation of the rules.
    """
    print("Your goals are to sink five of the games ships")
    time.sleep(2)
    print("The game will randomly generate eight ships")
    time.sleep(2)
    print("You have a number of shots at your disposal.")
    time.sleep(2)
    print("Easy: 30 shots, Medium: 20 shots, Hard: 10 shots.")
    time.sleep(2)
    print("Sink five ships before you run out of shots.")
    time.sleep(2)
    print("Are you ready to begin? Y/N")
    player_choice = input(" \n").upper()
    while player_choice != "Y" and player_choice != "N":
        print("Are you ready to begin? Y/N")
        player_choice = input(" \n").upper()
    if player_choice == "Y":
        difficulty_level()
    elif player_choice == "N":
        welcome()

def difficulty_level():
    """
    Makes the player chose between different difficulty levels
    """
    global SHOTS
    difficulty = input("Choose your difficulty level: easy, medium, hard\n")
    while difficulty not in "easy" "medium" "hard":
        difficulty = input("Choose your difficulty level: easy, medium, hard\n")
    if difficulty == "easy":
        SHOTS = 30
    if difficulty == "medium":
        SHOTS = 20
    if difficulty == "hard":
        SHOTS = 10
    game()


class BattleField():
    """
    Defines the BattleField
    """
    def __init__(self, board):
        self.board = board


    def make_board(self):
        """
        Create a board
        """
        print("  A  B  C  D  E  F  G ")
        row_number = 1
        for row in self.board:
            print(str(row_number)+"["+"][".join(row)+"]")
            row_number += 1



class Main():
    """
    Main function to make CPU place ships
    """
    def __init__(self, board, y_col, x_row):
        self.board = board
        self.y_col = y_col
        self.x_row = x_row


    def make_ships(self):
        """
        CPU makes five ships, and makes sure not to put it in the same location.
        """
        for _ in range(7):
            self.x_row, self.y_col = random.randint(0, 6), random.randint(0, 6)
            while self.board[self.x_row][self.y_col] == "X":
                self.x_row, self.y_col = random.randint(0, 6), random.randint(0, 6)
            self.board[self.x_row][self.y_col] = "X"
        return self.board



    def locate_ship(self):
        """
        Makes the player make a shots, need to ba a valid input to continue.
        """
        while True:
            try:
                x_row = input("Mark the row you are aiming for, 1-7: \n")
                while x_row not in '1234567':
                    print("Out of range, please try again")
                    x_row = input("Mark the row you are aiming for, 1-7: \n")

                y_col = input("Mark the column you are aiming for, A-G: \n").upper()
                while y_col not in "ABCDEFGH":
                    print("Out of range, please try again")
                    y_col = input("Mark the column you are aiming for, A-G: \n").upper()
                return int(x_row) - 1, LETTER_NUM[y_col]
            except (ValueError, KeyError):
                print('Not a valid coordinates')


    def ships_hit_count(self):
        """
        Counting numbers of hits
        """
        count = 0
        for column in self.board:
            for row in column:
                if row == "X":
                    count += 1
        return count


def game():
    """
    Main game logic
    """
    while True:
        cpu_board =  BattleField([[" "] * 7 for x in range(7)])
        p_board = BattleField([[" "] * 7 for x in range(7)])
        Main.make_ships(cpu_board)
        print("Battleship...")
        print("Welcome to the battlefield!")
        print(f"You have {SHOTS} shots at your disposal")
        turns = SHOTS
        while turns > 0:
            BattleField.make_board(p_board)
            # Get users coordinates
            x_row, y_col = Main.locate_ship(object)
            # Make sure no double shots
            while p_board.board[x_row][y_col] == "-" or p_board.board[x_row][y_col] == "X":
                print("Target already marked")
                x_row, y_col = Main.locate_ship(object)
            # Check if is a hit
            if cpu_board.board[x_row][y_col] == "X":
                print("You sunk a ship!")
                p_board.board[x_row][y_col] = "X"
            else:
                print("You missed! Try again!")
                p_board.board[x_row][y_col] = "-"
            # Check if the player wins or loses
            if Main.ships_hit_count(p_board) == 5:
                print("You won!")
                print("Would you like to try again? Type 'Yes' or 'No'")
                player_choice = input(" \n")
                if player_choice == "yes":
                    break
                elif player_choice == "no":
                    exit_game()
            else:
                turns -= 1
                print(f"You have {turns} remaining!")
                if turns == 0:
                    print("You have lost!")
                    BattleField.make_board(p_board)
                    BattleField.make_board(cpu_board)
                    print("Would you like to try again? Type 'Yes' or 'No'")
                    player_choice = input(" \n").lower()
                    if player_choice == "yes":
                        break
                    elif player_choice == "no":
                        exit_game()

def exit_game():
    """
    Exit the game
    """
    time.sleep(1)
    print("Thanks for playing!")
    time.sleep(2)
    print("Exiting...")
    sys.exit(0)


if __name__ == "__main__":
    welcome()

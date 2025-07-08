import numpy as np
import random

class TTT:
    def __init__(self):
        self.board = self.board_create()

    def board_create(self): 
        board = np.full((3, 3), '-')
        return board
    
    def show_board(self):
        for row in self.board:
            print(row)
    
    def start_game(self):
        self.board = self.board_create()
        input("Flipping coin for who starts (H or T): ")
        coin = random.randint(0, 100)
        if coin < 50:
            print("Heads starts")
        else:
            print("Tails starts")
        symbol1 = input("Would you like to be X or O: ")
        if symbol1.upper() == 'X':
            symbol2 = 'O'
        else:
            symbol2 = 'X'
        self.show_board()
        count = 1
        while True:
            if self.check_win(self.board):
                print("Congratulations, you won!")
                break
            if self.is_draw():
                print("It's a draw!")
                break

            while True:
                try:
                    x, y = map(int, input("Enter row and column to play (0–2): ").split())
                    if x in range(3) and y in range(3):
                        if self.board[x, y] == '-':
                            break
                        else:
                            print("That spot is already taken.")
                    else:
                        print("Values must be between 0 and 2.")
                except ValueError:
                    print("Please enter two numbers separated by a space.")
            if count % 2 == 0:
                self.board[x, y] = symbol2
            else:
                self.board[x, y] = symbol1
            count += 1
            self.show_board()
    
    def check_win(self, board):
        for i in range(3):
            if board[i, 0] == board[i, 1] == board[i, 2] != '-':
                return True
            if board[0, i] == board[1, i] == board[2, i] != '-':
                return True
        if board[0, 0] == board[1, 1] == board[2, 2] != '-':
            return True
        if board[0, 2] == board[1, 1] == board[2, 0] != '-':
            return True
        return False
    
    def is_draw(self):
        return '-' not in self.board

    def menu(self):
        while True:
            print("\n--- Tic Tac Toe Menu ---")
            print("1. Start New Game")
            print("2. Exit")

            choice = input("Enter your choice (1-2): ")

            if choice == '1':
                self.start_game()
            elif choice == '2':
                print("Exiting...")
                break
            else:
                print("Invalid choice. Please select 1, 2, or 3.")

game = TTT()
game.menu()

import tkinter as tk
from tkinter import messagebox
import math

class TicTacToe:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Tic-Tac-Toe")
        self.current_player = 'O'
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        self.buttons = [[None for _ in range(3)] for _ in range(3)]

        for i in range(3):
            for j in range(3):
                self.buttons[i][j] = tk.Button(self.window, text='', font=('normal', 20), width=5, height=2,
                                               command=lambda row=i, col=j: self.on_click(row, col))
                self.buttons[i][j].grid(row=i, column=j)

       
        self.ai_player = 'X'

        self.start_game()

    def start_game(self):
        self.reset_game()
        if self.current_player == 'X':
            self.ai_move()

    def on_click(self, row, col):
        if self.board[row][col] == ' ' and self.current_player == 'O':
            self.board[row][col] = self.current_player
            self.buttons[row][col].config(text=self.current_player)
            if self.check_winner(self.board, self.current_player):
                messagebox.showinfo("Game Over", f"{self.current_player} wins!")
                self.start_game()
            elif self.is_board_full():
                messagebox.showinfo("Game Over", "It's a draw!")
                self.start_game()
            else:
                self.current_player = 'X' if self.current_player == 'O' else 'O'
                self.window.title(f"Tic-Tac-Toe - {self.current_player}'s turn")

            
            if self.current_player == 'X':
                self.ai_move()

    def check_winner(self, board, player):
        for i in range(3):
            if all(cell == player for cell in board[i]) or all(
                    board[j][i] == player for j in range(3)):
                return True
        if all(board[i][i] == player for i in range(3)) or all(
                board[i][2 - i] == player for i in range(3)):
            return True
        return False

    def is_board_full(self):
        return all(cell != ' ' for row in self.board for cell in row)

    def reset_game(self):
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].config(text='')
                self.board[i][j] = ' '
        self.current_player = 'O'
        self.window.title("Tic-Tac-Toe")

    def ai_move(self):
        best_move = self.minimax(self.board, self.ai_player)['move']
        self.board[best_move[0]][best_move[1]] = self.ai_player
        self.buttons[best_move[0]][best_move[1]].config(text=self.ai_player)
        if self.check_winner(self.board, self.ai_player):
            messagebox.showinfo("Game Over", "AI wins!")
            self.start_game()
        elif self.is_board_full():
            messagebox.showinfo("Game Over", "It's a draw!")
            self.start_game()
        else:
            self.current_player = 'O'
            self.window.title(f"Tic-Tac-Toe - {self.current_player}'s turn")

    def minimax(self, board, player):
        empty_cells = [(i, j) for i in range(3) for j in range(3) if board[i][j] == ' ']

        if self.check_winner(board, self.ai_player):
            return {'score': 1}

        if self.check_winner(board, 'O'):
            return {'score': -1}

        if not empty_cells:
            return {'score': 0}

        moves = []

        for cell in empty_cells:
            move = {}
            move['move'] = cell
            board[cell[0]][cell[1]] = player

            if player == self.ai_player:
                result = self.minimax(board, 'O')
                move['score'] = result['score']
            else:
                result = self.minimax(board, self.ai_player)
                move['score'] = result['score']

            board[cell[0]][cell[1]] = ' '
            moves.append(move)

        best_move = None
        if player == self.ai_player:
            best_score = -math.inf
            for move in moves:
                if move['score'] > best_score:
                    best_score = move['score']
                    best_move = move['move']
        else:
            best_score = math.inf
            for move in moves:
                if move['score'] < best_score:
                    best_score = move['score']
                    best_move = move['move']

        return {'move': best_move, 'score': best_score}

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    game = TicTacToe()
    game.run()

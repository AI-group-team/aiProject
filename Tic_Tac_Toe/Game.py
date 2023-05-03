import tkinter as tk
import random

# Create the main window
root = tk.Tk()
root.title("Tic Tac Toe")

# Create the game board
board = [" "] * 9

# Create the game board buttons
buttons = []
for i in range(9):
    button = tk.Button(root, text=" ", font=("Arial", 20), width=5, height=2, command=lambda x=i: player_move(x))
    button.grid(row=i//3, column=i%3)
    buttons.append(button)

# Create the status label
status = tk.Label(root, text="X's turn", font=("Arial", 16))
status.grid(row=3, column=0, columnspan=3)
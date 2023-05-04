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
# Create the player move function
def player_move(index):
    global board
    if board[index] == " ":
        board[index] = "X"
        buttons[index].config(text="X")
        if check_win("X"):
            status.config(text="X wins!")
            disable_buttons()
        elif check_tie():
            status.config(text="Tie game!")
            disable_buttons()
        else:
            status.config(text="O's turn")
            computer_move()

# Create the computer move function
def computer_move():
    global board
    index = random.randint(0, 8)
    while board[index] != " ":
        index = random.randint(0, 8)
    board[index] = "O"
    buttons[index].config(text="O")
    if check_win("O"):
        status.config(text="O wins!")
        disable_buttons()
    elif check_tie():
        status.config(text="Tie game!")
        disable_buttons()
    else:
        status.config(text="X's turn")
# Create the win checking function
def check_win(player):
    if board[0] == player and board[1] == player and board[2] == player:
        return True
    elif board[3] == player and board[4] == player and board[5] == player:
        return True
    elif board[6] == player and board[7] == player and board[8] == player:
        return True
    elif board[0] == player and board[3] == player and board[6] == player:
        return True
    elif board[1] == player and board[4] == player and board[7] == player:
        return True
    elif board[2] == player and board[5] == player and board[8] == player:
        return True
    elif board[0] == player and board[4] == player and board[8] == player:
        return True
    elif board[2] == player and board[4] == player and board[6] == player:
        return True
    else:
        return False
import tkinter as tk
import random

# Define the options
options = ['rock', 'paper', 'scissors']

# Define the initial scores
user_score = 0
computer_score = 0
draws = 0

# Define the function for playing the game
def play_game(user_choice):
    global user_score, computer_score, draws
    
    # Get the computer's choice
    computer_choice = random.choice(options)

    # Compare the choices and update the scores
    if user_choice == computer_choice:
        result_label.config(text="It's a draw!")
        draws += 1
    elif user_choice == 'rock' and computer_choice == 'scissors' or \
         user_choice == 'paper' and computer_choice == 'rock' or \
         user_choice == 'scissors' and computer_choice == 'paper':
        result_label.config(text="You win!")
        user_score += 1
    else:
        result_label.config(text="The computer wins!")
        computer_score += 1

    # Update the scores label
    score_label.config(text="Score: You - {} Computer - {} Draws - {}".format(user_score, computer_score, draws))

# Create the tkinter window
window = tk.Tk()
window.title("Rock Paper Scissors")

# Create the widgets
rock_button = tk.Button(window, text="Rock", command=lambda: play_game("rock"))
paper_button = tk.Button(window, text="Paper", command=lambda: play_game("paper"))
scissors_button = tk.Button(window, text="Scissors", command=lambda: play_game("scissors"))
result_label = tk.Label(window, text="")
score_label = tk.Label(window, text="Score: You - 0 Computer - 0 Draws - 0")

# Add the widgets to the window
rock_button.pack(side="left", padx=10, pady=10)
paper_button.pack(side="left", padx=10, pady=10)
scissors_button.pack(side="left", padx=10, pady=10)
result_label.pack(padx=10, pady=10)
score_label.pack(padx=10, pady=10)

# Run the tkinter event loop
window.mainloop()
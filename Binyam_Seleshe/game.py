import tkinter as tk
import random

# Define possible moves
moves = ['rock', 'paper', 'scissors']

# Define AI function
def ai_move():
    return random.choice(moves)

# Define game logic
def play_game(player_move):
    ai_choice = ai_move()
    
    # Determine winner
    if player_move == ai_choice:
        return 'tie'
    elif player_move == 'rock' and ai_choice == 'scissors':
        return 'player'
    elif player_move == 'paper' and ai_choice == 'rock':
        return 'player'
    elif player_move == 'scissors' and ai_choice == 'paper':
        return 'player'
    else:
        return 'ai'

# Define GUI
class GameGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Rock, Paper, Scissors")
        self.root.geometry("300x200")

        self.label = tk.Label(self.root, text="ወደ ጨዋታው እንኳን በደህና መጡ!! Welcome to the game!!")
        self.label.pack(pady=10)
        
        self.label = tk.Label(self.root, text="እርምጃዎን ይምረጡ (Choese your step:)")
        self.label.pack(pady=10)
        
        self.rock_button = tk.Button(self.root, text="Rock", command=lambda: self.play_game('rock'))
        self.rock_button.pack(pady=5)
        
        self.paper_button = tk.Button(self.root, text="Paper", command=lambda: self.play_game('paper'))
        self.paper_button.pack(pady=5)
        
        self.scissors_button = tk.Button(self.root, text="Scissors", command=lambda: self.play_game('scissors'))
        self.scissors_button.pack(pady=5)
        
        self.result_label = tk.Label(self.root, text="")
        self.result_label.pack(pady=10)
        
        self.play_again_button = tk.Button(self.root, text="Play again", command=self.reset)
        
        self.root.mainloop()
    
    def play_game(self, player_move):
        winner = play_game(player_move)
        
        # Display result
        if winner == 'tie':
            self.result_label.config(text="ከኮምፒዩተሩ ጋር እኩል ወጥተዋል ‼️ It's a tie!")
        else:
            self.result_label.config(text=f"{winner.capitalize()} wins! እንኳን ደስ አሎት አሸንፈዋል")
        
        # Remove buttons and show play again button
        self.rock_button.pack_forget()
        self.paper_button.pack_forget()
        self.scissors_button.pack_forget()
        self.play_again_button.pack(pady=10)
    
    def reset(self):
        # Reset GUI
        self.result_label.config(text="")
        self.play_again_button.pack_forget()
        self.rock_button.pack(pady=5)
        self.paper_button.pack(pady=5)
        self.scissors_button.pack(pady=5)

# Create GUI instance
game_gui = GameGUI()

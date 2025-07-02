import tkinter as tk
from tkinter import messagebox
import random

# Score tracking
user_points = 0
computer_points = 0

# Game options
choices = ["Rock", "Paper", "Scissors"]

# Core game logic
def player_turn(user_choice):
    global user_points, computer_points

    computer_choice = random.choice(choices)

    user_choice_label.config(text=f"Your Choice: {user_choice}")
    computer_choice_label.config(text=f"Computer's Choice: {computer_choice}")

    if user_choice == computer_choice:
        result = "It's a Draw!"
    elif (user_choice == "Rock" and computer_choice == "Scissors") or \
         (user_choice == "Paper" and computer_choice == "Rock") or \
         (user_choice == "Scissors" and computer_choice == "Paper"):
        result = "You Win this round!"
        user_points += 1
    else:
        result = "Computer Wins this round!"
        computer_points += 1

    result_label.config(text=result)
    score_label.config(text=f"Score: You {user_points} | Computer {computer_points}")

# Reset game
def reset_game():
    global user_points, computer_points
    user_points = 0
    computer_points = 0
    user_choice_label.config(text="Your Choice:")
    computer_choice_label.config(text="Computer's Choice:")
    result_label.config(text="")
    score_label.config(text="Score: You 0 | Computer 0")

# Exit confirmation
def exit_game():
    if messagebox.askyesno("Exit Confirmation", "Are you sure you want to quit the game?"):
        game_window.destroy()

# Show game rules
def show_rules():
    rules = (
        "Game Rules:\n"
        "- Rock beats Scissors\n"
        "- Scissors beats Paper\n"
        "- Paper beats Rock\n"
        "Good Luck!"
    )
    messagebox.showinfo("How to Play", rules)

# GUI Setup
game_window = tk.Tk()
game_window.title("Rock Paper Scissors - Game")
game_window.geometry("400x370")
game_window.resizable(False, False)

tk.Label(game_window, text="Pick Rock, Paper, or Scissors:", font=("Arial", 14)).pack(pady=10)

button_frame = tk.Frame(game_window)
button_frame.pack()

tk.Button(button_frame, text="Rock", width=10, command=lambda: player_turn("Rock")).grid(row=0, column=0, padx=5)
tk.Button(button_frame, text="Paper", width=10, command=lambda: player_turn("Paper")).grid(row=0, column=1, padx=5)
tk.Button(button_frame, text="Scissors", width=10, command=lambda: player_turn("Scissors")).grid(row=0, column=2, padx=5)

user_choice_label = tk.Label(game_window, text="Your Choice:", font=("Arial", 12))
user_choice_label.pack(pady=5)

computer_choice_label = tk.Label(game_window, text="Computer's Choice:", font=("Arial", 12))
computer_choice_label.pack(pady=5)

result_label = tk.Label(game_window, text="", font=("Arial", 13, "bold"))
result_label.pack(pady=10)

score_label = tk.Label(game_window, text="Score: You 0 | Computer 0", font=("Arial", 12))
score_label.pack(pady=10)

bottom_frame = tk.Frame(game_window)
bottom_frame.pack(pady=15)

tk.Button(bottom_frame, text="Reset", width=10, command=reset_game).grid(row=0, column=0, padx=5)
tk.Button(bottom_frame, text="Rules", width=10, command=show_rules).grid(row=0, column=1, padx=5)
tk.Button(bottom_frame, text="Quit", width=10, command=exit_game).grid(row=0, column=2, padx=5)

game_window.mainloop()

import tkinter as tk
import random
import mysql.connector
import firebase_admin
from firebase_admin import credentials, db
from collections import defaultdict

# Initialize Firebase
cred = credentials.Certificate("C:/Users/Emoless/Desktop/rock, paper scissors game/rps-game-806a0-firebase-adminsdk-fbsvc-6c51e630a9.json")
firebase_admin.initialize_app(cred, {
    "databaseURL": "https://rps-game-806a0-default-rtdb.firebaseio.com/"
})

def connect_mysql():
    return mysql.connector.connect(
        host="127.0.0.1",
        port= 3306,
        user="root",
        password="Tonderaik999#",
        database="game_db"
    )

# Track player choices
player_history = defaultdict(int)

def play(choice):
    options = ["Rock", "Paper", "Scissors"]
    computer_choice = ai_choice()
    
    result = determine_winner(choice, computer_choice)
    
    player_history[choice] += 1  # Track player move
    
    player_label.config(text=f"Player: {choice}")
    computer_label.config(text=f"Computer: {computer_choice}")
    result_label.config(text=result)
    
    save_to_mysql(choice, computer_choice, result)
    save_to_firebase(choice, computer_choice, result)

def ai_choice():
    if not player_history:
        return random.choice(["Rock", "Paper", "Scissors"])
    
    # Predict player's next move (choose the most common)
    predicted_move = max(player_history, key=player_history.get)
    
    # AI selects the move that beats the predicted move
    counter_moves = {"Rock": "Paper", "Paper": "Scissors", "Scissors": "Rock"}
    return counter_moves[predicted_move]

def determine_winner(player, computer):
    if player == computer:
        return "It's a Draw!"
    elif (player == "Rock" and computer == "Scissors") or \
         (player == "Paper" and computer == "Rock") or \
         (player == "Scissors" and computer == "Paper"):
        return "You Win!"
    else:
        return "You Lose!"

def save_to_mysql(player, computer, result):
    conn = connect_mysql()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO game_results (player_choice, computer_choice, result) VALUES (%s, %s, %s)", (player, computer, result))
    conn.commit()
    cursor.close()
    conn.close()

def save_to_firebase(player, computer, result):
    ref = db.reference("game_results")
    ref.push({"player_choice": player, "computer_choice": computer, "result": result})

# Create main window
root = tk.Tk()
root.title("Rock, Paper, Scissors - AI & Database Version")
root.geometry("350x300")

# Labels
player_label = tk.Label(root, text="Player: ", font=("Arial", 12))
player_label.pack()

computer_label = tk.Label(root, text="Computer: ", font=("Arial", 12))
computer_label.pack()

result_label = tk.Label(root, text="", font=("Arial", 14, "bold"))
result_label.pack()

# Buttons
tk.Button(root, text="Rock", command=lambda: play("Rock"), width=10).pack()
tk.Button(root, text="Paper", command=lambda: play("Paper"), width=10).pack()
tk.Button(root, text="Scissors", command=lambda: play("Scissors"), width=10).pack()

# Run the main loop
root.mainloop()

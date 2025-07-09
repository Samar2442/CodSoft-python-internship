import tkinter as tk
import random
from playsound import playsound
import threading

# --- Setup Window ---
root = tk.Tk()
root.title("Rock Paper Scissors")
root.geometry("400x530")
root.config(bg="#1f1f1f")
root.resizable(False, False)

# --- Game Data ---
choices = ["Rock", "Paper", "Scissors"]
emojis = {"Rock": "✊", "Paper": "✋", "Scissors": "✌️"}

user_score = 0
computer_score = 0

# --- Functions ---

def play_sound(filename):
    threading.Thread(target=playsound, args=(filename,), daemon=True).start()

def play(user_choice):
    global user_score, computer_score

    comp_choice = random.choice(choices)
    result = ""

    if user_choice == comp_choice:
        result = "It's a Tie! 🤝"
        play_sound("tie.wav")
    elif (
        (user_choice == "Rock" and comp_choice == "Scissors") or
        (user_choice == "Paper" and comp_choice == "Rock") or
        (user_choice == "Scissors" and comp_choice == "Paper")
    ):
        result = "You Win! 🏆"
        user_score += 1
        play_sound("win.wav")
    else:
        result = "You Lose! 😢"
        computer_score += 1
        play_sound("lose.wav")

    user_choice_lbl.config(text=f"You: {emojis[user_choice]} ({user_choice})")
    comp_choice_lbl.config(text=f"Computer: {emojis[comp_choice]} ({comp_choice})")
    result_lbl.config(text=result)
    score_lbl.config(text=f"Score  👤 {user_score} : {computer_score} 🤖")


def reset_game():
    global user_score, computer_score
    user_score = 0
    computer_score = 0
    user_choice_lbl.config(text="You: ❔")
    comp_choice_lbl.config(text="Computer: ❔")
    result_lbl.config(text="Let's Play!")
    score_lbl.config(text=f"Score  👤 0 : 0 🤖")

# --- UI Widgets ---

# Title
tk.Label(root, text="Rock ✊ Paper ✋ Scissors ✌️", font=("Arial", 16, "bold"),
         fg="white", bg="#1f1f1f").pack(pady=10)

# Result display
result_lbl = tk.Label(root, text="Let's Play!", font=("Arial", 18, "bold"),
                      fg="#00ffcc", bg="#1f1f1f")
result_lbl.pack(pady=10)

# Choice display
user_choice_lbl = tk.Label(root, text="You: ❔", font=("Arial", 14),
                           fg="white", bg="#1f1f1f")
user_choice_lbl.pack()

comp_choice_lbl = tk.Label(root, text="Computer: ❔", font=("Arial", 14),
                           fg="white", bg="#1f1f1f")
comp_choice_lbl.pack(pady=(0, 20))

# Score
score_lbl = tk.Label(root, text="Score  👤 0 : 0 🤖", font=("Arial", 14, "bold"),
                     fg="#ffcc00", bg="#1f1f1f")
score_lbl.pack(pady=10)

# Buttons Frame
btn_frame = tk.Frame(root, bg="#1f1f1f")
btn_frame.pack(pady=10)

# Game buttons
def make_choice_button(label, emoji, choice):
    return tk.Button(btn_frame, text=f"{emoji}\n{label}", font=("Arial", 14),
                     width=8, height=3, bg="#333", fg="white",
                     activebackground="#555", bd=0, command=lambda: play(choice))

make_choice_button("Rock", "✊", "Rock").grid(row=0, column=0, padx=10)
make_choice_button("Paper", "✋", "Paper").grid(row=0, column=1, padx=10)
make_choice_button("Scissors", "✌️", "Scissors").grid(row=0, column=2, padx=10)

# Reset Button
reset_btn = tk.Button(root, text="🔁 Restart Game", font=("Arial", 12),
                      bg="#444", fg="white", command=reset_game, bd=0,
                      activebackground="#666")
reset_btn.pack(pady=20)

# Footer
tk.Label(root, text="Enjoy the game!", font=("Arial", 10),
         fg="#888", bg="#1f1f1f").pack(side=tk.BOTTOM, pady=10)

# --- Run ---
root.mainloop()
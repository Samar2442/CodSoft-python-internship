import tkinter as tk
from tkinter import messagebox
import math

# --- SETUP WINDOW ---
root = tk.Tk()
root.title("Calculator")
root.geometry("280x550")
root.configure(bg="black")
root.resizable(False, False)

expression = ""
history = []

# --- FUNCTIONS ---
def update_display(value):
    input_text.set(value)

def press(key):
    global expression
    if key == "=":
        try:
            result = str(eval(expression))
            history.append(f"{expression} = {result}")
            update_display(result)
            expression = result
            update_history()
        except:
            update_display("Error")
            expression = ""
    elif key == "C":
        expression = ""
        update_display("0")
    elif key == "CE":
        expression = expression[:-1]
        update_display(expression or "0")
    elif key == "√":
        try:
            result = math.sqrt(eval(expression))
            history.append(f"√({expression}) = {result}")
            expression = str(result)
            update_display(expression)
            update_history()
        except:
            update_display("Error")
            expression = ""
    elif key == "x²":
        try:
            result = eval(expression) ** 2
            history.append(f"({expression})² = {result}")
            expression = str(result)
            update_display(expression)
            update_history()
        except:
            update_display("Error")
            expression = ""
    elif key == "±":
        try:
            result = -eval(expression)
            expression = str(result)
            update_display(expression)
        except:
            update_display("Error")
            expression = ""
    else:
        if input_text.get() == "0" or input_text.get() == "Hello!":
            expression = ""
        expression += str(key)
        update_display(expression)

def update_history():
    history_list.delete(0, tk.END)
    for item in reversed(history[-5:]):
        history_list.insert(tk.END, item)

def clear_history():
    history.clear()
    update_history()

# --- DISPLAY ---
input_text = tk.StringVar()
input_text.set("Hello!")

entry = tk.Entry(root, textvariable=input_text, font=("Arial", 20),
                 bd=0, bg="black", fg="white", insertbackground="white",
                 justify="right")
entry.pack(fill="x", ipadx=8, ipady=15, padx=10, pady=10)

# --- BUTTON FRAME ---
btn_frame = tk.Frame(root, bg="black")
btn_frame.pack()

buttons = [
    ["%", "CE", "C", "⌫"],
    ["⅟x", "x²", "√", "÷"],
    ["7", "8", "9", "×"],
    ["4", "5", "6", "-"],
    ["1", "2", "3", "+"],
    ["±", "0", ".", "="]
]

def make_button(text, row, col):
    eval_map = {"×": "*", "÷": "/", "⌫": "CE", "⅟x": "1/"}
    key = eval_map.get(text, text)

    is_op = text in ["+", "-", "×", "÷", "="]
    bg_color = "#ffa500" if is_op else "#4d4d4d"

    btn = tk.Button(btn_frame, text=text, command=lambda: press(key),
                    font=("Arial", 12), fg="white", bg=bg_color,
                    activebackground="#666", activeforeground="white",
                    relief="flat", width=4, height=1, bd=0)

    btn.grid(row=row, column=col, padx=4, pady=4, ipadx=8, ipady=12)

# Place all buttons
for r, row in enumerate(buttons):
    for c, val in enumerate(row):
        make_button(val, r, c)

# --- HISTORY SECTION ---
history_label_frame = tk.Frame(root, bg="black")
history_label_frame.pack(fill="x", padx=10, pady=(5, 0))

tk.Label(history_label_frame, text="History", font=("Arial", 12, "bold"),
         fg="white", bg="black").pack(side=tk.LEFT)

# 🗑️ Delete history button
del_history_btn = tk.Button(history_label_frame, text="🗑️", font=("Arial", 12),
                            bg="#222", fg="white", width=3, height=1,
                            relief="flat", command=clear_history,
                            activebackground="#444")
del_history_btn.pack(side=tk.RIGHT)

# History Listbox
history_list = tk.Listbox(root, bg="#1c1c1c", fg="white",
                          font=("Arial", 11), height=4, bd=0,
                          highlightthickness=0)
history_list.pack(fill="both", padx=10, pady=(0, 10))

# --- RUN ---
root.mainloop()

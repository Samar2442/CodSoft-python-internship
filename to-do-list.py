import tkinter as tk
from tkinter import messagebox
from datetime import datetime
from playsound import playsound

root = tk.Tk()
root.title("Todo List App")
root.geometry("420x550")
root.resizable(False, False)

# Global theme state
is_dark_theme = False

# Task list
tasks = []

# Format current date & time
def get_timestamp():
    return datetime.now().strftime("%d %b %Y, %I:%M %p")

# Add a new task
def add_task():
    title = task_entry.get().strip()
    if title:
        timestamp = get_timestamp()
        tasks.append({"title": title, "completed": False, "time": timestamp})
        task_entry.delete(0, tk.END)
        update_listbox()
        playsound("add.wav") 
        messagebox.showinfo("Task Added", f"Task '{title}' added successfully!")
    else:
        messagebox.showwarning("Input Error", "Please enter a task!")

# Mark task as completed
def mark_done():
    selected = listbox.curselection()
    if selected:
        tasks[selected[0]]["completed"] = True
        update_listbox()
        playsound("done.wav")  
    else:
        messagebox.showinfo("Select Task", "Please select a task to mark as done.")

# Delete selected task
def delete_task():
    selected = listbox.curselection()
    if selected:
        tasks.pop(selected[0])
        update_listbox()
    else:
        messagebox.showinfo("Select Task", "Please select a task to delete.")

# View stats
def view_stats():
    total = len(tasks)
    completed = sum(1 for t in tasks if t["completed"])
    pending = total - completed
    messagebox.showinfo("Task Stats", f"📋 Total: {total}\n✅ Completed: {completed}\n❌ Pending: {pending}")

# Toggle theme
def toggle_theme():
    global is_dark_theme
    is_dark_theme = not is_dark_theme

    # Light Theme
    if not is_dark_theme:
        root.config(bg="white")
        listbox.config(bg="white", fg="black", selectbackground="#cccccc")
        task_entry.config(bg="white", fg="black", insertbackground="black")
        theme_btn.config(text="🌙 Dark Theme", bg="#f0f0f0", fg="black")
    else:
        # Dark Theme
        root.config(bg="#2e2e2e")
        listbox.config(bg="#3c3c3c", fg="white", selectbackground="#666666")
        task_entry.config(bg="#3c3c3c", fg="white", insertbackground="white")
        theme_btn.config(text="🌞 Light Theme", bg="#444444", fg="white")

    # Update background of buttons
    for widget in root.winfo_children():
        if isinstance(widget, tk.Button) and widget != theme_btn:
            widget.config(bg=("#1F2937" if not is_dark_theme else "#555"), fg=("white" if is_dark_theme else "white"))
    update_listbox()

# Update the listbox with tasks
def update_listbox():
    listbox.delete(0, tk.END)
    for i, task in enumerate(tasks, 1):
        symbol = "✅" if task["completed"] else "❌"
        display = f"{i}. {symbol} {task['title']} ({task['time']})"
        listbox.insert(tk.END, display)

        # Styling with color-coded backgrounds
        if task["completed"]:
            listbox.itemconfig(tk.END, {'bg': '#d4edda' if not is_dark_theme else '#355e3b', 'fg': '#155724' if not is_dark_theme else '#aaffaa'})
        else:
            listbox.itemconfig(tk.END, {'bg': '#fff3cd' if not is_dark_theme else '#664d00', 'fg': '#856404' if not is_dark_theme else '#ffd966'})

# Task entry
task_entry = tk.Entry(root, width=45, font=("Arial", 14))
task_entry.pack(pady=10)

# Add task button
add_btn = tk.Button(root, text="➕ Add Task", bg="#1F2937", fg="white", font=("Arial", 12), width=12, command=add_task)
add_btn.pack()

# Listbox
listbox = tk.Listbox(root, width=65, height=18, font=("Arial", 11), selectbackground="#8fa8f3", activestyle="none")
listbox.pack(pady=15)

# Scrollbar
scrollbar = tk.Scrollbar(root)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

# Button frame
btn_frame = tk.Frame(root)
btn_frame.pack(pady=10)

# Buttons
done_btn = tk.Button(btn_frame, text="✅ Done", bg="green", fg="white", width=14, command=mark_done)
done_btn.grid(row=0, column=0, padx=5)

stats_btn = tk.Button(btn_frame, text="📊 View Stats", bg="blue", fg="white", width=14, command=view_stats)
stats_btn.grid(row=0, column=1, padx=5)

del_btn = tk.Button(btn_frame, text="🗑️ Delete", bg="red", fg="white", width=14, command=delete_task)
del_btn.grid(row=0, column=2, padx=5)

# Theme toggle button
theme_btn = tk.Button(root, text="🌙 Dark Theme", bg="#f0f0f0", fg="black", font=("Arial", 11), width=20, command=toggle_theme)
theme_btn.pack(pady=8)

# Start app
toggle_theme()  # Start in dark mode if you prefer, comment out to start in light
toggle_theme()  # Call again to return to default (light)
root.mainloop()

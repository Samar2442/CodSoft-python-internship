import json
import os

# File to store tasks
TASK_FILE = "tasks.json"

# Load tasks from file
def load_tasks():
    if os.path.exists(TASK_FILE):
        with open(TASK_FILE, "r") as f:
            return json.load(f)
    return []

# Save tasks to file
def save_tasks(tasks):
    with open(TASK_FILE, "w") as f:
        json.dump(tasks, f, indent=4)

# Show menu
def show_menu():
    print("\n--- To-Do List ---")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Mark Task as Completed")
    print("4. Delete Task")
    print("5. Exit")

# Display all tasks
def view_tasks(tasks):
    if not tasks:
        print("No tasks found.")
    else:
        for i, task in enumerate(tasks, 1):
            status = "✅" if task['completed'] else "❌"
            print(f"{i}. [{status}] {task['title']}")

# Add a new task
def add_task(tasks):
    title = input("Enter task: ")
    tasks.append({"title": title, "completed": False})
    print("Task added.")

# Mark a task as complete
def mark_task_complete(tasks):
    view_tasks(tasks)
    index = int(input("Enter task number to mark complete: ")) - 1
    if 0 <= index < len(tasks):
        tasks[index]['completed'] = True
        print("Task marked as completed.")
    else:
        print("Invalid task number.")

# Delete a task
def delete_task(tasks):
    view_tasks(tasks)
    index = int(input("Enter task number to delete: ")) - 1
    if 0 <= index < len(tasks):
        deleted = tasks.pop(index)
        print(f"Deleted task: {deleted['title']}")
    else:
        print("Invalid task number.")

# Main function
def main():
    tasks = load_tasks()
    while True:
        show_menu()
        choice = input("Choose an option: ")

        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            mark_task_complete(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            save_tasks(tasks)
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the program
if __name__ == "__main__":
    main()

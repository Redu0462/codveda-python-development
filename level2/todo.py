import json

def load_tasks(filename="tasks.json"):
    try:
        with open(filename, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_tasks(tasks, filename="tasks.json"):
    with open(filename, "w") as file:
        json.dump(tasks, file, indent=4)

def add_task(tasks, description):
    task = {
        "task_id": len(tasks) + 1,
        "description": description,
        "done": False
    }
    tasks.append(task)
    print(f"Added: {description}")

def view_tasks(tasks):
    if not tasks:
        print("No tasks yet.")
        return
    for task in tasks:
        status = "✓" if task["done"] else " "
        print(f"[{status}] {task['task_id']}. {task['description']}")

def mark_done(tasks, task_id):
    for task in tasks:
        if task["task_id"] == task_id:
            task["done"] = True
            print(f"Marked task {task_id} as done.")
            return
    print("Task not found.")

def delete_task(tasks, task_id):
    for task in tasks:
        if task["task_id"] == task_id:
            tasks.remove(task)
            print(f"Deleted task {task_id}.")
            return
    print("Task not found.")

tasks = load_tasks()

while True:
    print("\n--- To-Do List ---")
    print("1. Add task")
    print("2. View tasks")
    print("3. Mark task as done")
    print("4. Delete task")
    print("5. Quit")
    choice = input("Choose an option: ").strip()

    if choice == "1":
        description = input("Task description: ").strip()
        add_task(tasks, description)
    elif choice == "2":
        view_tasks(tasks)
    elif choice == "3":
        task_id = int(input("Task ID to mark done: "))
        mark_done(tasks, task_id)
    elif choice == "4":
        task_id = int(input("Task ID to delete: "))
        delete_task(tasks, task_id)
    elif choice == "5":
        save_tasks(tasks)
        print("Saved. Goodbye!")
        break
    else:
        print("Invalid option.")
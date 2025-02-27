tasks = []

def display_menu():
    print("\nTo-Do List Application")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Complete")
    print("4. Delete Task")
    print("5. Exit")

def add_task():
    task = input("Enter the task: ")
    tasks.append({"task": task, "completed": False})
    print(f"Task '{task}' added successfully!")

def view_tasks():
    if not tasks:
        print("No tasks in the list.")
        return
    for idx, task in enumerate(tasks, start=1):
        status = "Done" if task['completed'] else "Pending"
        print(f"{idx}. {task['task']} [{status}]")

def mark_complete():
    view_tasks()
    task_num = int(input("Enter task number to mark as complete: "))
    if 0 < task_num <= len(tasks):
        tasks[task_num - 1]['completed'] = True
        print("Task marked as complete!")
    else:
        print("Invalid task number.")

def delete_task():
    view_tasks()
    task_num = int(input("Enter task number to delete: "))
    if 0 < task_num <= len(tasks):
        removed = tasks.pop(task_num - 1)
        print(f"Task '{removed['task']}' deleted.")
    else:
        print("Invalid task number.")

while True:
    display_menu()
    choice = input("Choose an option (1-5): ")

    if choice == '1':
        add_task()
    elif choice == '2':
        view_tasks()
    elif choice == '3':
        mark_complete()
    elif choice == '4':
        delete_task()
    elif choice == '5':
        print("Exiting To-Do List App. Goodbye!")
        break
    else:
        print("Invalid choice. Please choose a valid option.")

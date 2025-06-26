tasks = []

def add_task():
    task = input("Enter a new task: ")
    tasks.append(task)
    print("Task added!\n")

def show_tasks():
    if not tasks:
        print("The task list is empty.\n")
    else:
        print("Your tasks:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")
        print()

def remove_task():
    if not tasks:
        print("The task list is empty.\n")
        return

    show_tasks()
    try:
        index = int(input("Enter the number of the task to remove: "))
        if 1 <= index <= len(tasks):
            removed = tasks.pop(index - 1)
            print(f"Task \"{removed}\" removed!\n")
        else:
            print("Invalid task number.\n")
    except ValueError:
        print("Please enter a valid number.\n")

def show_menu():
    print("Menu:")
    print("1. Add a task")
    print("2. Show all tasks")
    print("3. Remove a task")
    print("4. Exit\n")

while True:
    show_menu()
    choice = input("Choose an option (1–4): ")
    print()

    if choice == "1":
        add_task()
    elif choice == "2":
        show_tasks()
    elif choice == "3":
        remove_task()
    elif choice == "4":
        print("Goodbye! Have a great day ☀️")
        break
    else:
        print("Invalid choice. Please try again.\n")

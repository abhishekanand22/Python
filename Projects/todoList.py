tasks = []

def show_tasks():
    if not tasks:
        print("No tasks in the to-do list.")
    else:
        print("To-Do List:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

def add_task(task):
    tasks.append(task)
    print(f"Task '{task}' added to the to-do list.")

def main():
    while True:
        print("\n1. Show Tasks")
        print("2. Add Task")
        print("3. Exit")

        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':
            show_tasks()
        elif choice == '2':
            task = input("Enter the task: ")
            add_task(task)
        elif choice == '3':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()

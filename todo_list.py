# Simple To-Do List Program

# This is a list to store the tasks
tasks = []

# Function to display tasks
def show_tasks():
    if len(tasks) == 0:
        print("\nYou have no tasks to display.")
    else:
        print("\nYour To-Do List:")
        for index, task in enumerate(tasks, 1):
            print(f"{index}. {task}")

# Function to add a task
def add_task():
    task = input("Enter a task to add: ")
    tasks.append(task)
    print(f'"{task}" has been added to your list.')

# Function to remove a task
def remove_task():
    show_tasks()
    if len(tasks) == 0:
        return
    try:
        task_number = int(input("\nEnter the task number to remove: "))
        if 1 <= task_number <= len(tasks):
            removed = tasks.pop(task_number - 1)
            print(f'"{removed}" has been removed from your list.')
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

# Main program loop
def main():
    while True:
        print("\n1. Show tasks")
        print("2. Add task")
        print("3. Remove task")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            show_tasks()
        elif choice == "2":
            add_task()
        elif choice == "3":
            remove_task()
        elif choice == "4":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

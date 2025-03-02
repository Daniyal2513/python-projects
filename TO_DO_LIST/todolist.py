import os

file_name = "TODO_list.txt"

def load_task():
    tasks = []
    if os.path.exists(file_name):
        with open(file_name,"r") as file:
            for task in file:
                task = task.strip()
                task, completed = task.split(" | ")
                tasks.append({"task": task, "completed": completed == "True"})
    return tasks

def save_task(tasks):
    with open(file_name, "w") as file:
        for task in tasks:
            file.write(f"{task['task']} | {task['completed']}\n")

def add_task(tasks,task):
    tasks.append({"task":task, "completed":False} )
    save_task(tasks)
    print("Task added successfully!")

def view_task(tasks):
    if not tasks:
        print("No task available")
    else:
        for index, item in enumerate(tasks,start=1):
            status = "✓"if item["completed"]else "✘"
            print(f"{index}.{item['task']}[{status}]")

def mark_task_completed(tasks, task_number):
    if 0 < task_number <= len(tasks):
        tasks[task_number-1]["completed"]="True"
        save_task(tasks)
        print(f"Task{'task'} marked as completed")
    else:
        print("Invalid task number")

def delete_task(tasks,task_number):
    if 0<task_number<=len(tasks):
        del tasks[task_number-1]
        save_task(tasks)
        print(f"Task {'task'} deleted successfully")

    else:
        print("Invalid task number") 

def main():
    tasks = load_task()
    while True:
        print("\nOptions:")
        print("1. Add task")
        print("2. View tasks")
        print("3. Mark task as completed")
        print("4. Delete task")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            task = input("Enter the task: ")
            add_task(tasks, task)
        elif choice == "2":
            view_task(tasks)
        elif choice == "3":
            task_number = int(input("Enter the task number to mark as completed: "))
            mark_task_completed(tasks, task_number)
        elif choice == "4":
            task_number = int(input("Enter the task number to delete: "))
            delete_task(tasks, task_number)
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
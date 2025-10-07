import json
def main_function():
    while True:
        show_menu()
        choice = input("Enter your choice: ").strip()
        if choice == "1":
            add_task()
        elif choice == "2":
            delete_task()
        elif choice == "3":
            show_tasks()
        elif choice == "4":
            update_due_date()
        elif choice == "5":
            mark_task_completed()
        elif choice == "6":
             exit_program()
             break
        else:
            print("Invalid choice, please try again.")


def add_task():
    with open("user.json", "r") as file:
        data = json.load(file)
    title = input("Enter your title:").strip()
    description = input("Enter your description:").strip()
    due_date = input("Enter your due date:").strip()
    status = input("Enter your status(incomplete, complete, in progress)").strip().lower()
    new_task = {
        "title": title,
        "description": description,
        "due_date": due_date,
        "status": status}
    data.append(new_task)
    with open("user.json", "w") as file:
        json.dump(data, file)
    print("Task added successfully!")


def delete_task():
    with open("user.json", "r") as file:
        data = json.load(file)
    print("Tasks are:")
    for task in data:
        print(task["title"])
    your_task=input("Enter your task title to delete:").strip().lower()
    for task in data:
        if task["title"].strip().lower == your_task:
            data.remove(task)
            with open("user.json", "w") as file:
                json.dump(data, file)
            print("Task deleted successfully!")
            return
    print("Your task not found")



def  show_tasks():
    with open("user.json", "r") as file:
        data = json.load(file)
    print("1.Show all tasks")
    print("2.Show task details")
    choice = input("Enter your choice: ").strip()
    if choice == "1":
        print("Your tasks:")
        for task in data:
            print(task["title"])
            print(f" Description: {task['description']}")
            print(f" Due Date: {task['due_date']}")
            print(f" Status: {task['status']}")
    elif choice == "2":
        title=input("Enter your title:").strip()
        for task in data:
            if task["title"] == title:
                print(f"Title: {task['title']}")
                print(f" Description: {task['description']}")
                print(f" Due Date: {task['due_date']}")
                print(f" Status: {task['status']}")
                return
        print("Your task not found")
    else:
        print("Invalid choice, please try again.")

def update_due_date():
    with open("user.json", "r") as file:
        data = json.load(file)
    title=input("Enter your title:").strip()
    for task in data:
        if task["title"] == title:
            print("Your due date is " + task["due_date"])
            new_due_date = input("Enter your new due date:").strip()
            if task["due_date"] == new_due_date:
                print("Please change your due date.")
            else:
                task["due_date"] = new_due_date
                with open("user.json", "w") as file:
                    json.dump(data, file)
                print("Task updated successfully!")
            return
    print("Your task not found")


def mark_task_completed():
    with open("user.json", "r") as file:
        data = json.load(file)
    title = input("Enter your title:").strip().lower()
    for task in data:
        if task["title"].strip().lower() == title:
            if task["status"].strip().lower() == "complete":
                print("Task is already completed.")
            else:
                task["status"] = "complete"
                with open("user.json", "w") as file:
                    json.dump(data, file)
                print("Task updated successfully!")
            return
    print("Your task not found")


def exit_program():
    print("Thank you for using Task Manager application. Goodbye!.")

def show_menu():
    print("Menu")
    print("1.add task")
    print("2.delete task")
    print("3.show list of tasks")
    print("4. update due date")
    print("5.mark task as completed")
    print("6.Exit")

main_function()




import json

class Task :
    def __init__(self,title, description, due_date, status):
        self.title = title
        self.description = description
        self.due_date = due_date
        self.status = status

    def update_due_date(self,due_date):
        self.due_date = due_date

    def get_task_type(self):
        return "Normal Task"



    def dict_conv(self):
        lst={
            "type": self.__class__.__name__,
            "title" : self.title,
            "description" : self.description ,
            "due_date" : self.due_date ,
            "status" : self.status
        }
        return lst

    def show_task(self):
        print(f"Title: {self.title}")
        print(f"Description: {self.description}")
        print(f"Due Date: {self.due_date}")
        print(f"Status: {self.status}")
        print(f"Type: {self.get_task_type()}")

class PersonalTask(Task):
    def __init__(self,title, description, due_date,status,category ):
        super().__init__(title, description, due_date,status)
        self.category = category

    def get_task_type(self):
        task_type = f"personal : {self.category}"
        return task_type

    def dict_conv(self):
        lst1 = super().dict_conv()
        lst1["category"] = self.category
        return lst1

class WorkTask(Task):

    def __init__(self,title, description, due_date, status ,priority):
        super().__init__(title, description, due_date, status)
        self.priority = priority

    def get_task_type(self):
        task_type = f"priority : {self.priority}"
        return task_type

    def dict_conv(self):
        lst1 = super().dict_conv()
        lst1["priority"] = self.priority
        return lst1

class Taskmanager:

    def __init__(self):
        self.tasks= []

    def add_task(self) :

        with open("user.json", "r") as file:
            data = json.load(file)

        title = input("Enter your title:").strip()
        description = input("Enter your description:").strip()
        due_date = input("Enter your due date:").strip()
        status = input("Enter your status(incomplete, complete, in progress)").strip().lower()

        print("Select task type:")
        print("1. Normal Task")
        print("2. Personal Task (with category)")
        print("3. Work Task (with priority)")
        task_type = input("Enter choice (1-3): ").strip()

        if task_type == "2":
            category = input("Enter category (family/sports/etc): ").strip()
            task = PersonalTask(title, description, due_date, status, category)

        elif task_type == "3":
            priority = input("Enter priority (high/medium/low): ").strip()
            task = WorkTask(title, description, due_date, status, priority)
        else:
            task = Task(title, description, due_date, status)


        task_data = task.dict_conv()
        data.append(task_data)

        with open("user.json", "w") as file:
            json.dump(data, file)
        print("Task added successfully!")

    def delete_task(self):

        with open("user.json", "r") as file:
            data = json.load(file)
        print("Tasks are:")
        for task in data:
            print(task["title"])
        your_task = input("Enter your task title to delete:").strip()
        for task in data:
            if task["title"] == your_task:
                data.remove(task)
                with open("user.json", "w") as file:
                    json.dump(data, file)
                print("Task deleted successfully!")
                return
        print("Your task not found")

    def show_tasks(self):
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

            title = input("Enter your title:").strip()
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

    def list_tasks(self):
        try:
            if not self.tasks:
                raise IndexError("Task not found")
            for task in self.tasks:
                print(f"\n{task.title}")
        except IndexError as ie:
            print("Error:", ie)

    def update_due_date(self):

        with open("user.json", "r") as file:
            data = json.load(file)
        title = input("Enter your title:").strip().lower()
        for task in data:
            if task["title"].strip().lower() == title:
                print("Your due date is " + task["due_date"])
                new_due_date = input("Enter your new due date:").strip().lower()
                if task["due_date"] == new_due_date:
                    print("Please change your due date.")
                else:
                    task["due_date"] = new_due_date
                    with open("user.json", "w") as file:
                        json.dump(data, file)
                    print("Task updated successfully!")
                return
        print("Your task not found")

    def mark_task_completed(self):
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

#####################  main here  ###########################
Task_Manager = Taskmanager()

def main_function():
    while True:
        show_menu()
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            Task_Manager.add_task()
        elif choice == "2":
            Task_Manager.delete_task()
        elif choice == "3":
            Task_Manager.show_tasks()
        elif choice == "4":
            Task_Manager.update_due_date()
        elif choice == "5":
            Task_Manager.mark_task_completed()
        elif choice == "6":
             exit_program()
             break
        else:
            print("Invalid choice, please try again.")

def exit_program():
    print("Thank you for using Task Manager application. Goodbye!.")

def show_menu():
    print("Menu")
    print("1.add task")
    print("2.delete task")
    print("3.show list of tasks")
    print("4.update due date")
    print("5.mark task as completed")
    print("6.Exit")

main_function()
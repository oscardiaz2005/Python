class Task:
    def __init__(self, name):
        self.name = name
        self.completed = False

    def mark_completed(self):
        self.completed = True

    def __str__(self):
        status = "Completed" if self.completed else "Pending"
        return f"Task: {self.name} - Status: {status}"


class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task_name):
        task = Task(task_name)
        self.tasks.append(task)

    def mark_task_completed(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index].mark_completed()
        else:
            print("Invalid task index")

    def list_pending_tasks(self):
        pending_tasks = [task for task in self.tasks if not task.completed]
        if pending_tasks:
            print("Pending Tasks:")
            for task in pending_tasks:
                print(f"- {task.name}")
        else:
            print("No pending tasks")

    def list_all_tasks(self):
        if self.tasks:
            print("List of all tasks:")
            for task in self.tasks:
                print(task)
        else:
            print("No tasks available")


def show_menu():
    print("\nMenu:")
    print("1. Add task")
    print("2. Mark task as completed")
    print("3. Show all tasks")
    print("4. Show pending tasks")
    print("5. Exit")

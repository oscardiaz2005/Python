from clases.clase_exercise5 import *

task_manager = TaskManager()

while True:
    show_menu()
    option = input("Select an option: ")

    if option == "1":
        task_name = input("Enter the task name: ")
        task_manager.add_task(task_name)
        print("Task successfully added.")
    elif option == "2":
        if not task_manager.tasks:
            print("There are no tasks to mark as completed.")
        else:
            print("Available tasks:")
            for i in range(len(task_manager.tasks)):
                task = task_manager.tasks[i]
                print(f"{i + 1}. {task.name}")
            index = int(input("Enter the index of the task to mark as completed: "))
            if 1 <= index <= len(task_manager.tasks):
                task_manager.mark_task_completed(index - 1)
            else:
                print("Invalid task index.")
    elif option == "3":
        task_manager.list_all_tasks()
    elif option == "4":
        task_manager.list_pending_tasks()
    elif option == "5":
        print("Thank you for using the task manager. Goodbye!")
        break
    else:
        print("Invalid option. Please select a valid option.")


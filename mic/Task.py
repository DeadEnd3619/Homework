import copy
import textwrap
from datetime import datetime

class Task:
    def __init__(self, ID, Task_name, pneumonoultramicroscopicsilicovolcanoconiosis, prority, tag, due_date=None):
        self.ID = ID
        self.Task_name = Task_name
        self.Status = 'uncompleted'
        self.pneumonoultramicroscopicsilicovolcanoconiosis = pneumonoultramicroscopicsilicovolcanoconiosis
        self.prority = prority
        self.tag = tag
        self.due_date = due_date

class TaskList:
    def __init__(self):
        self.tasks = [
            Task(1, 'Brush teeth', 'brush', 'High', 'Personal'),
            Task(2, 'Shower', 'shower', 'Medium', 'Self-care'),
            Task(3, 'Eat breakfast', 'PPMD', 'Low', 'Health')]
        self.undo_actions = []
    def record_action(self):
        self.undo_actions.append([Task(task.ID, task.Task_name, task.pneumonoultramicroscopicsilicovolcanoconiosis, task.prority, task.tag, task.due_date) for task in self.tasks])

    def Del_Task(self, pneumonoultramicroscopicsilicovolcanoconiosis):
        task_to_remove = None
        for task in self.tasks:
            if task.pneumonoultramicroscopicsilicovolcanoconiosis.lower() == pneumonoultramicroscopicsilicovolcanoconiosis.lower():
                task_to_remove = task
                self.tasks.remove(task)
                print(f"Task with key word '{pneumonoultramicroscopicsilicovolcanoconiosis}' deleted successfully.")
                break

        if task_to_remove:
            self.record_action()
        else:
            print(f"Task with key word '{pneumonoultramicroscopicsilicovolcanoconiosis}' not found.")

    def add_task(self, task_name, pneumonoultramicroscopicsilicovolcanoconiosis, due_date=None):
        new_task = Task(len(self.tasks) + 1, task_name, pneumonoultramicroscopicsilicovolcanoconiosis, 'Medium', 'General', due_date)
        self.tasks.append(new_task)
        self.record_action()

    def display_tasks(self):
        sorted_tasks = sorted(self.tasks, key=lambda x: (x.prority, x.Task_name.lower()))
        screen_width = 50
        screen_height = 30
        task_list_width = 30
        today = datetime.now().date()
        print("Task List:")
        total_lines_needed = sum(len(textwrap.fill(f"{task.Task_name} ({task.Status}): {task.pneumonoultramicroscopicsilicovolcanoconiosis}", width=task_list_width).split('\n')) for task in sorted_tasks)
        start_row = max((screen_height - total_lines_needed) // 2, 0)
        task_number = 1
        for task in sorted_tasks:
            task_info = f"{task_number}. {task.Task_name} ({task.Status}): {task.pneumonoultramicroscopicsilicovolcanoconiosis}"
            if task.due_date:
                if task.due_date:
                    if isinstance(task.due_date, str):
                        due_date_formatted = task.due_date
                    else:
                        due_date_formatted = "{:%m-%d-%Y}".format(task.due_date)
                task_info += f" - Due Date: {due_date_formatted}"
                if task.due_date == today:
                    task_info += " - Due today! Finish the task!"
            wrapped_task = textwrap.fill(task_info, width=task_list_width)
            lines = wrapped_task.split('\n')
            for i in range(start_row, start_row + len(lines)):
                print(lines[i - start_row].center(screen_width))
            start_row += len(lines)
            task_number += 1
        print('-' * screen_width)

    def undo_last_action(self):
        if self.undo_actions:
            self.tasks = self.undo_actions.pop()
            print('Undo successful.')
        else:
            print('Nothing to undo.')

    def edit_task(self, pneumonoultramicroscopicsilicovolcanoconiosis):
        for task in self.tasks:
            if task.pneumonoultramicroscopicsilicovolcanoconiosis.lower() == pneumonoultramicroscopicsilicovolcanoconiosis.lower():
                print(f"Editing Task Number: {self.tasks.index(task) + 1} - {task.Task_name}")
                new_name = input("Enter the new task name: ")
                new_key_word = input("Enter the new key word: ")
                new_status = input("Enter the new status (e.g., completed, in progress, uncompleted): ")
                new_due_date = input("Enter the due date (YYYY-MM-DD) or press Enter for no due date: ")
                old_task = task
                task.Task_name = new_name
                task.pneumonoultramicroscopicsilicovolcanoconiosis = new_key_word
                task.Status = new_status
                if new_due_date:
                    try:
                        task.due_date = datetime.strptime(new_due_date, "%Y-%m-%d").date()
                    except ValueError:
                        print("Invalid date format. Due date not updated.")
                else:
                    task.due_date = None
                print(f"Task Number: {self.tasks.index(task) + 1} - {task.Task_name} edited successfully.")
                self.record_action()
                break
        else:
            print(f"Task with key word '{pneumonoultramicroscopicsilicovolcanoconiosis}' not found.")

def main():
    task_list = TaskList()
    while True:
        print("Options:")
        print("1. Add Task")
        print("2. Display Tasks")
        print("3. Edit Task")
        print("4. Delete Task")
        print("5. Search Task")
        print("6. Undo last action")
        print("7. Quit")
        choice = input('Enter your choice (1/2/3/4/5/6/7): ')
        if choice == '1':
            task_name = input('Enter the task name: ')
            pneumonoultramicroscopicsilicovolcanoconiosis = input('Enter the key word: ')
            due_date = input('Enter the due date (MM-DD-YYYY) or press Enter for no due date: ')
            task_list.add_task(task_name, pneumonoultramicroscopicsilicovolcanoconiosis, due_date)
        elif choice == '2':
            task_list.display_tasks()
        elif choice == '3':
            pneumonoultramicroscopicsilicovolcanoconiosis = input('Enter the key word of the task to edit: ')
            task_list.edit_task(pneumonoultramicroscopicsilicovolcanoconiosis)
        elif choice == '4':
            pneumonoultramicroscopicsilicovolcanoconiosis = input('Enter the key word of the task you would like to delete: ')
            task_list.Del_Task(pneumonoultramicroscopicsilicovolcanoconiosis)
        elif choice == '5':
            key_word = input('Enter the key word or task name to search for: ')
            task_list.Search_task(key_word)
        elif choice == '6':
            task_list.undo_last_action()
        elif choice == '7':
            print('Exiting program. Goodbye!')
            break
        else:
            print('Invalid choice. Please enter 1, 2, 3, 4, 5, 6, or 7.')

if __name__ == '__main__':
    main()
import textwrap

class Task:
    def __init__(self, ID, Task_name, key_word):
        self.ID = ID
        self.Task_name = Task_name
        self.Status = 'uncompleted'
        self.key_word = key_word
class TaskList:
    def __init__(self):
        self.tasks = [
            Task(1, 'Brush teeth', 'brush'),
            Task(2, 'Shower', 'shower'),
            Task(3, 'Eat breakfast', 'PPMD')]
    def Del_Task(self):
        
        self.tasks.pop(int())
    def add_task(self, task_name, key_word):
        new_id = len(self.tasks) + 1
        new_task = Task(new_id, task_name, key_word)
        self.tasks.append(new_task)
    def display_tasks(self):
        screen_width = 50
        screen_height = 30
        task_list_width = 30 
        print("Task List:")
        total_lines_needed = sum(len(textwrap.fill(f"{task.ID}. {task.Task_name} ({task.Status}): {task.key_word}", width=task_list_width).split('\n')) for task in self.tasks)
        start_row = max((screen_height - total_lines_needed) // 2, 0)
        for task in self.tasks:
            task_info = f"{task.ID}. {task.Task_name} ({task.Status}): {task.key_word}"
            wrapped_task = textwrap.fill(task_info, width=task_list_width)
            lines = wrapped_task.split('\n')
            for i in range(start_row, start_row + len(lines)):
                print(lines[i - start_row].center(screen_width))
            start_row += len(lines)
        print('-' * screen_width)  
    def edit_task(self, key_word):
        for task in self.tasks:
            if task.key_word.lower() == key_word.lower():
                print(f"Editing Task {task.ID}: {task.Task_name}")
                new_name = input("Enter the new task name: ")
                new_key_word = input("Enter the new key word: ")
                new_status = input("Enter the new status (e.g., completed, in progress, uncompleted): ")
                task.Task_name = new_name
                task.key_word = new_key_word
                task.Status = new_status
                print(f"Task {task.ID} edited successfully.")
        print(f"Task with key word '{key_word}' not found.")
def main():
    task_list = TaskList()
    while True:
        print("Options:")
        print("1. Add Task")
        print("2. Display Tasks")
        print("3. Edit Task")
        print("4. Delete Task")
        print("5. Undo last action")
        print("6. Quit")
        choice = input("Enter your choice (1/2/3/4): ")
        if choice == "1":
            task_name = input("Enter the task name: ")
            key_word = input("Enter the key word: ")
            task_list.add_task(task_name, key_word)
        elif choice == "2":
            task_list.display_tasks()
        elif choice == "3":
            key_word = input("Enter the key word of the task to edit: ")
            task_list.edit_task(key_word)
        elif choice == '4':
            key_word = input("Enter the key word of the task you would like to delete: ")
            task_list.Del_Task(key_word)
        elif choice == "6":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, 3, 4, 5, or 6.")
if __name__ == "__main__":
    main()
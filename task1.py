import tkinter as tk
from tkinter import messagebox,simpledialog

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        messagebox.showinfo("Task Added", f'Task "{task}" added successfully.')

    def view_tasks(self):
        if not self.tasks:
            messagebox.showinfo("To-Do List", "No tasks in the To-Do List.")
        else:
            tasks_text = "\n".join(f"{index}. {task}" for index, task in enumerate(self.tasks, start=1))
            messagebox.showinfo("To-Do List", f"Tasks in the To-Do List:\n{tasks_text}")

    def mark_done(self, task_index):
        if 1 <= task_index <= len(self.tasks):
            task = self.tasks[task_index - 1]
            messagebox.showinfo("Task Done", f'Task "{task}" marked as done.')
            del self.tasks[task_index - 1]
        else:
            messagebox.showerror("Error", "Invalid task index.")

class ToDoListApp:
    def __init__(self, master):
        self.master = master
        self.master.title("To-Do List App")

        self.todo_list = ToDoList()

        self.label = tk.Label(master, text="To-Do List App", font=("Helvetica", 16))
        self.label.pack(pady=10)

        self.add_button = tk.Button(master, text="Add Task", command=self.add_task)
        self.add_button.pack(pady=5)

        self.view_button = tk.Button(master, text="View Tasks", command=self.view_tasks)
        self.view_button.pack(pady=5)

        self.mark_done_button = tk.Button(master, text="Mark Task as Done", command=self.mark_done)
        self.mark_done_button.pack(pady=5)

    def add_task(self):
        task = simpledialog.askstring("Add Task", "Enter the task:")
        if task:
            self.todo_list.add_task(task)

    def view_tasks(self):
        self.todo_list.view_tasks()

    def mark_done(self):
        task_index = simpledialog.askinteger("Mark Task as Done", "Enter the task index to mark as done:")
        if task_index:
            self.todo_list.mark_done(task_index)

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoListApp(root)
    root.mainloop()

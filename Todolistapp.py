# Todo List GUI App

import tkinter as tk
from tkinter import messagebox

class TodoListApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Todo List App")
        self.tasks = []

        # Create GUI components
        self.task_listbox = tk.Listbox(self.root, width=40, height=10)
        self.task_listbox.pack(padx=10, pady=10)

        self.task_entry = tk.Entry(self.root, width=40)
        self.task_entry.pack(padx=10, pady=10)

        self.add_button = tk.Button(self.root, text="Add Task", command=self.add_task, background="light green")
        self.add_button.pack(padx=10, pady=10)

        self.delete_button = tk.Button(self.root, text="Delete Task", command=self.delete_task, background="light green")
        self.delete_button.pack(padx=10, pady=10)

        self.complete_button = tk.Button(self.root, text="Complete Task", command=self.complete_task, background="light green")
        self.complete_button.pack(padx=10, pady=10)

        self.load_tasks()

    def load_tasks(self):
        try:
            with open("todo_list.txt", "r") as f:
                self.tasks = [line.strip() for line in f.readlines()]
            self.task_listbox.delete(0, tk.END)
            for task in self.tasks:
                self.task_listbox.insert(tk.END, task)
        except FileNotFoundError:
            pass

    def save_tasks(self):
        with open("todo_list.txt", "w") as f:
            for task in self.tasks:
                f.write(task + "\n")

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append(task)
            self.task_listbox.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)
            self.save_tasks()

    def delete_task(self):
        try:
            task_index = self.task_listbox.curselection()[0]
            self.task_listbox.delete(task_index)
            del self.tasks[task_index]
            self.save_tasks()
        except IndexError:
            messagebox.showerror("Error", "Select a task to delete")

    def complete_task(self):
        try:
            task_index = self.task_listbox.curselection()[0]
            task = self.tasks[task_index]
            self.tasks[task_index] = f"[X] {task}"
            self.task_listbox.delete(task_index)
            self.task_listbox.insert(task_index, self.tasks[task_index])
            self.save_tasks()
        except IndexError:
            messagebox.showerror("Error", "Select a task to complete")

if __name__ == "__main__":
    root = tk.Tk()
    root.configure(background="light blue")  # Set the background color of the root window
    app = TodoListApp(root)
    root.mainloop() 
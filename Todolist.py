import tkinter as tk
from tkinter import messagebox

class TaskManager:
    def __init__(self, master):
        self.master = master
        self.master.title("Task Organizer")

        self.task_data = []

        self.task_box = tk.Listbox(self.master, height=12, width=50)
        self.task_box.grid(row=0, column=0, columnspan=2, padx=20, pady=15)

        self.task_input = tk.Entry(self.master, width=40)
        self.task_input.grid(row=1, column=0, padx=20, pady=5)

        tk.Button(self.master, text="Add Task", width=15, command=self.add_task).grid(row=1, column=1, pady=5)
        tk.Button(self.master, text="Remove Selected", width=15, command=self.delete_task).grid(row=2, column=0, pady=5)
        tk.Button(self.master, text="Mark as Complete", width=15, command=self.complete_task).grid(row=2, column=1, pady=5)
        tk.Button(self.master, text="Clear All Tasks", width=15, command=self.clear_all).grid(row=3, column=0, columnspan=2, pady=10)

    def add_task(self):
        task_text = self.task_input.get().strip()
        if not task_text:
            messagebox.showwarning("Empty Task", "Please enter a task before adding.")
            return

        self.task_data.append({"title": task_text, "completed": False})
        self.task_input.delete(0, tk.END)
        self.refresh_display()

    def delete_task(self):
        try:
            selected = self.task_box.curselection()[0]
        except IndexError:
            messagebox.showwarning("No Selection", "Please select a task to delete.")
            return

        removed = self.task_data.pop(selected)
        self.refresh_display()
        messagebox.showinfo("Task Removed", f"Deleted: '{removed['title']}'")

    def complete_task(self):
        try:
            selected = self.task_box.curselection()[0]
        except IndexError:
            messagebox.showwarning("No Selection", "Please select a task to mark as complete.")
            return

        self.task_data[selected]["completed"] = True
        self.refresh_display()

    def clear_all(self):
        if messagebox.askyesno("Clear All", "Are you sure you want to clear all tasks?"):
            self.task_data.clear()
            self.refresh_display()

    def refresh_display(self):
        self.task_box.delete(0, tk.END)
        for task in self.task_data:
            status = "✅ Completed" if task["completed"] else "🕗 Incomplete"
            self.task_box.insert(tk.END, f"{task['title']} — {status}")

def main():
    root = tk.Tk()
    app = TaskManager(root)
    root.mainloop()

if __name__ == "__main__":
    main()

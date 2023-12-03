import tkinter as tk
from tkinter import ttk
from backend import PerformanceDB

class PerformanceApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Performance Management System")

        self.performance_db = PerformanceDB()


        tk.Label(self.root, text="Staff Name:").grid(row=0, column=0, padx=5, pady=5)
        self.staff_name_entry = tk.Entry(self.root)
        self.staff_name_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(self.root, text="Achievement:").grid(row=1, column=0, padx=5, pady=5)
        self.achievement_entry = tk.Entry(self.root)
        self.achievement_entry.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(self.root, text="Goal:").grid(row=2, column=0, padx=5, pady=5)
        self.goal_entry = tk.Entry(self.root)
        self.goal_entry.grid(row=2, column=1, padx=5, pady=5)

        tk.Label(self.root, text="Feedback:").grid(row=3, column=0, padx=5, pady=5)
        self.feedback_entry = tk.Text(self.root, height=5, width=30)
        self.feedback_entry.grid(row=3, column=1, padx=5, pady=5)

        self.submit_button = tk.Button(self.root, text="Submit Entry", command=self.submit_entry)
        self.submit_button.grid(row=4, column=0, columnspan=2, pady=10)


        self.tree = ttk.Treeview(self.root, columns=('ID', 'Staff Name', 'Achievement', 'Goal', 'Feedback'))
        self.tree.grid(row=5, column=0, columnspan=2, padx=5, pady=5)

        self.tree.heading('#0', text='ID')
        self.tree.heading('#1', text='Staff Name')
        self.tree.heading('#2', text='Achievement')
        self.tree.heading('#3', text='Goal')
        self.tree.heading('#4', text='Feedback')

        self.update_treeview()

    def submit_entry(self):
        staff_name = self.staff_name_entry.get()
        achievement = self.achievement_entry.get()
        goal = self.goal_entry.get()
        feedback = self.feedback_entry.get("1.0", tk.END).strip()

        if staff_name and achievement and goal and feedback:
            self.performance_db.add_performance_entry(staff_name, achievement, goal, feedback)
            self.update_treeview()


            self.staff_name_entry.delete(0, tk.END)
            self.achievement_entry.delete(0, tk.END)
            self.goal_entry.delete(0, tk.END)
            self.feedback_entry.delete(1.0, tk.END)

    def update_treeview(self):
        for row in self.tree.get_children():
            self.tree.delete(row)

        performance_data = self.performance_db.get_all_performance_entries()

        for row in performance_data:
            self.tree.insert('', 'end', values=row)

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    app = PerformanceApp(root)
    app.run()
    app.performance_db.close_connection()

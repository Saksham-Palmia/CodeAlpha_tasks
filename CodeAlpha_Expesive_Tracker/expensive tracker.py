import tkinter as tk
from tkinter import messagebox, filedialog
import csv
from tkinter import ttk

class Expense:
    def __init__(self, amount, category, date, description):
        self.amount = amount
        self.category = category
        self.date = date
        self.description = description

class ExpenseTracker:
    def __init__(self, budget):
        self.budget = budget
        self.expenses = []

    def add_expense(self, expense):
        self.expenses.append(expense)

    def get_total_expenses(self):
        return sum(expense.amount for expense in self.expenses)

    def get_remaining_budget(self):
        return self.budget - self.get_total_expenses()

    def save_expenses(self, filename):
        with open(filename, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Amount", "Category", "Date", "Description"])
            for expense in self.expenses:
                writer.writerow([expense.amount, expense.category, expense.date, expense.description])

    def load_expenses(self, filename):
        self.expenses.clear()
        with open(filename, 'r') as file:
            reader = csv.reader(file)
            next(reader)  # Skip the header row
            for row in reader:
                amount, category, date, description = row
                self.add_expense(Expense(float(amount), category, date, description))

class ExpenseTrackerGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Expense Tracker")
        self.master.geometry("600x400")
        self.master.configure(bg="#2e3f4f")

        # Create frames
        self.header_frame = tk.Frame(self.master, bg="#1f2a36")
        self.header_frame.pack(fill="x")

        self.content_frame = tk.Frame(self.master, bg="#2e3f4f")
        self.content_frame.pack(fill="both", expand=True)

        # Create header
        self.header_label = tk.Label(self.header_frame, text="Expense Tracker", font=("Helvetica", 24, "bold"), bg="#1f2a36", fg="white")
        self.header_label.pack(pady=10)

        # Create menu
        self.menu_frame = tk.Frame(self.content_frame, bg="#2e3f4f")
        self.menu_frame.pack(fill="x")

        self.add_expense_button = tk.Button(self.menu_frame, text="Add Expense", command=self.add_expense, bg="#4CAF50", fg="white", font=("Helvetica", 12, "bold"))
        self.add_expense_button.pack(side="left", padx=10, pady=5)

        self.view_expenses_button = tk.Button(self.menu_frame, text="View Expenses", command=self.view_expenses, bg="#2196F3", fg="white", font=("Helvetica", 12, "bold"))
        self.view_expenses_button.pack(side="left", padx=10, pady=5)

        self.total_spending_button = tk.Button(self.menu_frame, text="Total Spending", command=self.total_spending, bg="#FF5722", fg="white", font=("Helvetica", 12, "bold"))
        self.total_spending_button.pack(side="left", padx=10, pady=5)

        self.remaining_budget_button = tk.Button(self.menu_frame, text="Remaining Budget", command=self.remaining_budget, bg="#9C27B0", fg="white", font=("Helvetica", 12, "bold"))
        self.remaining_budget_button.pack(side="left", padx=10, pady=5)

        self.save_expenses_button = tk.Button(self.menu_frame, text="Save Expenses", command=self.save_expenses, bg="#FFEB3B", fg="black", font=("Helvetica", 12, "bold"))
        self.save_expenses_button.pack(side="left", padx=10, pady=5)

        self.load_expenses_button = tk.Button(self.menu_frame, text="Load Expenses", command=self.load_expenses, bg="#FFC107", fg="black", font=("Helvetica", 12, "bold"))
        self.load_expenses_button.pack(side="left", padx=10, pady=5)

        # Create expense list
        self.expense_list_frame = tk.Frame(self.content_frame, bg="#2e3f4f")
        self.expense_list_frame.pack(fill="both", expand=True)

        self.expense_list = tk.Listbox(self.expense_list_frame, width=60, height=15, bg="#f0f0f0", fg="#000000", font=("Helvetica", 12))
        self.expense_list.pack(fill="both", expand=True, padx=20, pady=20)

        # Create tracker
        self.tracker = ExpenseTracker(30000)

    def add_expense(self):
        # Create add expense window
        add_expense_window = tk.Toplevel(self.master)
        add_expense_window.title("Add Expense")
        add_expense_window.geometry("300x300")
        add_expense_window.configure(bg="#2e3f4f")

        # Create labels and entries
        amount_label = tk.Label(add_expense_window, text="Amount:", bg="#2e3f4f", fg="white", font=("Helvetica", 12))
        amount_label.pack(pady=5)
        amount_entry = tk.Entry(add_expense_window)
        amount_entry.pack(pady=5)

        category_label = tk.Label(add_expense_window, text="Category:", bg="#2e3f4f", fg="white", font=("Helvetica", 12))
        category_label.pack(pady=5)
        category_entry = tk.Entry(add_expense_window)
        category_entry.pack(pady=5)

        date_label = tk.Label(add_expense_window, text="Date:", bg="#2e3f4f", fg="white", font=("Helvetica", 12))
        date_label.pack(pady=5)
        date_entry = tk.Entry(add_expense_window)
        date_entry.pack(pady=5)

        description_label = tk.Label(add_expense_window, text="Description:", bg="#2e3f4f", fg="white", font=("Helvetica", 12))
        description_label.pack(pady=5)
        description_entry = tk.Entry(add_expense_window)
        description_entry.pack(pady=5)

        # Create add button
        def add_expense_callback():
            amount = float(amount_entry.get())
            category = category_entry.get()
            date = date_entry.get()
            description = description_entry.get()
            self.tracker.add_expense(Expense(amount, category, date, description))
            add_expense_window.destroy()

        add_button = tk.Button(add_expense_window, text="Add", command=add_expense_callback, bg="#4CAF50", fg="white", font=("Helvetica", 12, "bold"))
        add_button.pack(pady=10)

    def view_expenses(self):
        # Clear expense list
        self.expense_list.delete(0, tk.END)

        # Add expenses to list
        for expense in self.tracker.expenses:
            self.expense_list.insert(tk.END, f"Amount: {expense.amount}, Category: {expense.category}, Date: {expense.date}, Description: {expense.description}")

    def total_spending(self):
        messagebox.showinfo("Total Spending", f"Total Spending: {self.tracker.get_total_expenses()}")

    def remaining_budget(self):
        messagebox.showinfo("Remaining Budget", f"Remaining Budget: {self.tracker.get_remaining_budget()}")

    def save_expenses(self):
        filename = filedialog.asksaveasfilename(defaultextension=".csv")
        if filename:
            self.tracker.save_expenses(filename)

    def load_expenses(self):
        filename = filedialog.askopenfilename(defaultextension=".csv")
        if filename:
            self.tracker.load_expenses(filename)
            self.view_expenses()  # Refresh the expense list

root = tk.Tk()
gui = ExpenseTrackerGUI(root)
root.mainloop()

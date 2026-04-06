import tkinter as tk
from datetime import datetime

expenses = []

# Add expense
def add_expense():
    amount = amount_entry.get()
    category = category_entry.get()

    if amount and category:
        date = datetime.now().strftime("%d-%m-%Y")

        expense_text = f"{date} | {category} | ₹{amount}"
        listbox.insert(tk.END, expense_text)

        expenses.append(float(amount))
        update_total()

        amount_entry.delete(0, tk.END)
        category_entry.delete(0, tk.END)

# Delete selected expense
def delete_expense():
    selected = listbox.curselection()
    if selected:
        index = selected[0]
        listbox.delete(index)
        expenses.pop(index)
        update_total()

# Clear all
def clear_all():
    listbox.delete(0, tk.END)
    expenses.clear()
    update_total()

# Update total
def update_total():
    total_label.config(text=f"Total: ₹{sum(expenses)}")

# GUI
root = tk.Tk()
root.title("Expense Tracker")
root.geometry("350x400")

tk.Label(root, text="Amount").pack()
amount_entry = tk.Entry(root)
amount_entry.pack()

tk.Label(root, text="Category").pack()
category_entry = tk.Entry(root)
category_entry.pack()

tk.Button(root, text="Add Expense", command=add_expense).pack(pady=5)
tk.Button(root, text="Delete Selected", command=delete_expense).pack(pady=5)
tk.Button(root, text="Clear All", command=clear_all).pack(pady=5)

listbox = tk.Listbox(root)
listbox.pack(fill=tk.BOTH, expand=True)

total_label = tk.Label(root, text="Total: ₹0")
total_label.pack(pady=5)

root.mainloop()
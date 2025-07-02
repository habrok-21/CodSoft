import tkinter as tk
from tkinter import messagebox

# Function to perform the calculation
def perform_calculation():
    try:
        number1 = float(entry_first.get())
        number2 = float(entry_second.get())
        operation = operation_choice.get()

        if operation == "Addition":
            result = number1 + number2
        elif operation == "Subtraction":
            result = number1 - number2
        elif operation == "Multiplication":
            result = number1 * number2
        elif operation == "Division":
            if number2 == 0:
                messagebox.showerror("Math Error", "Division by zero is not allowed.")
                return
            result = number1 / number2
        else:
            messagebox.showerror("Invalid Selection", "Please select a valid operation.")
            return

        result_label.config(text=f"Result: {result}")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numerical values.")

# Function to clear fields
def clear_fields():
    entry_first.delete(0, tk.END)
    entry_second.delete(0, tk.END)
    result_label.config(text="Result will be shown here")

# Main window setup
app = tk.Tk()
app.title("Basic Calculator")
app.geometry("400x300")

tk.Label(app, text="Enter First Number:").pack(pady=5)
entry_first = tk.Entry(app)
entry_first.pack(pady=5)

tk.Label(app, text="Enter Second Number:").pack(pady=5)
entry_second = tk.Entry(app)
entry_second.pack(pady=5)

tk.Label(app, text="Select Operation:").pack(pady=5)
operation_choice = tk.StringVar(value="Addition")
operations = ["Addition", "Subtraction", "Multiplication", "Division"]
operation_menu = tk.OptionMenu(app, operation_choice, *operations)
operation_menu.pack(pady=5)

tk.Button(app, text="Calculate", command=perform_calculation).pack(pady=10)
tk.Button(app, text="Clear", command=clear_fields).pack(pady=5)

result_label = tk.Label(app, text="Result will be shown here", font=("Arial", 12))
result_label.pack(pady=15)

app.mainloop()

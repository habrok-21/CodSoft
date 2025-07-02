import tkinter as tk
from tkinter import messagebox
import random
import string

def create_password():
    try:
        desired_length = int(length_input.get())
        if desired_length <= 0:
            raise ValueError
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a positive number for password length.")
        return

    characters = string.ascii_letters + string.digits + string.punctuation
    new_password = ''.join(random.choice(characters) for _ in range(desired_length))

    password_display.set(new_password)

def copy_to_clipboard():
    generated = password_display.get()
    if generated:
        root.clipboard_clear()
        root.clipboard_append(generated)
        messagebox.showinfo("Copied", "Password copied to clipboard!")
    else:
        messagebox.showwarning("No Password", "Please generate a password first.")

# Main window setup
root = tk.Tk()
root.title("Secure Password Generator")
root.geometry("350x200")

tk.Label(root, text="Enter desired password length:").pack(pady=5)
length_input = tk.Entry(root)
length_input.pack(pady=5)

tk.Button(root, text="Generate Password", command=create_password).pack(pady=10)

password_display = tk.StringVar()
tk.Label(root, textvariable=password_display, font=("Arial", 14), fg="white").pack(pady=10)

tk.Button(root, text="Copy to Clipboard", command=copy_to_clipboard).pack(pady=5)

root.mainloop()

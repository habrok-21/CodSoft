import tkinter as tk
from tkinter import messagebox, simpledialog, ttk


class Person:
    def __init__(self, fullname, phone, email, address):
        self.fullname = fullname
        self.phone = phone
        self.email = email
        self.address = address

    def __repr__(self):
        return f"{self.fullname} | {self.phone} | {self.email} | {self.address}"


class PhoneBookApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Personal Contact Manager")

        self.contacts = []
        self.selected_index = None

        self.setup_ui()

    def setup_ui(self):
        tk.Label(self.master, text="Full Name").grid(row=0, column=0, padx=5, pady=5, sticky='w')
        self.name_entry = tk.Entry(self.master)
        self.name_entry.grid(row=0, column=1, padx=5, pady=5, sticky='ew')

        tk.Label(self.master, text="Phone Number").grid(row=1, column=0, padx=5, pady=5, sticky='w')
        self.phone_entry = tk.Entry(self.master)
        self.phone_entry.grid(row=1, column=1, padx=5, pady=5, sticky='ew')

        tk.Label(self.master, text="Email Address").grid(row=2, column=0, padx=5, pady=5, sticky='w')
        self.email_entry = tk.Entry(self.master)
        self.email_entry.grid(row=2, column=1, padx=5, pady=5, sticky='ew')

        tk.Label(self.master, text="Home Address").grid(row=3, column=0, padx=5, pady=5, sticky='w')
        self.address_entry = tk.Entry(self.master)
        self.address_entry.grid(row=3, column=1, padx=5, pady=5, sticky='ew')

        button_frame = tk.Frame(self.master)
        button_frame.grid(row=4, column=0, columnspan=2, pady=10)

        tk.Button(button_frame, text="Add Contact", command=self.add_person).grid(row=0, column=0, padx=3)
        tk.Button(button_frame, text="Update Contact", command=self.edit_person).grid(row=0, column=1, padx=3)
        tk.Button(button_frame, text="Delete Contact", command=self.remove_person).grid(row=0, column=2, padx=3)
        tk.Button(button_frame, text="Search Contact", command=self.search_person).grid(row=0, column=3, padx=3)
        tk.Button(button_frame, text="Show All", command=self.show_all).grid(row=0, column=4, padx=3)
        tk.Button(button_frame, text="Clear Fields", command=self.clear_inputs).grid(row=0, column=5, padx=3)

        self.tree = ttk.Treeview(self.master, columns=("Name", "Phone", "Email", "Address"), show='headings')
        self.tree.heading("Name", text="Full Name")
        self.tree.heading("Phone", text="Phone")
        self.tree.heading("Email", text="Email")
        self.tree.heading("Address", text="Address")

        self.tree.column("Name", width=150)
        self.tree.column("Phone", width=110)
        self.tree.column("Email", width=180)
        self.tree.column("Address", width=220)

        self.tree.grid(row=5, column=0, columnspan=2, sticky='nsew', padx=5, pady=5)
        self.tree.bind("<<TreeviewSelect>>", self.on_select)

        self.master.grid_columnconfigure(1, weight=1)
        self.master.grid_rowconfigure(5, weight=1)

    def add_person(self):
        name = self.name_entry.get().strip()
        phone = self.phone_entry.get().strip()
        email = self.email_entry.get().strip()
        address = self.address_entry.get().strip()

        if not name or not phone:
            messagebox.showwarning("Missing Info", "Name and phone number are required.")
            return

        if any(c.phone == phone for c in self.contacts):
            messagebox.showerror("Duplicate", "This phone number already exists.")
            return

        self.contacts.append(Person(name, phone, email, address))
        messagebox.showinfo("Added", "Contact successfully added.")
        self.clear_inputs()
        self.show_all()

    def show_all(self):
        for item in self.tree.get_children():
            self.tree.delete(item)
        for contact in self.contacts:
            self.tree.insert('', 'end', values=(contact.fullname, contact.phone, contact.email, contact.address))

    def on_select(self, event):
        selected = self.tree.selection()
        if not selected:
            self.selected_index = None
            return

        self.selected_index = self.tree.index(selected[0])
        contact = self.contacts[self.selected_index]

        self.name_entry.delete(0, tk.END)
        self.name_entry.insert(0, contact.fullname)
        self.phone_entry.delete(0, tk.END)
        self.phone_entry.insert(0, contact.phone)
        self.email_entry.delete(0, tk.END)
        self.email_entry.insert(0, contact.email)
        self.address_entry.delete(0, tk.END)
        self.address_entry.insert(0, contact.address)

    def edit_person(self):
        if self.selected_index is None:
            messagebox.showwarning("No Selection", "Please select a contact to update.")
            return

        name = self.name_entry.get().strip()
        phone = self.phone_entry.get().strip()
        email = self.email_entry.get().strip()
        address = self.address_entry.get().strip()

        if not name or not phone:
            messagebox.showwarning("Missing Info", "Name and phone cannot be empty.")
            return

        for idx, c in enumerate(self.contacts):
            if idx != self.selected_index and c.phone == phone:
                messagebox.showerror("Conflict", "Phone number already exists for another contact.")
                return

        contact = self.contacts[self.selected_index]
        contact.fullname = name
        contact.phone = phone
        contact.email = email
        contact.address = address

        messagebox.showinfo("Updated", "Contact information updated.")
        self.show_all()
        self.clear_inputs()
        self.selected_index = None

    def remove_person(self):
        if self.selected_index is None:
            messagebox.showwarning("No Selection", "Select a contact to delete.")
            return

        contact = self.contacts[self.selected_index]
        confirm = messagebox.askyesno("Confirm Delete", f"Are you sure you want to delete {contact.fullname}?")
        if confirm:
            self.contacts.pop(self.selected_index)
            messagebox.showinfo("Deleted", "Contact removed successfully.")
            self.show_all()
            self.clear_inputs()
            self.selected_index = None

    def search_person(self):
        term = simpledialog.askstring("Search", "Enter name or phone number to search:")
        if not term:
            return

        term = term.lower()
        results = [c for c in self.contacts if term in c.fullname.lower() or term in c.phone]

        for item in self.tree.get_children():
            self.tree.delete(item)
        for c in results:
            self.tree.insert('', 'end', values=(c.fullname, c.phone, c.email, c.address))

        if not results:
            messagebox.showinfo("No Results", "No contacts found matching your search.")

    def clear_inputs(self):
        self.name_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)
        self.address_entry.delete(0, tk.END)


if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("750x450")
    app = PhoneBookApp(root)
    root.mainloop()

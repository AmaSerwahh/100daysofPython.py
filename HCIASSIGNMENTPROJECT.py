import customtkinter as ctk
import tkinter as tk
from tkinter import messagebox

# Setup
ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("Task Manager")
app.geometry("420x500")

items = []


# Functions
def add_item():
    task = entry.get().strip()

    if task == "":
        messagebox.showwarning("Error", "Please enter a task!")
        return

    items.append(task)
    listbox.insert(tk.END, task)
    entry.delete(0, tk.END)
    status_label.configure(text="Item added ✅")


def delete_item():
    try:
        selected_index = listbox.curselection()[0]
        listbox.delete(selected_index)
        items.pop(selected_index)
        status_label.configure(text="Item deleted ❌")
    except:
        messagebox.showwarning("Error", "Select an item first!")


def toggle_mode():
    current = ctk.get_appearance_mode()
    if current == "Light":
        ctk.set_appearance_mode("dark")
    else:
        ctk.set_appearance_mode("light")


# UI Layout
title = ctk.CTkLabel(app, text="📝 Task Manager", font=("Arial", 22))
title.pack(pady=10)

entry = ctk.CTkEntry(app, placeholder_text="Enter a task...", width=280)
entry.pack(pady=10)

add_btn = ctk.CTkButton(app, text="Add Task", command=add_item)
add_btn.pack(pady=5)

# Frame for listbox + scrollbar
frame = ctk.CTkFrame(app)
frame.pack(pady=10, fill="both", expand=True)

scrollbar = tk.Scrollbar(frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

listbox = tk.Listbox(
    frame,
    font=("Arial", 12),
    yscrollcommand=scrollbar.set,
    selectbackground="#3B8ED0"
)
listbox.pack(fill="both", expand=True)

scrollbar.config(command=listbox.yview)

delete_btn = ctk.CTkButton(app, text="Delete Selected", command=delete_item)
delete_btn.pack(pady=5)

toggle_btn = ctk.CTkButton(app, text="Toggle Dark Mode", command=toggle_mode)
toggle_btn.pack(pady=10)

status_label = ctk.CTkLabel(app, text="", font=("Arial", 12))
status_label.pack(pady=5)

# Run app
app.mainloop()
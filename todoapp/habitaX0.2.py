"""
Docstring for todoapp.habitaX0.2
 So this is the GUI version of my previous project habitaX which 
 is ToDo app but this version will be more awesome and fun .LETS MAKE IT !

"""
# imports
import customtkinter as ctk
import tkinter as tk
from PIL import Image
import storage as strg

# --------------------------------------------------------------
# Window
window = ctk.CTk()
window.geometry("450x360")
window.title("HabitaX")
window.resizable(False, False)

# --------------------------------------------------------------
# Logo
logo = Image.open("HabitaX.png")
logo = ctk.CTkImage(light_image=logo, size=(140, 120))
logo_lbl = ctk.CTkLabel(window, image=logo, text="")
logo_lbl.pack(pady=10)

# --------------------------------------------------------------
# Main container
main_frame = ctk.CTkFrame(window)
main_frame.place(relx=0.5, rely=0.68, anchor="center")

main_frame.columnconfigure(0, weight=1)
main_frame.columnconfigure(1, weight=1)

# Left: Listbox frame
list_frame = ctk.CTkFrame(main_frame)
list_frame.grid(row=0, column=0, rowspan=2, padx=10, pady=5)

# Right top: Entry frame
input_frame = ctk.CTkFrame(main_frame)
input_frame.grid(row=0, column=1, padx=10, pady=5, sticky="n")

# Right bottom: Buttons frame
btn_frame = ctk.CTkFrame(main_frame)
btn_frame.grid(row=1, column=1, padx=10, pady=5, sticky="n")

# --------------------------------------------------------------
# Widgets
entry1 = ctk.CTkEntry(
    input_frame,
    width=160,
    placeholder_text="Enter your task"
)
entry1.pack(pady=5)

listbox = tk.Listbox(
    list_frame,
    height=9,
    width=28
)
listbox.pack(pady=10)

# --------------------------------------------------------------
# Load tasks (simple list)
t_tasks = strg.load_tasks()

# --------------------------------------------------------------
# Functions

def list_tasks():
    """Refresh listbox"""
    listbox.delete(0, tk.END)
    for task in (t_tasks):
      listbox.insert(tk.END, task)



def add_task():
    """Add new task"""
    task = entry1.get().strip().lower()
    if not task:
        return

    if task in t_tasks:
        entry1.delete(0, "end")
        return

    t_tasks.append(task)
    strg.save_tasks(t_tasks)
    list_tasks()
    entry1.delete(0, "end")


def delete_task():
    """Delete selected task"""
    selected = listbox.curselection()
    if not selected:
        return

    index = selected[0]
    t_tasks.pop(index)
    strg.save_tasks(t_tasks)
    list_tasks()

# --------------------------------------------------------------
# Buttons
buttons = {
    "Add Task": add_task,
    "Delete Task": delete_task,
}

for i, (text, func) in enumerate(buttons.items()):
    btn = ctk.CTkButton(btn_frame, text=text, command=func)
    btn.grid(row=i, column=0, sticky="ew", padx=5, pady=5)

# Enter key support
entry1.bind("<Return>", lambda e: add_task())

# Initial display
list_tasks()

# --------------------------------------------------------------
window.mainloop()

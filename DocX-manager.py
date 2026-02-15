import os
import shutil
import tkinter as tk
import customtkinter as ctk
from tkinter import messagebox as msg
from PIL import Image 

ctk.set_appearance_mode("light")
#window 
window = ctk.CTk()
window.title("DocX-manager")
window.geometry("500x500")
window.resizable(False, False)

#frames 
h_frame = ctk.CTkFrame(window, width=500, height=150, fg_color="#0A3323")
h_frame.pack()
h_frame.pack_propagate(False)
f_frame = ctk.CTkFrame(window, width=500, height=350, fg_color="#F7F4D5")
f_frame.pack()
f_frame.pack_propagate(False)
ins_frame = ctk.CTkFrame(h_frame, width=100, height=100, fg_color="#105666", border_width=2, border_color="grey")
ins_frame.place(rely=0.5, relx=0.2, anchor="center")

entry = ctk.CTkEntry(h_frame, placeholder_text="Enter the name ", width=200, corner_radius=10, fg_color="#F7F4D5")
entry.place(rely=0.5, relx=0.55, anchor="center")
listbox = tk.Listbox(f_frame, height=7, width=20, background="#F7F4D5")
listbox.pack(pady=10)


def create_folder():
    folder_name = entry.get().strip()
    
    try :
        if os.path.isdir(folder_name):
            msg.showerror("Error", "This file is already Exists")
        else:
            os.mkdir(folder_name)
            listbox.insert(tk.END, folder_name)
            msg.showinfo("info", "File Created")
    except PermissionError:
        msg.showerror("Permission Error", "folder not created due to permission error ")
        
def create_file():
    file_name = entry.get().strip()
    try:
        if os.path.isfile(file_name):
            msg.showerror("File Exists", "File already exists !")
        else:
            window2 = ctk.CTkToplevel(window)
            window2.geometry("350x350")
            window2.title(file_name)
            textbox = ctk.CTkTextbox(window2, width=350, height=300)
            textbox.pack(pady=5)
            def add_text():
                content = textbox.get("1.0", "end-1c")
                with open(file_name, "w") as f:
                    f.write(content)
                    listbox.insert(tk.END, file_name)
                    msg.showinfo("File", "File created sucessfully ")
                    window2.destroy()        
            add_t = ctk.CTkButton(window2, command=add_text, text="Add Text")
            add_t.pack(pady=5)
           

    except PermissionError :
        msg.showerror("Permission Error", "File not Created due to permission Error")
        
def delete():
    selected = listbox.curselection()

    if selected:
        index = selected[0]
        filename = listbox.get(index)
        
        full_path = os.path.join(os.getcwd(), filename)
        
        try :
            if os.path.isfile(full_path):
                os.remove(full_path)
            elif os.path.isdir(full_path):
                os.rmdir(full_path)
            
            listbox.delete(index)
            msg.showinfo("Success", "Item deleted sucessfully")
        except Exception as e :
          msg.showerror("Error", str(e))
          
current_file = None

def load_file():
    listbox.delete(0, tk.END)
    for item in os.listdir(os.getcwd()):
        if os.path.isfile(item):
            listbox.insert(tk.END, item)
            
def open_file():
    selected = listbox.curselection()
    if selected:
        filename = listbox.get(selected[0])
        full_path = os.path.join(os.getcwd(), filename)
        
        if os.path.isfile(full_path):
            
            editor = ctk.CTkToplevel(window)
            editor.geometry("400x400")
            editor.title(filename)
            
            textbox = ctk.CTkTextbox(editor, width=350, height=300, )
            textbox.pack(pady=10, padx=10, fill="both", expand=True)
            
            with open(full_path, "r") as f:
                content = f.read()
                textbox.insert("1.0", content)
                
            def save_and_close():
                content = textbox.get("1.0", "end-1c")
                with open(full_path, "w") as f:
                    f.write(content)
                editor.destroy()
            editor.protocol("WM_DELETE_WINDOW", save_and_close)
      

def list_items():
    listbox.delete(0, tk.END)
    
    path = os.getcwd()
    items = os.listdir(path)
    for item in items :
        listbox.insert(tk.END, item)
       
list_items()

edit_btn = ctk.CTkButton(f_frame, command=open_file, width=100, fg_color="#D3968C", text="Edit File")
edit_btn.pack(pady=5)
delete_btn = ctk.CTkButton(f_frame, command=delete, fg_color="#D3968C", text="Delete", width=100)
delete_btn.pack(pady=5)
button = ctk.CTkButton(f_frame,command=create_folder,  fg_color="#D3968C", text="Create folder", width=100)
button.pack(pady=5)
file_btn = ctk.CTkButton(f_frame, text="Create File", command=create_file,fg_color="#D3968C", width=100 )
file_btn.pack(pady=5)

window.mainloop()

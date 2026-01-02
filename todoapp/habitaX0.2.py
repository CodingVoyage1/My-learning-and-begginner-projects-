"""
Docstring for todoapp.habitaX0.2
 So this is the GUI version of my previous project habitaX which 
 is ToDo app but this version will be more awesome and fun .LETS MAKE IT !

"""
#imports 
import customtkinter as ctk
import tkinter as tk
from PIL import Image as img 
import storage as strg 
#--------------------------------------------------------------

#Making Window
window = ctk.CTk()
window.geometry("400x300")
window.title("HabitaX")
window.resizable(False, False)
#--------------------------------------------------------------
#Logo adding 
image = img.open("HabitaX.png")
image = ctk.CTkImage(light_image=image, size=(140, 120))
img_lbl = ctk.CTkLabel(window, image=image, text="")
img_lbl.pack(pady=10)
#Frame's
main_frame = ctk.CTkFrame(window)
main_frame.place(relx=0.5, rely=0.7, anchor="center")
main_frame.columnconfigure(0, weight=1) 
main_frame.columnconfigure(1, weight=1)
frame3 = ctk.CTkFrame(main_frame)
frame3.grid(row=0, column=0, rowspan=2, padx=10, pady=5, sticky="n")
frame2 = ctk.CTkFrame(main_frame)
frame2.grid(row=0, column=1, padx=10, pady=5, sticky="n")
frame = ctk.CTkFrame(main_frame)
frame.grid(row=1, column=1, padx=10, pady=5, sticky="n")

#--------------------------------------------------------------

#inputs or entry
entry1 = ctk.CTkEntry(frame2, font=("Arial", 12), width=140, placeholder_text="Enter your tasks " )
entry1.grid()
listbox = tk.Listbox(frame3, height=8 , width=30,)
listbox.pack(pady=20,)
#---------------------------------------------------------------
t_tasks = strg.load_tasks()
#---------------------------------------------------------------
#functions or options  
def list_tasks():
  listbox.delete(0, tk.END)

  for i , task in enumerate(t_tasks, start=1):
    listbox.insert(tk.END, f"{i}.{task}")

def add_task():
   task = entry1.get().strip().lower()
   if not task:
     print("Empty task not allowed !")
     return
   
   if task in t_tasks:
     print("Task already exist !")
     entry1.delete(0, "end")
     return
   t_tasks.append(task)
   strg.save_tasks(t_tasks)
   list_tasks()
   entry1.delete(0, "end")

def delete_task():
  selected = listbox.curselection()
  if not selected:
    print("No task selected")
    return
  index = selected[0]
  t_tasks.pop(index)
  strg.save_tasks(t_tasks)
  list_tasks()



#------------------------------------------------------------

#buttons

btn_func = {
  "Add Task" : add_task,
  "Delete Task": delete_task,
  "Show Task" : list_tasks,
  
}
for i in range(len(btn_func)):
  frame.rowconfigure(i, weight=1)

for row, (text, func) in enumerate(btn_func.items()):
  btn = ctk.CTkButton(frame, text=text, command=func)
  btn.grid(row=row, column=0, sticky="ew", padx=5, pady=5)
  
       






window.mainloop()
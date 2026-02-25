
import os
import shutil
import customtkinter as ctk
import tkinter as tk
from tkinter import filedialog , messagebox
from PIL import Image as image
# import time
# from pathlib import Path as path
# from collections import Counter as counter
# import hashlib 
# import threading as thread


ctk.set_appearance_mode("light")
window = ctk.CTk()
window.title("Filerest - File Organizer")
window.geometry("600x600")
# window.resizable(False, False)

h_frame = ctk.CTkFrame(window, width=600, height=100, fg_color="lightgreen" )
h_frame.pack()
h_frame.pack_propagate(False)

logo = image.open("filerest.png")
logo = ctk.CTkImage(light_image=logo, size=(350, 250))
logo_lbl = ctk.CTkLabel(h_frame, image=logo, text="")
logo_lbl.place(rely=0.5, relx=0.5, anchor="center")

f_frame = ctk.CTkFrame(window, width=600, height=500, fg_color="#F7F4D5")
f_frame.pack()
f_frame.pack_propagate(False)

# btn_frame = ctk.CTkFrame(f_frame)
# btn_frame.grid(row=10, column=1, padx=2, pady=10, sticky="n")
# btn_frame.pack_propagate(False)
listbox = tk.Listbox(f_frame, height=9, width=35,)
listbox.pack()

class FileOrganizer:
    def __init__(self):
        self.source = ""
        self.destination = ""
    
    def set_source(self, path ):
        if os.path.isdir(path):
            self.source = path
            messagebox.showinfo("Source Set ", "Source folder has been set")
        else:
            messagebox.showerror("Invalid Folder", "Invalid Folder or Folder do not Exists")
    def set_destination(self, path):
        if os.path.isdir(path):
            self.destination = path 
            messagebox.showinfo("Destination Set", "Destination Folder Has been set ")
        else:
            messagebox.showerror("Destination not set", "Destination folder do not exists")
    def list_files(self):
        if self.source:
            files = os.listdir(self.source)
            for file in files :
                listbox.insert(tk.END, file)
        else:
            messagebox.showerror("Source not set", "Source do no exists or set")
            
            
    def move_all_files(self):
        if not self.source or not self.destination :
            messagebox.showerror("Error", "Set Folder first")
            return
        
        for file in os.listdir(self.source):
            src = os.path.join(self.source, file)
            dest = os.path.join(self.destination, file)
            
            if os.path.isfile(src):
                shutil.move(src, dest)
               
        messagebox.showinfo("File Moved Successfully", "Your existing file has been moved Sucessfully")
        
        
    def move_by_ext(self):
        if not self.source or not self.destination:
            messagebox.showerror("Error", "Set source and Destination")
            return
        extension_pop = ctk.CTkToplevel(window)
        extension_pop.title("Move By File Type")
        extension_pop.geometry("300x300")
        entry = ctk.CTkEntry(extension_pop, placeholder_text="Enter your file type" )
        entry.pack(pady=10)
       
     
        def start_move():
            type_input = entry.get().strip().lower()
            
            image_ext = (".jpeg", ".jpg", ".png", ".ico")
            doc_ext = (".txt", ".docx", ".word", ".py", ".html", ".js", ".css")
            vid_ext = (".mp4", ".mkv", "webm", "mpeg")
            aud_ext = (".mp3", ".wav", ".aac", ".m4a")
            moved = 0
            for file in os.listdir(self.source):
                src = os.path.join(self.source, file)
                dest = os.path.join(self.destination, file)  
                
             
            if type_input == "image" and file.endswith(image_ext):
                    shutil.move(src, dest)
                    moved += 1
                    listbox.insert(tk.END, f"{src} ➡️ {dest}")
                           
            elif type_input == "documents" and file.endswith(doc_ext):
                    shutil.move(src, dest)
                    moved += 1
                    
            elif type_input == "video" and file.endswith(vid_ext):
                    shutil.move(src, dest)
                    moved += 1
                    
            elif type_input == "image" and file.endswith(aud_ext):
                   shutil.move(src, dest)
                   moved +=1
                    
            messagebox.showinfo("Done", f"{moved} files moved")
            extension_pop.destroy()
        ctk.CTkButton(extension_pop, text="move", command=start_move).pack(pady=5)                
    
            
organizer = FileOrganizer()
def set_src():
    ask = filedialog.askdirectory()
    if ask:
     organizer.set_source(ask)
     listbox.insert(tk.END, f"source ➡️ {ask}")
     
def set_dest():
    ask = filedialog.askdirectory()
    # listbox.delete(0, tk.END)
    if ask:
     organizer.set_destination(ask)
     listbox.insert(tk.END, f"destination ➡️ {ask}")
     
def list_items():
    listbox.insert(tk.END, "------FILES-----")
    organizer.list_files()

    
def move_ext():
    organizer.move_by_ext()
    
def move_all():
    organizer.move_all_files()
    
def clear():
    listbox.delete(0, tk.END)

functions = {
    "Choose Source" : set_src,
    "Choose Dest" : set_dest,
    "List File" : list_items,
    "Move by ext" : move_ext,
    "Move all file" : move_all,
    "Clear" : clear
}
# for i in range (len(functions)):
#     btn_frame.columnconfigure(i, weight=1)

for col, (text, func) in enumerate(functions.items()):
    button = ctk.CTkButton(f_frame, text=text, command=func,)
    button.pack(pady=5) 
    
window.mainloop()
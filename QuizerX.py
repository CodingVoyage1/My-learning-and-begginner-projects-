"""
Docstring for QuizerX

So basically its quiz programme where you will get random questions and you have to answer them 
 
"""
import random as rnd
import customtkinter as ctk
from PIL import Image as img

window = ctk.CTk()
window.geometry("600x500")
window.title("QuizerX")

img1 = ctk.CTkImage(
    light_image=img.open("QuizerX.png"),
    dark_image=img.open("QuizerX.png"),
    size=(200, 100)
 )
label_img = ctk.CTkLabel(window, image=img1, text="")
label_img.pack(pady=15)

quizz= [
    ("Python me list ka syntax kaunsa hai?",
     ["{}", "()", "[]", "<>"], "[]"),

    ("Python me output kaise print karte hain?",
     ["echo()", "display()", "print()", "show()"], "print()"),

    ("x = 10, y = 5, x // y = ?",
     ["2", "2.0", "15", "Error"], "2"),

    ("Error handling ke liye kya use hota hai?",
     ["handle", "try-except", "error", "catch"], "try-except"),

    ("CustomTkinter ka button class kaunsa hai?",
     ["Button", "tk.Button", "CTkButton", "ModernButton"], "CTkButton")
]




txt_box =ctk.CTkTextbox(window, width=350, height=160, wrap = "word")
txt_box.pack( pady=15)
txt_box.configure(state="disabled")
entry = ctk.CTkEntry(window, placeholder_text="1,2,3,4...", font=("Arial", 14))
entry.pack(pady=5)
current_answer = ""
current_options = []
def show():
  global current_answer, current_options
  q, options , a = rnd.choice(quizz)
  current_answer = a
  current_options = options

  txt_box.configure(state = "normal")
  txt_box.delete("1.0", "end")
  txt_box.insert("end", f"Question :\n{q}\n\nOptions:\n ")
  for i, opt in enumerate(options, start=1):
    txt_box.insert("end",f"{i}.{opt}\n" )
def ans():
  txt_box.configure(state="normal")
  txt_box.delete("1.0", "end")
  txt_box.insert("end", f"Answers: {current_answer}")
  

def etr_ans():

  try:
    inpt = int(entry.get())
  except ValueError:
    txt_box.configure(state="normal")
    txt_box.delete("1.0", "end")
    txt_box.insert("end", "Please enter valid options !")
    txt_box.configure(state="disabled")
    return

  if inpt < 1 or inpt > len(current_options):
    txt_box.configure(state="normal")
    txt_box.delete("1.0", "end")
    txt_box.insert("end", "Options number out of range !")
    txt_box.configure(state="disabled")
    return
  
  selected_options = current_options[inpt - 1]

  txt_box.configure(state="normal")
  txt_box.delete("1.0", "end")
 
  if selected_options == current_answer:
    txt_box.insert("end", "Correct answer !")
  else:
    txt_box.insert("end", f"Wrong Answer \n Correct answer : {current_answer}")
  
  txt_box.configure(state = "disabled")
  entry.delete(0, "end")


ctk.CTkButton(window, text="Next", command=show).pack(pady= 2)
ctk.CTkButton(window , text="show answer", command=ans,).pack()
ctk.CTkButton(window, text="Enter", command=etr_ans).pack(pady=2)

window.mainloop()
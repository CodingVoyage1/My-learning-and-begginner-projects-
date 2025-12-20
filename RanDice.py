"""
Docstring for RanDice

RanDice is programme which is can be used to generate random password
And you can increase your password just by entering the length of password
You want.

"""

import random as rnd 
import string as strn
import tkinter as tk
from PIL import Image, ImageTk

window = tk.Tk()
window.configure(bg="lightblue")
window.geometry("500x350")
window.title("RanDice")
img = Image.open("RanDice.png")
img = img.resize((200, 100))
photo = ImageTk.PhotoImage(img)
imglb = tk.Label(window, image=photo)
imglb.image = photo
imglb.pack(pady=5)
p_label = tk.Label(window, text="Enter Password Length ", bg="lightblue", font=("Arial", 10))
p_label.pack()
p_len = tk.Entry(window, font=("Arial", 12), width=5)
p_len.pack(pady=5)
text = tk.Text(window, height=2, width=30)
text.pack()
frame = tk.Frame(window, bg="lightblue")
frame.place(relx=0.5, rely=0.70, anchor="center")
def generate():
    alpha1 = strn.ascii_lowercase
    alpha2 = strn.ascii_uppercase
    num = strn.digits
    alpha3 = strn.punctuation
    try:

         input1 = int(p_len.get())

    except  ValueError:
          text.insert(tk.END, "Please Enter valid number \n")
          return
    s = []
    s.extend(alpha1)
    s.extend(alpha2)
    s.extend(alpha3)
    s.extend(num)
    if input1 > len(s):
       text.insert(tk.END, "Your password is too long \n")  
       return
    password = ''.join(rnd.sample(s, input1))
    text.config(state="normal")
    text.delete("1.0", tk.END)
    text.insert(tk.END, f"Your password is : {password}\n")
    text.config(state="disabled")
def clear():
    text.config(state="normal")
    text.delete("1.0", tk.END)
    text.config(state="disabled")

function = {
    "Generate" :{"cmd" : generate, "bg" : "green", "fg": "white"},
    "Clear" : {"cmd" : clear, "bg": "red", "fg": "white" }
}

for i in range(len(function)):
    frame.columnconfigure(i, weight=1)

for col, (btn_text, data) in enumerate(function.items()):
    btn = tk.Button(frame, text=btn_text, command=data["cmd"], width=10 ,
                     bg=data["bg"],
                     fg=data["fg"])
    btn.grid(row=0, column=col, sticky="ew", padx=10, pady=10)

window.mainloop()
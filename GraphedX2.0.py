"""
Docstring for GraphedX2.0

This one is upgraded version of my previous project GraphedX project
where i have created a simple programme
where you can create a graph just by providing information you want 
but this one is upgraded version , i will create this programme using tkinter programme and make it looks 
little bit awesome than before , I hope you like it.

"""

import tkinter as tk 
import matplotlib.pyplot as plt
from tkinter import messagebox as msg
from PIL import Image, ImageTk


window = tk.Tk()
window.resizable(False, False)
window.configure(bg="Lightgreen")
window.geometry("500x400")
window.title("GraphedX2.0")
img = Image.open("GraphedX2.0.png")
img = img.resize((200, 70))
photo = ImageTk.PhotoImage(img)
imglb = tk.Label(window, image=photo)
imglb.image = photo
imglb.pack(pady=5)

frame = tk.Frame(window, bg="lightgreen")
frame.place(relx=0.5, rely=0.60, anchor="center",)


#label.pack()
#label2.pack()
label1 = tk.Label(window, text="Enter your X data:", font=("Arial", 14), bg="lightgreen")
label1.pack(pady="5")
input1 = ( tk.Entry(window, font=("Arial", 13)))
input1.pack() 
label2 = tk.Label(window, text="Enter your Y data :" , font=("Arial", 14), bg="lightgreen").pack(pady="5")
input2 = (tk.Entry(window, font=("Arial", 13)))
input2.pack()
def histo(): 
	entry1 = list(map(int,input1.get().split()))
	entry2 = list(map(int, input2.get().split()))
	if not entry2:
		plt.hist(entry1)
		plt.show()
	elif not entry1 or not entry2:
		msg.showinfo("Info", "Please enter the value first ")

	else:
		msg.showinfo("Info", "Histogram requires only X data  ")
def bar():
	entry1 = list(map(int, input1.get().split()))
	entry2 = list(map(int, input2.get().split()))
	if not entry1 or not entry2:
		msg.showinfo("Notice", "please enter the value first")
	else:
		plt.bar(entry1, entry2)
		plt.show()
	
def scatter():
	entry1 = list(map(int,input1.get().split()))
	entry2 = list(map(int, input2.get().split()))
	if not entry1 or not entry2 :
		msg.showinfo("Info", "Please enter the value first")
	else:
		plt.scatter(entry1, entry2)
		plt.show()

def plane():
	entry1 = list(map(int,input1.get().split()))
	entry2 = list(map(int, input2.get().split()))
	if not entry1 or not entry2:
		msg.showinfo("info", "Please enter the value first")
	else:
		plt.plot(entry1, entry2)
		plt.show()
	    	
def pie():
	window2 = tk.Tk()
	window2.geometry("400x300")
	window2.title("Pie graph maker ")

	tk.Label(window2, text="Enter the name of your data :", font=("Arial", 12)).pack()
	data_name = tk.Entry(window2, font=("Arial", 10))
	data_name.pack(pady="5")
	tk.Label(window2, text="Enter your data label :", font=("Arial", 12)).pack()
	pie_ent = tk.Entry(window2, font=("Arial", 10))
	pie_ent.pack(pady="5")
	tk.Label(window2, text="Enter your data in numbers :", font=("Arial", 12)).pack()
	pie_ent2 = tk.Entry(window2, font=("Arial", 10))
	pie_ent2.pack(pady="5")
	
	def create():
	
		data_name1 = data_name.get()
		label = pie_ent.get().split()
		data = list(map(int, pie_ent2.get().split()))
		if len(label) != len(data):
			msg.showinfo("Notice", "lenght of data and label should be equal ")
		
		plt.pie(data , labels=label, autopct='%1.1f%%')
		plt.title(data_name1)
		plt.show()
	
	btn_create = tk.Button(window2, text="Create Pie", command=create).pack()
	window2.mainloop()

actions ={
	"Histogram" : histo,
	"Bar" : bar,
	"Scatter": scatter,
	"line": plane,
	"Pie": pie
} 

for i in range(len(actions)):
	frame.columnconfigure(i, weight=1)

for col, (text, func) in enumerate(actions.items()):
    btn = tk.Button(frame, text=text, command=func, width=10,)
    btn.grid(row=0, column=col, sticky="ew", padx=10, pady=10)
	
window.mainloop()

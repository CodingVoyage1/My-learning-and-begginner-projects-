"""
Docstring for calculatorUsingTkinter

i have made this calculator using Tkinter and learned a lot of new things about GUI of python , will learn more and add some awesome features in upcoming commits 

"""



import tkinter as tk

window = tk.Tk()
window.geometry("400x300")
window.title("Simple Calculator")
window.configure(bg="lightblue")
window.resizable(False, False)

tk.Label(window, text="Number 1:", font=("Arial", 12)).pack(pady='5')
entry1 = tk.Entry(window, font=("Arial", 14))
entry1.pack()  

tk.Label(window, text="Number 2 :", font=("Arial", 12)).pack(pady="5")
entry2 = tk.Entry(window, font=("Arial", 14))
entry2.pack()

result_label = tk.Label(window, text="Result", font=("Arial", 14, "bold"))
result_label.pack()

def add_sum():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        result = num1 + num2
        result_label.config(text=f"Result: {result}")
    except ValueError:
        result_label.config(text="Please enter valid numbers")

def sub_sum():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        result2 = num1 - num2
        result_label.config(text=f"Result : {result2}")
    except ValueError:
        result_label.config(text="Invalid Operator")

def mul_sum():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        result3 = num1 * num2
        result_label.config(text=f"Result : {result3}")

    except ValueError:
        result_label.config(text="Invalid Operator")
    
def divide():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        result4 = num1 / num2 
        result_label.config(text=f"Result : {result4}")
    
    except ValueError:
        result_label.config(text="Invalid Operator")


tk.Button(window, text="Sub", command=sub_sum, bg="lightgreen", fg="black").place(relx=0.5, rely=0.6, anchor="center")
tk.Button(window, text="Add", command=add_sum, bg="lightgreen", fg="black" ).place(relx=0.5 , rely=0.8, anchor="center")
tk.Button(window, text= "Multiply", command=mul_sum, bg="lightgreen", fg="black").place(relx=0.8, rely=0.7 , anchor="e")
tk.Button(window, text="divide", command=divide, bg="lightgreen", fg="black").place(relx=0.2, rely=0.7, anchor="w")

window.mainloop()
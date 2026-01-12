"""
Docstring for BMIcalc

This is a simple BMI calculator with GUI .. LETS MAKE IT ! 
"""
import customtkinter as ctk
from PIL import Image as img


window = ctk.CTk()
window.geometry("450x400")
window.resizable(False,False)
window.title("BMIcalcX")
logo = img.open("BMIcalcX.png")
logo = ctk.CTkImage(light_image=logo, size=(140, 140))
logo_lbl = ctk.CTkLabel(window, image=logo)
logo_lbl.pack(pady=10)



#frame = ctk.CTkFrame(window, bg_color="blue", width=50, height=50)
#frame.place(rely=0.2, relx=0.1 , anchor ="center")

age = ctk.CTkEntry(window, placeholder_text="Enter your age ", width=200)
age.pack(pady=5)
wt_ent = ctk.CTkEntry(window, placeholder_text="Enter your weight(kg)", width=200)
wt_ent.pack(pady=5)
ht_ent = ctk.CTkEntry(window, placeholder_text="Enter your height(cm)", width=200)
ht_ent.pack(pady=5)
result_label = ctk.CTkLabel(window, text="", font=("Arial", 14))
result_label.pack(pady=10)
label_m = ctk.CTkLabel(window, text="", font=("Arial", 14))
label_m.pack()


def calc():
    weight = float(wt_ent.get())
    height = float(ht_ent.get())/100

    bmi = weight/(height**2)
    result_label.configure(text = f"Your BMI is : {bmi:.2f}")

    if bmi < 16:
        label_m.configure(text="You are underweight !")
    elif bmi > 16 and bmi < 17:
        label_m.configure(text="Moderate weight !")
    elif bmi > 17 and bmi < 18.5:
        label_m.configure(text="Mild weight ")
    elif bmi > 18.5 and bmi < 25 :
        label_m.configure(text="Normal weight (Healthy)")
    elif bmi > 25 :
        label_m.configure(text="Your are overweight ")
    else:
        label_m.configure(text="Please Enter valid input ")

age.bind("<Return>", lambda _ : wt_ent.focus_set())   
wt_ent.bind("<Return>", lambda _ : ht_ent.focus_set())
ht_ent.bind("<Return>", lambda _ : calc())
btn = ctk.CTkButton(window, command=calc, text="calculate")
btn.pack()        


window.mainloop()



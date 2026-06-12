import customtkinter as ctk
from tkinter import messagebox as mbox
from encrypt import encrypt_text
from Decrypt import decrypt_text


window = ctk.CTk()
window.title("GlyphNet v0.1")
window.geometry("600x600")
h_frame = ctk.CTkFrame(window, height=80, width=300, corner_radius=50,fg_color="lightgreen")
h_frame.pack(pady=10)
h_frame.pack_propagate(False)
h_label = ctk.CTkLabel(h_frame, text="GlyphNet v0.1", text_color="grey", font=("Arial", 20),)
h_label.pack(expand=True)
info_label = ctk.CTkLabel(window, text="Enter your text : ", font=("Arial",15))
info_label.pack(pady=0)
textbox = ctk.CTkTextbox(window, width=300, height=100, )
textbox.pack(pady=20)


def encrypt_message():
    user_text = textbox.get("1.0", "end").strip()

    encrypted = encrypt_text(user_text)
    output_box.delete("1.0", "end")
    output_box.insert("1.0", encrypted)

info_label2 = ctk.CTkLabel(window, text="Output :", font=("Arial", 15))
info_label2.pack(pady=0)
output_box = ctk.CTkTextbox(window, width=300, height=100)
output_box.pack(pady=20)

btn = ctk.CTkButton(window, text="Encrypt", command=encrypt_message)
btn.place(relx=0.37, rely=0.8, anchor="center")

def decrypt_message():
    encrypted_text = textbox.get("1.0", "end").strip()

    decrypted = decrypt_text(encrypted_text)

    output_box.delete("1.0", "end")
    output_box.insert("1.0", decrypted)

btn2 = ctk.CTkButton(window, text="Decrypt", command=decrypt_message)
btn2.place(relx=0.66, rely=0.8, anchor="center")
window.mainloop()

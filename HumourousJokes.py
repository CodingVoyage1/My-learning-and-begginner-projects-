"""
Docstring for HumourousJokes


"""
import tkinter as tk
import requests
#from googletrans import Translator



window = tk.Tk()
window.title("😂HumourousJokes😂")
window.configure(bg="lightyellow")
window.geometry("400x500")



ta_frame = tk.Frame(window, width=250, height=250,bg="white" )
ta_frame.pack(expand=True, pady=0, fill="both")
ta_frame.pack_propagate(True)
h_frame = tk.Frame(ta_frame, width=400, height=50, bg="#FFC608" ,)
h_frame.pack(pady=0)
h_frame.pack_propagate(False)
h_label = tk.Label(h_frame, text="😂HumorousJokes😂", font=("Segoe UI", 15,"bold"), bg="#FFC608")
h_label.pack(pady=5)
joke_frame = tk.Frame(ta_frame, width=320, height=300, bg="#FFDC9E")
joke_frame.pack(pady=10)
joke_frame.pack_propagate(False)
jokes_label = tk.Label(joke_frame, text="click button to get joke 😂", font=("Century Gothic", 15), justify="center", bg="#FFDC9E", wraplength=290)
jokes_label.pack(pady=20)




def get_jokes():

  jokesapi = "https://official-joke-api.appspot.com/random_joke"
 
  try :
    response = requests.get(jokesapi, timeout=1)
 

    if response.status_code == 200:
      data = response.json()
      jokes_label.config(text=f"{data["setup"]}\n\n{data["punchline"]}\n😂😜")
    else:
      jokes_label.config(text="❌ API error ❌")
  except requests.exceptions.RequestException:
    jokes_label.config(text="❌ Internet problem")


nxt_btn = tk.Button(ta_frame, bg="#FFE626", text="Next Joke 😂", command=get_jokes, font=("Arial",12), activebackground="#FFE626", relief="flat")
nxt_btn.pack(pady=20)
footer = tk.Label(ta_frame, font=("Segoe UI",8), text="😊 Made by me in Python ❤️", fg="black", bg="white")
footer.pack(pady=10)  

window.mainloop()
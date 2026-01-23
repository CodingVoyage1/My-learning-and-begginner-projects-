import requests
import customtkinter as ctk
from PIL import Image as img


ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")

window = ctk.CTk()
window.geometry("500x500")
window.title("Poekdex 📱")
pokedex = img.open("pokedex.png")
pokedex = ctk.CTkImage(light_image=pokedex, size=(180,100))
pokeball = img.open("pokeball.png")
pokeball = ctk.CTkImage(light_image=pokeball, size=(90, 90))
pokeball2 = img.open("pokeball.png")
pokeball2 = ctk.CTkImage(light_image=pokeball2, size=(90, 90))
h_frame = ctk.CTkFrame(
  window,
  width=500,
  height=100,
  fg_color="#FFCC00",
  corner_radius=30,
  border_width=4,
  border_color="gray"
)
h_frame.pack(pady=10)
h_frame.pack_propagate(False)

info_frame = ctk.CTkFrame(
  window, 
  width=250, 
  height=200, 
  fg_color="#FF7966", 
  corner_radius=20,
  border_width=4,
  border_color=("gray","yellow")
)
info_frame.pack(padx=20, pady=20)
info_frame.pack_propagate(False)
poke_head = ctk.CTkLabel(info_frame, text="Pokemon Data", font=("Segoe UI", 18, "bold"))
poke_head.pack(pady=10)

pokeball_lbl2 = ctk.CTkLabel(h_frame, image=pokeball2,text="" )
pokeball_lbl2.place(rely=0.5,relx=0.95, anchor = "e")
pokedex_lbl = ctk.CTkLabel(h_frame, image=pokedex, text="")
pokedex_lbl.pack()
pokeball_lbl = ctk.CTkLabel(h_frame, image=pokeball,text="" )
pokeball_lbl.place(rely=0.5,relx=0.25, anchor = "e")
pkm_name = ctk.CTkEntry(
  window,
  placeholder_text="Enter your fav pokemon 😊", 
  width=200
)
pkm_name.pack(pady=10)
poke_data = ctk.CTkLabel(info_frame, font=("Century Gothic", 12,"bold"), text="")
poke_data.pack()




def get_poekemon_info(pokemon):
  
  pokeapi = "https://pokeapi.co/api/v2/"
  
  data = f"{pokeapi}/pokemon/{pokemon}"
  response = requests.get(data)

  if response.status_code == 200:
     res = response.json()
     return res

  else:
     poke_data.configure(text="data not found")
     return None



def fetch_and_show():
   pokemon = pkm_name.get().strip()
   if not pokemon:
      poke_data.configure(text="Please enter the name of pokemon 😊")
      return
   info = get_poekemon_info(pokemon)

   if info:
      poke_data.configure(text=f"""
Name : {info['name'].title()}
ID : {info['id']}
Height : {info['height']/10 }m
Weight : {info['weight']/10 }kg
Type : {info["types"][0]["type"]["name"]}

""")
  

pkm_name.bind("<Return>", lambda _: fetch_and_show())
button = ctk.CTkButton(window, text="Get Data", command=fetch_and_show, fg_color="blue", corner_radius=20)  
button.pack(pady=10)


window.mainloop()
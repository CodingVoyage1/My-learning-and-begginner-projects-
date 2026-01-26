"""
Docstring for YuvuDownloader
This is just a simple youtube downloader in GUI 
"""
import customtkinter as ctk
from PIL import Image, ImageDraw
from pytubefix import YouTube as youtube 
from tkinter import filedialog
import threading

ctk.set_appearance_mode("light")
window = ctk.CTk()
window.title("Yuvu Downloader ⬇️")
window.geometry("500x500")
img = Image.open("yuvu_logo.png").convert("RGBA")
w, h = img.size
s = min(w, h)
left = (w - s) // 2
top = (h - s) // 2
image = img.crop((left, top, left + s, top + s))

mask = Image.new("L", (s, s), 0)
draw = ImageDraw.Draw(mask)
draw.ellipse((0, 0, s, s), fill=255)
img.putalpha(mask)

logo = ctk.CTkImage(light_image=img, size=(100, 100))

h_frame = ctk.CTkFrame(window, fg_color="#6951FC", width=490, height=100, corner_radius=30, border_width=2, border_color="black")
h_frame.pack(pady=5)
h_frame.pack_propagate(False)
circle_frame = ctk.CTkFrame(h_frame, width=100,height=100, fg_color="#6951FC", corner_radius=50, border_width=2, border_color="blue")
circle_frame.pack()
circle_frame.pack_propagate(False)
logo_lb = ctk.CTkLabel(circle_frame,image=logo , text="")
logo_lb.pack()

tittle = ctk.CTkLabel(h_frame, text="YUVU", font=("Segoe UI", 30, "bold"), fg_color="#6951FC", )
tittle.place(rely=0.5, relx=0.1, anchor="w")
title2 = ctk.CTkLabel(h_frame, text="DOWNLOADER", font=("Segoe UI",23, "bold"),fg_color="#6951FC")
title2.place(rely=0.5, relx=0.98, anchor="e" )


download_frame2 = ctk.CTkFrame(window, fg_color="#058DAB", width=450, height=400, corner_radius=10, border_color="black", border_width=2)
download_frame2.pack(pady=10)
download_frame2.pack_propagate(False)
download_frame = ctk.CTkFrame(download_frame2, width=400 , height=50, fg_color="lightblue", corner_radius=20, border_width=2, border_color="black")
download_frame.place(rely=0.2,relx=0.5, anchor="center")
download_frame.pack_propagate(False)

entry = ctk.CTkEntry(download_frame, placeholder_text="Enter or Paste your URl...", font=("Sageo UI", 12), width=200)
entry.pack(pady=10)
progress = ctk.CTkProgressBar(download_frame2, width=200,)
progress.place(rely=0.5, relx=0.5, anchor="center")
progress.set(0)
label = ctk.CTkLabel(download_frame2, text="0%")
label.place(rely=0.5, relx=0.5, anchor="center")

def on_progress(streams, chunk, bytes_remaining):
    total = streams.filesize
    downloaded = total - bytes_remaining
    percent = downloaded / total

    progress.set(percent)
    label.configure(text=f"{int(percent * 100)}%")

def download_video():
    yt = youtube(entry.get(), on_progress_callback=on_progress)
    stream = yt.streams.get_highest_resolution()
    folder = filedialog.askdirectory()
    stream.download(output_path=folder)
    label.configure(text="Download Complete ")
  

def start_download():
    threading.Thread(target=download_video, daemon=True).start()
    label.configure(text="wait for a while...")

button = ctk.CTkButton(window, text="Download", command=start_download, fg_color="#F50559", font=("Arial",12 ))
button.place(rely=0.7, relx=0.5, anchor="center")

window.mainloop()

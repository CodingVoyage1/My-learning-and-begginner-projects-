import socket
import threading
from Decrypt import decrypt_text


client = socket.socket()
client.connect(("127.0.0.1", 5000))

def recv():
    while True:
        message = client.recv(1024).decode()
        enc = decrypt_text(message)
        print(enc)
thread = threading.Thread(target=recv)
thread.start()

username = input("Enter username :")
while True:

    msg = input("")
    full_msg = f"{username} : \n{msg}"
    client.send(full_msg.encode())

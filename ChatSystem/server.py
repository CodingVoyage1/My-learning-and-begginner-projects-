import socket
import threading
from Decrypt import decrypt_text

server = socket.socket()
server.bind(("127.0.0.1", 5000))

server.listen()

print("Listening on 127.0.0.1 : 5000")

clients, address = server.accept()

print("Connected ", address)

def worker():
    while True:
        message = clients.recv(1024).decode()
        decrypted = decrypt_text(message)
        if not message:
            break
        print(decrypted)
thread = threading.Thread(target=worker)
thread.start()

username = input("Enter username :")
while True:

    msg = input("")
    full_msg = f"{username} : \n{msg}"
    clients.send(full_msg.encode())
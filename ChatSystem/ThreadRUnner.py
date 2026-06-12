import threading
import time

def worker():
    while True:
        print("Working..")
        time.sleep(1)

thread = threading.Thread(target=worker)
thread.start()

while True:
    message = input("Type something :")
    print(message)

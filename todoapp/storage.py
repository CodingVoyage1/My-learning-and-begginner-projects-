"""
Docstring for storage
its storage for habitaX programme this file will be used as storage where i can add/delete/upgrade tasks >....
"""

FILE_NAME = "tasks.txt"

def load_tasks():
    tasks = []

    try:
        with open(FILE_NAME, "r") as f:
           for line in f:
               tasks.append(line.strip())
 
    except FileNotFoundError:
        pass
    return tasks
def save_tasks(task):
    with open(FILE_NAME, "w") as f:
        for task in task:
            f.write(task + "\n")


"""
Docstring for habitaX

so its a todolist programe with file handeling included which can save your 
list and works in file so that after closing the programe it will still be saved 
, SO LETS MAKE IT !....

"""

t_tasks = []
print("--------OPTIONS----------")
print(""
        "'q' to quit \n"
        "'d' to delete\n"
        "'s' to see tasks\n"
        "'u' to upgrade your task")
print("-------------------------")
while True:

    input1 = input("Enter your task :")
    

    if input1.lower() == "q":
        print("Thanks for using the programme!")
        break
    elif input1.lower() == "d":
        del_t = input("Enter the name to delete : ").strip().lower()
        if del_t in t_tasks:
           t_tasks.remove(del_t)
           print(f"{del_t} is deleted !")

        else:
          print("Task is not found !")  
    elif input1.lower() == "u":
        u_ts = input("Enter the name of task to upgrade :").lower()
        new = input("Enter the name of upgraded task :").lower()
        if u_ts in t_tasks:
         ind = t_tasks.index(u_ts)
         t_tasks[ind] = new
         print(f"{u_ts} is upgraded to {new}")
        else:
           print("Task not found !")
    elif input1.lower() == "s":
        print("------Total Tasks-----")
        for i, task in enumerate(t_tasks, start=1):
           
           print(f"{i}.{task}")

        print("----------------------")
    elif input1.lower() == "":
       print("Empty task is not allowed !")

    else:
        t_tasks.append(input1.lower())
        
        print(f"'{input1}' is added")
        
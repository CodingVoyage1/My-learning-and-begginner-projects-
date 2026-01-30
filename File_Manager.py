import os
import shutil
import logging


logging.basicConfig(
   filename="programme.log",
   level=logging.INFO,
   format="%(asctime)s | %(filename)s | %(message)s "
)


def creating_folder():
    folder_name = input("Enter the name of the folder:")
    try:
      
      if os.path.exists(folder_name):
         print(f"{folder_name} is already exist...")
         logging.info(f"Folder exixts : {folder_name} ")
      else:
        os.mkdir(folder_name)
        print(f"{folder_name} is created ...")
        logging.info(f"Folder created : {folder_name}")
    except PermissionError:
        print('File was not created due to permision error...')
        logging.error(f"File was not create due to error : Permission Error ")

     

def creating_file():
   file_name = input("Enter the name of the file :")
   file_content = input("Enter the text to save in file :")
   try:

      if os.path.isfile(file_name):
        print("file is already exist ..")
        logging.info(f"File exists : {file_name}")
      else:
            with open(file_name, "w") as f:
              f.write(file_content)
   except PermissionError:
     print("file was not created..")
     logging.error("File was not created due to error : Permission Error ")

def moving_file():
   file = input("Enter the name of the file to move:")
   folder_n = input("Enter the name of the folder :")
   if not os.path.isfile(file):
      print("File is not present..")
      logging.info(f"Given file is not present : {file}")
   elif not os.path.isdir(folder_n):
      print("Folder is not present")
      logging.info(f"Given folder is not present : {folder_n} ")
   else:
     shutil.move(file, folder_n)
     print(f"{file} is successfuly moved to {folder_n}...")
     logging.info(f"File is moved : {file}  -- {folder_n}")

  
def list_file():
   folder = input("Enter the name of the folder to check files :")

   if os.path.isdir(folder):
      print("---------FILES---------")
      logging.info(f"File listed of folder : {folder}")
      path = os.listdir(folder)
      for files in path:
         print(files)
   else:
      print("Folder is not present..")
      logging.info(f"No file present in selected folder: {folder}")

def delete_item():
   delete = int(input("\nChoose to delete"
   " \n1.File"
   " \n2.Folder :"))
   if delete == 1:
      p_folder = input("Enter the name of the file folder :")
      d_file = input("Enter the name of the file to delete :") 
      folder_path = os.path.abspath(p_folder)
      file_path = os.path.join(folder_path, d_file)

      print("deleting", file_path)

      if not os.path.isdir(folder_path):
         print(f"{folder_path} do not exists")
         logging.error(f"Folder not exists : {folder_path}")
         return
      if not os.path.isfile(file_path):
         print("File does not exist at this location")
         logging.error(f"File not exist in location : {file_path}")
         return
   
      try:
         os.remove(file_path)#remember that os.remove() needs absolute path >>> system/things/things/things ...etc
         print(f"{file_path} was removed succesfully")
         logging.info(f"file deleted : {file_path}")
      except Exception as d :
         print("File was not deleted due to error ")
         logging.error(f"File was not deleted due to error : {d}")
      
   elif delete == 2:
      d_folder =input("Enter the name of the folder to delete :")
      if os.path.isdir(d_folder):      
        try:
          shutil.rmtree(d_folder)
          print(f"{d_folder} was deleted successfull")
          logging.info(f"folder deleted : {d_folder}")
        except Exception as e:
          print("Folder was not deleted due to error")
          logging.error(f"Folder not deleted due to error : {e}")
      else:
         print("Folder not exists ")
         logging.info(f"folder not exist : {d_folder}")
 

def menu():
   print("\n-------choose your options--------")
   print("1.Create Folder")   
   print("2.Create File")
   print("3.Move File")
   print("4.List files")
   print("5.Delete(file or folder)")
   print("6.Exit")
  

while True:
   menu()
   option = int(input("Enter the option (1-6) :"))
   if option == 1:
      creating_folder()
   elif option == 2:
      creating_file()
   elif option == 3:
      moving_file()
   elif option == 4:
      list_file()
   elif option == 5:
      delete_item()
   elif option == 6:
      print("Thanks for using the programme ")
      logging.info("Program closed ")
      break
  
menu()     
    

   


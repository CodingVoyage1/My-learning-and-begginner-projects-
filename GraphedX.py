#GraphedX programme 

"""
Docstring for GraphedX
 This is programme where you can create a plotted graph just by providing some inputs about the information you want.
 I hope this programme will be completed as i structured or planned . LETS DO IT !

 Will later make it more awesome using tkinter > THANK YOU !
"""
import matplotlib.pyplot as plt


g_type = input("Choose your Graph type (histogram,scatter,pie,bar) :").lower().strip()
data_name = input("Enter the name of your data :").strip()

if g_type in ["line", "scatter","bar"]:
   x_data = list(map(int,input("Enter your x data :").split()))
   y_data = list(map(int,input("Enter your y data :").split()))


if g_type == "scatter":
     plt.scatter(x_data, y_data)
  
elif g_type == "histogram" :
     hist_data = list(map(int, input("Enter your data :").split()))
     plt.hist(hist_data)
    
elif g_type == "bar":
      plt.bar(x_data, y_data)
      
elif g_type == "pie":    
      labels = input("Provide Your label :").split()
      data = list(map(int, input("Enter your data :").split()))
      plt.pie(data , labels=labels, autopct='%1.1f%%')
     
elif g_type == "line":
      plt.plot(x_data, y_data)
else :
      print("Please provide valid inputs ")
      exit()
plt.title(data_name)
plt.show()


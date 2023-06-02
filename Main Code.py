#Tingoyang'ana Kanjadza Lab 10



import tkinter


from tkinter import *

# Question 1
root = Tk()
root.title("Millilitre Conversion")
root.minsize(400,300)
Enter = Entry()
def tspoon():
    num = int(Enter.get())
    tspoon = num * 0.2029
    result.config(text = "teaspoons = " + str(tspoon))
def tabspoon():
    num = int(Enter.get())
    tabspoon = num * 0.0676
    result.config(text = "tablespoons = " + str(tabspoon))
def ouncs():
    num = int(Enter.get())
    ouncs = num * 0.0338
    result.config(text = "Ounces = " + str(ouncs))
def Quit():
    root.destroy()

Enter_metres = Label(root,text = "Enter Millilitres",fg="red")
chose_speed = Label(root,text = "Choose a volume:", fg="green")
Kilo_Button = Button(root,text = "teaspoons",command=tspoon)
miles_button = Button(root,text = "tablespoons",command=tabspoon)
feet_button = Button(root,text = "ounces",command=ouncs)
quit_button = Button(root,text = "Quit",command=Quit)
result = Label(root,text = "Result =")




Enter_metres.place(x=0,y=20)
Enter.place(x=160,y=20)
chose_speed.place(x=0,y=40)
Kilo_Button.place(x=0,y=80)
miles_button.place(x=120,y=80)
feet_button.place(x=220,y=80)
result.place(x=0,y=120)
quit_button.place(x=0,y=200)
root.mainloop()

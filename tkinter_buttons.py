


from tkinter import *
from tkinter import messagebox

def function1():
    messagebox.showinfo("general message","black colour !!")
def function2():
    messagebox.showinfo("general message","red colour !!")
def function3():
    messagebox.showinfo("general message","blue colour !!")
def function4():
    messagebox.showinfo("general message","green colour !!")

top = Tk()
top.geometry("400x600")
top.title("My First GUI")



b1 = Button(top,bg="black",text = "confirm",fg = "white",activebackground="grey",activeforeground="white",command=function1)
b2 = Button(top,bg="red",text = "confirm",fg = "white",activebackground="grey",activeforeground="white",command=function2)
b3 = Button(top,bg="blue",text = "confirm",fg = "white",activebackground="grey",activeforeground="white",command=function3)
b4 = Button(top,bg="green",text = "confirm",fg = "white",activebackground="grey",activeforeground="white",command=function4)

b1.pack(side = LEFT)
b2.pack(side = RIGHT)
b3.pack(side = TOP)
b4.pack(side = BOTTOM)


top.mainloop()

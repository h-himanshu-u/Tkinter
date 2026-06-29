
from tkinter import *

top = Tk()
top.geometry("500x200")
top.title("tk")

def select1() :
    string = "your selected value is" + str(r1.get())
    lable2.config(text = string)

lable1 =  Label(top,text = " Faviurite programming language ")
lable1.pack()

r1 = StringVar()

radio1 = Radiobutton(top,text = " c ",variable = r1,value = " c ",command = select1)
radio2 = Radiobutton(top,text = " c++ ",variable = r1,value = " c++ ",command = select1)
radio3 = Radiobutton(top,text = " java ",variable = r1,value = " java ",command = select1)

radio1.place(x=10,y=50)
radio2.place(x=10,y=70)
radio3.place(x=10,y=90)

lable2 = Label(top)
lable2.place(x=180,y=150)


top.mainloop()
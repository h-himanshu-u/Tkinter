
from tkinter import *

top = Tk()
top.geometry("500x500")
top.title("tk")


def select1() :
    sel = " value is " + str(scale.get())
    lable.config(text = sel )


scale = IntVar()
sc = Scale(top,variable= scale,from_ = 0,to = 15,orient = HORIZONTAL)
sc.pack()

but = Button(top,text = "value",command = select1,height = "1",width = "4")
but.pack()

lable = Label(top)
lable.pack()

top.mainloop()
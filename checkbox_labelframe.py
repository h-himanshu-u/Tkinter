
from tkinter import *

top = Tk()
top.geometry("600x600")
top.title("tk1")

def select1() :
    top1 = Toplevel(top)
    top1.geometry("400x400")
    top1.title("tk2")
    lb11 = LabelFrame(top1,height = "500",width = "500",bg="light green",text = "main settings")
    lb11.pack()


    r1 = IntVar()
    r2 = IntVar()
    r3 = IntVar()
    radio1 = Checkbutton(lb11,text = " c ",variable = r1,onvalue =  1,offvalue=0,height ="2",width = "50")
    radio2 = Checkbutton(lb11,text = " c++ ",variable = r2,onvalue =  1,offvalue=0,height ="2",width = "50")
    radio3 = Checkbutton(lb11,text = " java ",variable = r3,onvalue =  1,offvalue=0,height ="2",width = "50")

    radio1.pack()
    radio2.pack()
    radio3.pack()

    top1.mainloop()



lb = LabelFrame(top,height = "300",width = "400",text = "personal information")
lb.pack()

lab = Label(lb,text = "first name")
lab.pack(side = LEFT)
ent = Entry(lb)
ent.pack(side = LEFT)

lab = Label(lb,text = "last name")
lab.pack(side = LEFT)
ent = Entry(lb)
ent.pack(side = LEFT)


lb1 = LabelFrame(top,height = "300",width = "400",text = "address")
lb1.pack()

lab = Label(lb1,text = "country")
lab.pack(side = LEFT)
ent = Entry(lb1)
ent.pack(side = LEFT)

lab = Label(lb1,text = "state")
lab.pack(side = BOTTOM)
ent = Entry(lb1)
ent.pack(side = BOTTOM)





bt = Button(top,text = "submit",bg = "blue",fg = "white",command = select1)
bt.pack(side= BOTTOM)

top.mainloop()
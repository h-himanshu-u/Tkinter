
from tkinter import *

top = Tk()
top.geometry("500x500")
top.title("tk")

scrol = Scrollbar(top)
scrol.pack()

l1 = Listbox(top,yscrollcommand = scrol.set)

for i in range(1,50) :
    irt = " number " + str(i)
    l1.insert(END,irt)

l1.pack()
scrol.config(command = l1.yview)

top.mainloop()

from tkinter import *

top = Tk()
top.geometry("600x600")
top.title("My First GUI with canvas")

c = Canvas(top,bg = "pink",bd = 10,relief = "groove",height = 500,width = 500)
c.pack(side = LEFT)

imagee = PhotoImage(file = "format-GIF.gif" )
ck = c.create_image(250,250,image = imagee)

c1 = Canvas(top,bg = "yellow",bd = 10,relief = "groove",height = 500,width = 500)
c1.pack(side = LEFT)

ima = PhotoImage(file = "wallpaper.png")
cl = c1.create_image(250,250,image = ima)

top.mainloop()
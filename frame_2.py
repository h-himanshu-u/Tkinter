
# 2nd


from tkinter import * 

top = Tk()
top.geometry("600x600")
top.title("My First GUI with Frames")

frame1 = Frame(top, bg = "red" , height = "100", width = "400")
frame1.place(x=100,y=0)
frame2 = Frame(top , bg = "yellow",height = "450",width = "400")
frame2.place(x=100,y=100)
frame3 = Frame(top ,bg = "blue",height = "50",width = "400")
frame3.place(x=100,y=550)
frame4 = Frame(top,bg = "green",height="600",width="100")
frame4.place(x=0,y=0)
frame5 = Frame(top,bg = "grey",height="600",width="100")
frame5.place(x=500,y=0)

l1 = Label(frame1,text = "left")
l1.place(x=50,y=10)
l2 = Label(frame1,text = "center")
l2.place(x=190,y=10)
l3 = Label(frame1,text = "right")
l3.place(x=350,y=10)

top.mainloop()


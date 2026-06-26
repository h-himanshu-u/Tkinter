
# 4th



from tkinter import * 

top = Tk()
top.geometry("650x700")
top.title("My First GUI with Frames")

frame1 = Frame(top, bg = "light green" , height = "700", width = "650")
frame1.place(x=0,y=0)
frame2 = Frame(frame1 , bg = "white",height = "20",width = "550")
frame2.place(x=50,y=50)
frame3 = Frame(frame1 ,bg = "white",height = "300",width = "550",)
frame3.place(x=50,y=95)
frame4 = Frame(frame1 ,bg = "white",height = "50",width = "50",)
frame4.place(x=295,y=450)


b1 = Button(frame1,text = "submit",bg="red",fg = "black",height = "1",width = "8")
b1.place(x=295,y=70)
b2 = Button(frame1,text = "delete task number",bg="blue",fg = "white",height = "2",width = "20")
b2.place(x=250,y=400)
b3 = Button(frame1,text = "delete",bg="red",fg = "black",height = "2",width = "10")
b3.place(x=280,y=510)
b4 = Button(frame1,text = "exit",bg="red",fg = "black",height = "2",width = "5")
b4.place(x=295,y=560)

l1 = Label(frame1,text = "enter your task",bg="light green",fg = "black")
l1.place(x=280,y=10)

top.mainloop()
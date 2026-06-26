
# 3rd



from tkinter import * 

top = Tk()
top.geometry("600x600")
top.title("My First GUI with Frames")

frame1 = Frame(top, bg = "sky blue" , height = "600", width = "600")
frame1.place(x=0,y=0)
frame2 = Frame(frame1 , bg = "white",height = "20",width = "420")
frame2.place(x=20,y=10)
frame3 = Frame(frame1 ,bg = "white",height = "300",width = "400",)
frame3.place(x=80,y=50)



l1 = Button(frame1,text = "add task",bg="green",fg = "white",height = "1",width = "8")
l1.place(x=450,y=10)
l2 = Button(frame1,text = "remove task",bg="red",fg = "white",height = "1",width = "50")
l2.place(x=20,y=400)
l3 = Button(frame1,text = "complete task",bg="orange",fg = "white",height = "1",width = "12")
l3.place(x=410,y=400)

top.mainloop()


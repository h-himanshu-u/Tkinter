
# 1st


from tkinter import * 

top = Tk()
top.geometry("600x600")
top.title("My First GUI with Frames")

frame1 = Frame(top,bg = "blue" , height = "600", width = "600")
frame1.pack()
frame2 = Frame(frame1 , bg = "green",height = "280",width = "580")
frame2.place(x=10,y=10)
frame3 = Frame(frame1 ,bg = "red",height = "290",width = "580")
frame3.place(x=10,y=300)

l1= Label(frame2,text = "a label in top frame",fg = "black",bg= "green")
l1.place(x=10,y=10)
l2= Label(frame3,text = "a label in bottom frame",fg = "black",bg= "red")
l2.place(x=420,y=250)

top.mainloop()

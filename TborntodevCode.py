from tkinter import*
def g():
    print("HI")
popwindow = Tk ()
Button1 = Button(popwindow,text="ราคา",command=g,width=10,height=5,font=(75),justify="center")
Button1.place(x=700,y=350)
Button2 = Button(popwindow,text="ราคา",command=g,width=10,height=5,font=(75),justify="center") 
Button2.place(x=100,y=100)
Button3 = Button(popwindow,text="ราคา",command=g,width=10,height=5,font=(75),justify="center") 
Button3.place(x=300,y=100) 
print ()
popwindow.mainloop()
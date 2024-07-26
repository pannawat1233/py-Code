from tkinter import*
def sayHelloWorld():
    print("Hello World")
ManWindow = Tk()
Button1 =Button(ManWindow,text="Click",command=sayHelloWorld,width=20,height=20,font=("Helvetica",76),anchor=E).grid(row=0,column=1)
Button2 =Button(ManWindow,text="Click",command=sayHelloWorld).grid(row=1,column=1)
Button2 =Button(ManWindow,text="Click",command=sayHelloWorld).grid(row=0,column=2)
label = Label(ManWindow,text="Hello World",width=20).grid(row=2, column=1)
ManWindow.mainloop()
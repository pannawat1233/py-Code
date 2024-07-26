from tkinter import *

def LeftClicker(event):
    print("Left")

def DoubleClicker(event):
    print("Double")

ManWindows = Tk()
Button1 = Button(ManWindows, text="Click")
Button1.pack()
Button1.bind('<Button-1>', LeftClicker)
Button1.bind('<Double-1>', DoubleClicker)
ManWindows.mainloop()
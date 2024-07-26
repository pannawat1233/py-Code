from tkinter import*
import subprocess

ManWindows = Tk()

def shutdown ():
    subprocess.run(["shutdown", "/r", "/t", "0"])

Button1 = Button(text="shutdown",command=shutdown)
Button1.grid(row=0,column=0)

ManWindows.mainloop()


from tkinter import*
import math

ManWindows = Tk()

def LeftClicker(event):
    ac = (float(textBox1.get())/math.pow(float(textBox2.get())/100,2))
    LabelHeight3.configure(text=(float(textBox1.get())/math.pow(float(textBox2.get())/100,2)))
    print(ac)

LabelHeight1 = Label(ManWindows,text ="ส่วนสูง(cm)")
LabelHeight1.grid(row=0,column=0)
textBox1 = Entry(ManWindows)
textBox1.grid(row=0,column=1)
LabelHeight2 = Label(ManWindows,text="น้ำหนัก(kg)")
LabelHeight2.grid(row=1,column=0)
textBox2 = Entry(ManWindows)
textBox2.grid(row=1,column=1)
Button1 = Button(ManWindows,text="คำนวน")
Button1.grid(row=2)
Button1.bind ('<Button-1>',LeftClicker)
LabelHeight3 = Label(ManWindows,text ="ผลัพธ์")
LabelHeight3.grid(row=2,column=1)
ManWindows.mainloop()


import tkinter.ttk as ttk
from tkinter import *
import time

root = Tk()
root.title("gui2")
root.geometry("400x400")

vs = [str(i) for i in range(1,6)]

lb = ttk.Combobox(root, height = 3, values = vs, state = "readonly")
lb.set("엄준식")
lb.pack()

def dlbtn() :
    print(lb.get())

lbtn = Button(root, text="value in lb", command = dlbtn)
lbtn.pack()

chkvar = IntVar()
cb1 = Radiobutton(root, text="엄준식1", value = 1, variable=chkvar)
cb2 = Radiobutton(root, text="엄준식2", value = 2, variable=chkvar)
cb3 = Radiobutton(root, text="엄준식3", value = 3, variable=chkvar)
cb1.pack()
cb2.pack()
cb3.pack()

def ott() :
    print(chkvar.get())

btn = Button(root, text="엄1준2식3", command = ott)
btn.pack()

pvar =DoubleVar()

pb = ttk.Progressbar(root, maximum=100, length = 150, variable = pvar, mode = "determinate")
pb.pack()

def getpb() :
    print(pvar.get())
    btn.config(text="엄2준3식4")

btn2 = Button(root, text="progressbar variable", command = getpb)
btn2.pack()

def setpb() :
    for i in range(1,101) :
        time.sleep(0.01)
        pvar.set(i)
        pb.update()
        print(pvar.get())

btn3 = Button(root, text="progressbar start", command = setpb)
btn3.pack()

root.mainloop()
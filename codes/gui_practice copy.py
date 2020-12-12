from tkinter import *

root = Tk()
root.title("gui2")
root.geometry("400x400")

btn1 = Button(root, text="버튼1")
btn2 = Button(root, text="버튼2")

btn1.grid(row=0, column=0)
btn2.grid(row=11, column=12)

root.mainloop()
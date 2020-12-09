from tkinter import *

root = Tk()
root.title("gui_practice")
root.geometry("400x400")

label1 = Label(root, text = "엄준식")
label1.pack()

def btncmd() :
    label1.config(text="엄준식은 살아있다")

def delete() :
    txt.delete("1.0",END)

btn = Button(root, text="엄튼", command = btncmd)
btn.pack()

txt = Text(root, width=30,height=5)
txt.pack()

e=Entry(root, width=30)
e.insert(END, "엄준식준엄")
e.pack()

btn2 = Button(root, text="del_text", command = delete)
btn2.pack()

root.mainloop()
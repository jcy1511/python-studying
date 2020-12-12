from tkinter import *

root = Tk()
root.title("gui2")
root.geometry("400x400")

frame1 = LabelFrame(root, text="frame1")
frame1.pack()

scrollbar = Scrollbar(frame1)
scrollbar.pack(side = "right", fill = "y")

listbox = Listbox(frame1, selectmode="extended", height=10, yscrollcommand = scrollbar.set)
for i in range(1,32) :
    listbox.insert(END, i)
listbox.pack(side="left")
scrollbar.config(command=listbox.yview)

root.mainloop()
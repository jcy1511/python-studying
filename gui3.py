from tkinter import *

root = Tk()
root.title("gui2")
root.geometry("400x400")

mn = Menu(root)

def cmd():
    print("새 파일을 만듭니다")

def open():
    print("여는 중")

menu_file = Menu(mn, tearoff = 0)
menu_file.add_command(label="New file", command = cmd)
menu_file.add_separator()
menu_file.add_command(label="Open", command=open)
menu_file.add_separator()
menu_file.add_command(label="Save all", state = "disabled")

mn.add_cascade(label = "File", menu = menu_file)

mn.add_cascade(label="Edit")

chkvar = IntVar()
menu_lang = Menu(mn, tearoff=0)
menu_lang.add_radiobutton(label="Java", value = 1, variable = chkvar)
menu_lang.add_radiobutton(label="Python", value = 2, variable = chkvar)
menu_lang.add_radiobutton(label="C++", value = 3, variable = chkvar)
mn.add_cascade(label="Languages", menu = menu_lang)


menu_view = Menu(mn, tearoff=0)
menu_view.add_checkbutton(label="Show minimap")
mn.add_cascade(label="View", menu=menu_view)

root.config(menu = mn)




def cmd():
    print(chkvar.get())

btn = Button(root, text="radiobutton", command = cmd)
btn.pack()




root.mainloop()
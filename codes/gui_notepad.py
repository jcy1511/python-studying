from tkinter import *
import os
import tkinter.messagebox as msgbox

root = Tk()
root.title("gui_notepad")
root.geometry("400x400")



filename = "mynote.txt"

def open_file():
    if os.path.isfile(filename):
        with open(filename, "r", encoding="utf8") as file :
            text.delete("1.0", END)
            text.insert(END, file.read())

def save_file():
     with open(filename, "w", encoding="utf8") as file :
            file.write(text.get("1.0", END))
            msgbox.showinfo("저장","저장되었습니다.")





menu = Menu(root)

menu_file = Menu(menu, tearoff=0)
menu_file.add_command(label="열기", command = open_file)
menu_file.add_command(label="저장", command = save_file)
menu_file.add_separator()
menu_file.add_command(label="끝내기")
menu.add_cascade(label="파일", menu=menu_file)

menu.add_cascade(label="편집")
menu.add_cascade(label="서식")
menu.add_cascade(label="보기")
menu.add_cascade(label="도움말")

root.config(menu=menu)


scrollbar = Scrollbar(root)
scrollbar.pack(side="right", fill="y")


text=Text(root, yscrollcommand=scrollbar.set)
text.pack(side="left", fill="both", expand=True)

scrollbar.config(command=text.yview)



root.mainloop()
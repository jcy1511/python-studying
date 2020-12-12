from tkinter import *

root = Tk()
root.title("gui2")
root.geometry("400x400")

menu = Menu(root)

menu_file = Menu(menu, tearoff=0)
menu_file.add_command(label="열기")
menu_file.add_command(label="저장")
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
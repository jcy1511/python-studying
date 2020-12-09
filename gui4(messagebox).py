from tkinter import *
import tkinter.messagebox as msgbox

root = Tk()
root.title("gui2")
root.geometry("400x400")


# def info():
#     msgbox.showinfo(btn, "정상적으로 예매 완료되었습니다")

# btn = Button(root, text="알림", command=info)
# btn.pack()

def info():
    msgbox.showinfo("알림", "정상적으로 예매 완료되었습니다")

def warn():
    msgbox.showwarning("경고", "해당 좌석은 매진되었습니다")

Button(root, text="알림", command=info).pack()

Button(root, text="경고", command=warn).pack()


root.mainloop()
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
    msgbox.showinfo("알림", "정상적으로 예매 완료되었습니다.")

def warn():
    msgbox.showwarning("경고", "해당 좌석은 매진되었습니다.")

def error():
    msgbox.showerror("에러", "결제 오류가 발생했습니다.")

def okcancel():
    msgbox.askokcancel("확인/취소", "확인/취소")

def yesno():
    response = msgbox.askyesno("y/n", "y/n")
    print(response)


Button(root, text="알림", command=info).pack()
Button(root, text="경고", command=warn).pack()
Button(root, text="에러", command=error).pack()
Button(root, text="확인/취소", command=okcancel).pack()
Button(root, text="y/n", command=yesno).pack()


root.mainloop()
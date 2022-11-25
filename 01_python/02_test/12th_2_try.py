#로그인 인증 처리 문제
#도전
from tkinter import *
from tkinter import messagebox
from tkinter import font

w=Tk()
w.title("로그인")

def login_try():
    if input_id.get() == "cmr" and input_pw.get() == "1234":
        messagebox.showinfo("Success", "로그인에 성공하였습니다.")
    elif input_id.get() != "cmr":
        messagebox.showerror("id not Found", "등록되지 않은 아이디입니다.")
    else:
        messagebox.showerror("password error", "비밀번호가 틀렸습니다.")

#스타일
titleStyle= font.Font(family="Malgun Gothic", size="18", weight="bold")

title=Label(w, text="로그인", font=titleStyle)
label_id=Label(w, text="아이디")
input_id=Entry(w)
label_pw=Label(w, text="비밀번호")
input_pw=Entry(w)
btn_main=Button(w, text="로그인", command=login_try)
btn_cancle=Button(w, text="취소", command=quit)


title.pack(pady=32, side=TOP)
label_id.pack()
input_id.pack()
label_pw.pack()
input_pw.pack()
btn_main.pack()
btn_cancle.pack()

w.geometry("360x400")

w.mainloop()
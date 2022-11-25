#답
from tkinter import *
from tkinter.messagebox import *

def login():
    if sid.get=="sejong":
        if spw.get()=="1234":
            showinfo("success", "로그인 성공")
        else:
            showerror("fail", "패스워드 오류")
    else:
        showinfo("fail", "회원가입")

#메인코드
w=Tk()
w.title("Welcome to SEJONG!!")
logo=Label(w, text="세사대-온라인 강의실", fg="green")
sid=Entry(w)
spw=Entry(w, show="♧")
btn1=Button(w, text="Login", command=login, fg="white", bg="green")

logo.pack()
sid.pack()
spw.pack()
btn1.pack()

w.geometry("200x300")
w.mainloop()
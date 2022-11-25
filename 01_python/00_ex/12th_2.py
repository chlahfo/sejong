#CUI 방식 - 문자 기반으로 사용자와 소통
#GUI 방식 - 그래픽 요소를 기반으로 사용자와 소통
from tkinter import *
from tkinter import messagebox

def login():
    if pw.get() == "1234":
        messagebox.showinfo("success", "로그인 성공")
    else:
        messagebox.showerror("fail", "로그인 오류")

w=Tk() #윈도우 생성

w.title("Welcome to SEJONG!!")

#위젯생성
label1=Label(w, text="패스워드")
pw = Entry(w, show="*")
btn1=Button(w, text="확인", command=login)
btn2=Button(w, text="종료", command=quit)

#위젯배치 (얼굴 팩처럼 배치하기)
label1.pack()
pw.pack()
btn1.pack()
btn2.pack()
w.geometry("300x200")#윈도우 크기


w.mainloop()
#mainloop()는 단순히 코드 마지막이 아니라 프로그램 흐름 마지막단에 위치해야 한다. (https://golony777.tistory.com/31)
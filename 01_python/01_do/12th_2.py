from tkinter import *
from tkinter import messagebox

def login():
    if pw.get() =="sejong":#사용자가 입력한 값을 가져옴.
        messagebox.showinfo("success", "로그인 성공!")#첫 번째, 두번쨰 == 대화상자 제목 , 내용
    else:
        messagebox.showerror("Fail", "패스워드 오류")


w=Tk()#윈도우 생성
w.title("Welcom to SEJONG!")#윈도우 제목

label1 = Label(w, text="패스워드")#라벨: 텍스트 지정
pw = Entry(w, show="*")#엔트리: *로 보이도록 지정
btn1 = Button(w, text="확인", command=login)#버튼1: 확인텍스트 지정, 로그인(커스텀 함수)지정. 커멘드는 함수 이름만 지정
btn2 = Button(w, text="종료", command=quit)#버튼2: 텍스트 지정, 종료 함수 지정

label1.pack()#라벨 배치
pw.pack()
btn1.pack()
btn2.pack()
w.geometry("300x200")#윈도우 크기 지정

w.mainloop()#윈도우 꺼지지 않게 조정

#15:00

#질문
#import 에서 *를 써서 모두 가져왔는데 왜 messagebox 만 따로 추가로 가져와야 하는건지
#form  import 구문을 두 개 이상 사용했을 때 같은 이름의 함수가 있으면 충돌이 나지 않는건지
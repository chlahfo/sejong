#터틀그래픽을 사용!!!하여 사각형 그리기
#파이썬 터틀
import turtle

turtle.shape("turtle")
"""
for i in range(4): #사각형은 4변의 길이를 가지고 있으므로 4번 반복
    turtle.forward(100)#100만큼 앞으로 나아감
    turtle.left(90)#90도 회전 
"""
for i in range(2):
    turtle.forward(100)
    turtle.left(30)
    turtle.forward(200)
    turtle.left(150)
#막대그래프 그리기(0 입력되면 그리기 멈춤)

#도전
import turtle
import sys

while True:
    print("막대그래프 수치를 입력해주세요(1~500)(종료시 0입력): ", end="")
    n = int(sys.stdin.readline().rstrip())

    if n == 0:
        print("종료")
        break

    turtle.forward(20)

    for i in range(2):
        turtle.forward(10)
        turtle.left(90)
        turtle.forward(n)
        turtle.left(90)

turtle.forward(40)

#답
while True:
    n = int (input("n:"))
    if n == 0:
        break
    for i in range(n):
        print("*", end="")
    print()
#사각형 그리기
#import 로 불러오면 앞에 계속 모듈 이름을 붙여줘야함.
from turtle import *
color("blue")
shape("turtle")
for i in range(4):
    forward(100)
    left(90)

#알고리즘
#사각형 그리는 동작은
#앞으로 일정 거리 이동
# 왼쪽  or 오른쪽으로 90도 회전 과정을 4번 반복하면 된다.

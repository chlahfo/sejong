#터틀 그래픽 모듈이 제공하는 함수를 이용하여 입력받은 숫자에 따라 다각형을 그리는 프로그램
#도전
"""
from turtle import *
import sys

def figure(nums):
    if nums == 1 or nums ==2:
        print("\n!!!!3이상의 수 필요!!!!")
        inNum()
    else:
        corner_sum = 180 * (nums-2)
        corner = corner_sum/nums
        cursor_corner = 180 - corner
        line_len = 720 / nums
        
        for i in range(nums):
            forward(line_len)
            right(cursor_corner)

def inNum():
    print("\n몇 각형 입니까?\n(주의! 3이상의 수에서 한계점은 없지만 큰 수를 입력할 경우 느릴 수 있습니다 100이하의 수를 입력 하는 것을 추천합니다.):", end=" ")
    n = int(sys.stdin.readline().rstrip())
    figure(n)

inNum()
"""
#외각 값
#180-[180 * (n - 2)/n]
#180 -180(n-2)/n
#180+(-180n+360)/n
#180+(-180+360/n)
#180-180+360/n
#360/n

#답
from turtle import *
def makepolygon(n):
    for i in range(n):
        forward(100)
        left(360/n)#외각 구하는 공식
shape("turtle")
n=int(textinput("도형그리기", "숫자입력(삼각형:3, 사각형:4, 오각형:5)"))#안내창 제목, 내용
if n in [3, 4, 5]:
    makepolygon(n)
else:
    print("error")


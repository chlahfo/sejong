import sys
#점수 입력하면 학점출력
def score(x):
    if x >= 90:
        return "A"
    elif x >= 80:
        return "B"
    elif x >= 70:
        return "C"
    else:
        return "F"

while True:
    print("점수를 입력해주세요(단, 종료 하고 싶을 경우 -1을 입력해주세요):", end=" ")
    n = int(sys.stdin.readline().rstrip())

    if n < -1 or n > 100:
        print("점수를 잘못 입력하였습니다. 다시 입력해주세요")
    elif n == -1:
        print("점수 입력 종료")
        break
    else:
        print(score(n))

#답
def grade(s):
    if s >= 90:
        print("A")
    elif s >= 80:
        print("B")
    elif s >= 70:
        print("C")
    else:
        print("F")

score = int (input("score:"))
grade(score)

#매개변수 (Parameter):호출된 함수에서 전달받은 값을 임시로 할당하는 변수(s)
#인수(Argument):호출된 함수에 전달할 값(score)
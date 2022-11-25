#주사위 게임

#도전
import sys
import random

while True:
    print("1~6 의 정수를 입력하세요")
    me = int(sys.stdin.readline().rstrip())
    com = random.randint(1, 6)
    print("컴퓨터 숫자:", com)
    
    if me == 0:
        print("종료")
        break
    elif me > com:
        print("승리!")
        break
    elif me == com:
        print("동점")
    else:
        print("패배")

#답
import random
print("주사위 게임 시작")
throw = input("Enter 를 치세요")

while throw != "0": #0 이 아닐 동안 반복됨
    com = random.randint(1, 6) #1~6
    user = int(input("num:"))
    if com>user:
        win="com"
    else:
        win="user"
    print("com {} : user {}, {} win" .format(com, user, win))

    throw=input("재시작: Enter, 종료:0")
#입력한 숫자 홀수 판별. 0일때 종료
import sys
while True:
    print("수를 입력하세요:", end=" ")
    num = int(sys.stdin.readline().rstrip())
    if num == 0:
        print("종료")
        break
    elif num % 2 ==0:
        print("짝수")
    else:
        print("홀수")


    
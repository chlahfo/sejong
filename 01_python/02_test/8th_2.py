#난수
import random
import sys
com = random.randint(1, 20)
try_num = 0
#도전
while True:
    print("컴퓨터가 설정한 숫자(1 ~ 20)를 맞춰보세요:", end=" ")
    try_num += 1
    num = int(sys.stdin.readline().rstrip())

    if num == 0:
        print("강제종료")
        break
    elif com == num:
        print("정답")
        print("사용자가 {}번만에 정답을 맞췄습니다.".format(try_num))
        break
    elif com < num:
        print("좀 더 작게")
    else:
        print("좀 더 크게")
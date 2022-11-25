#사용자로부터 단을 입력 받아 구구단을 출력하기

#도전
import sys
print("구구단을 시작할 숫자를 입력해주세요: ")
num = int(sys.stdin.readline().rstrip())
for i in range(1, 10):
    print("{} x {} = {}" .format(num, i, num*i))

#답
dan = int(input("단 입력:"))
for i in range(1, 10):
    print("%d * %d = %d" %(dan, i, dan*i))
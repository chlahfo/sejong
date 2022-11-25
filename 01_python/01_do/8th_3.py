#1부터 사용자로부터 입력받은 숫자까지 짝수/홀수를 판별하는 프로그램
#도전
import sys
print("끝 수를 입력하세요 :",end=" ")
num = int(sys.stdin.readline().rstrip())


for i in range(1, num+1):
    if i % 2 == 0:
        print("{}는 짝수입니다." .format(i))
    else:
        print("{}는 홀수입니다." .format(i))

#답
n = int(input("수를 입력 : "))
for i in range(1, n+1):
    if i%2 ==0:
        print(i, "짝수")
    else:
        print(i, "홀수")

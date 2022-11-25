#두 정수를 입력받아 덧셈 결과를 출력하는 프로그램
#도전
import sys
def add(a, b):
    return a + b
print("더 할 두 정수를 입력해주세요(단, 띄어쓰기로 구분해주세요)", end=" ")
x, y = map(int, sys.stdin.readline().rstrip().split())
print(add(x, y))

#답
def add(n1, n2, n3):
    result = n1+ n2 + n3 #연산식이 길어질 수 있으므로 미리 변수에 넣어둔다.
    return result
num1=int(input("num1: "))
num2=int(input("num2: "))
num3=int(input("num3: "))
result = add(num1, num2, num3)#오른쪽 먼저 실행된 후 왼쪽으로 대입함 식이 길어질 수 있기 때문에 반환값을 변수에 담은 뒤 출력함.

print(result)

#개인적 응용
def add(item):
    sum = 0
    for i in item:
        sum += i
    return sum 

print("더 할 숫자들을 입력해주세요(단 띄어쓰기로 구분해주세요)")
s = tuple(map(int, sys.stdin.readline().rstrip().split()))
print(add(s))

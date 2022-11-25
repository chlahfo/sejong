#사용자로부터 시작, 끝 값을 입력 받은 후 전체 합계, 짝수의 합계, 홀수의 합계를 출력하는 프로그램

#도전
import sys
print("시작 수를 입력하세요:", end=" ")
s_num = int(sys.stdin.readline().rstrip())
print("끝 수를 입력하세요:", end=" ")
num = int(sys.stdin.readline().rstrip())
sum = 0
sum_even = 0
sum_odd = 0

for i in range(s_num, num + 1):
    sum += i
    if i % 2 == 0:
        sum_even += i
    else:
        sum_odd += i

print("전체 합계: {} \n 짝수의 합계 : {} \n 홀수의 합계 : {}" .format(sum, sum_even, sum_odd))

#답
#IPO 기법
#I = input, 입력받을 수가 몇개인지, P = process, 입력받은 수를 어떻게 처리할건지, O = output출력받을 수 

s = int(input("start num:"))
e = int(input("end num:"))
total, even, odd = 0, 0, 0
for i in range(s, e+1):
    total += i
    if i % 2 == 0:
        even += i
    else:
        odd += i

print("전체 합계:", total)
print("짝수 합계:", even)
print("홀수 합계:", odd)
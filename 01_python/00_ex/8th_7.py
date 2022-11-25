#반복문의 종류
#1~10까지 출력
#1. 반복문을 사용하지 않은 경우
print(1,2,3,4,5,6,7,8,9,10, sep="\n")

print("\n")

#2.for 문 사용
for i in range(1, 11):
    print(i)

print("\n")
#3. while문사용
i = 1
while i < 11:
    print(i)
    i= i+1
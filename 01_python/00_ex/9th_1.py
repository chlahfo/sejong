#수강하는 과목의 점수를 리스트에 저장, 점수가 70점 이상인 과목 수를 출력

#도전
score=[70, 90, 60, 100, 60]
num = 0

#확장
import sys
while True:
    print("추가할 점수 입력(단, 음수 값 입력 시 입력 값 종료):", end=" ")
    m=int(sys.stdin.readline().rstrip())
    score.append(m)

    if m <= -1:
        score.remove(-1)
        print("입력종료")
        break

for i in score:
    if i >= 70:
        num += 1
print(score, num, sep="\n")



#답
score=[70, 90, 60, 100, 60]
cnt=0
for i in range(5):
    if score[i]>=70:
        cnt += 1
print("count: ", cnt)

#I:  리스트에 해당되는 과목의 점수
#P: 점수비교
#O: 몇개나 되는지
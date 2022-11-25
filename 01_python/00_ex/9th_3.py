#레벨판별 프로그램

#도전
import sys
print("학생들의 점수를 입력하세요(띄어쓰기로 구분해주세요)")
score = list(map(int, sys.stdin.readline().rstrip().split()))
for i in score:
    if i > 90:
        print(i, "Level 1")
    elif i > 80:
        print(i, "Level 2")
    elif i > 70:
        print(i, "Level 3")
    else:
        print(i, "Fail")

#답
print("-" * 30)
score = [85, 95, 70, 50, 100]
n = 0
print("코딩 시험 결과")
for s in score:
    n += 1

    if s >= 90:
        result = "LEVEL 1"
    elif s>= 80:
        result = "LEVEL 2"
    elif s>=70:
        result = "LEVEL 3"
    else:
        result ="FAIL"

    print("{} 번 학생의 점수는 {}입니다." .format(n, s))
    print("결과는 {}입니다." . format(result))
    print()
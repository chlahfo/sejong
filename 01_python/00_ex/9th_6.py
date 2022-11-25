#합격, 불합갹

#도전
score=[20, 40, 70, 100, 90, 88]
for i in score:
    if i >= 80:
        print("합격")
    else:
        print("불합격")

#답
score = [60, 80, 90, 70, 95]
cnt = 0
print(score)
for i in range(len(score)):
    if score[i] > 80:
        result = "합격"
        cnt += 1
    else:
        result ="불합격"
    print("{}번 학새은 {}입니다." .format(i+1, result))
print("합격한 학생 수:", cnt)
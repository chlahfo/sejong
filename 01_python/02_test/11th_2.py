#도전
f = open("score2.txt", encoding="UTF-8")

while True:
    line = f.readline()
    if not line: break
    name, score = line.split()
    score = int(score)
    
    if score >= 90:
        print(name, score, "A")
    elif score >= 80:
        print(name, score, "B")
    elif score >= 70:
        print(name, score, "C")
    elif score >= 60:
        print(name, score, "D")
    else:
        print(name, score, "F")
    
f.close()

#답
def grade(avg):
    if avg>=90:
        result="A"
    elif avg>=80:
        result="B"
    elif avg>=70:
        result="C"
    elif avg>=60:
        result="D"
    else:
        result="F"
    return result

f= open("score2.txt", encoding="UTF-8")
print("이름, 평균, 학점")
for line in f:
    name, avg = line.split()
    avg=int(avg)
    result = grade(avg)
    print(name, avg, result)
f.close()

    
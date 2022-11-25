#도전
f = open("score1.txt", encoding="UTF-8")
print("이름, 합계, 평균")
for line in f:
    name,mid,final=line.split()
    hap= int(mid)+int(final)
    avg=hap/2
    print(name, hap, avg)
f.close()
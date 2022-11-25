#데이터 시각화
import csv
import matplotlib.pyplot as plt              #1 matplotlib 라이브러리에 속한 pyplot 모듈을 불러옴
#csv = 내장 모듈(설치 x), matplotlib = 외부모듈(설치필요)
#pip install 모듈명 --> 설치 됨
#실행: cmd -> 도스창에서 설치

f = open("2002.csv")    
data = csv.reader(f)    
header = next(data)     
print(header) 
temp=[]                                     #2 평균 
for row in data:                            
    temp.append(row[1])                     #3 평균기온을 리스트에 저장
temp=list(map(float, temp))                 #4 평균기온 데이터는 숫자값이 아닌 문자열이기 떄문에 값을 숫자 데이터형으로 변환


print(temp)

#그래프 그리기
plt.title("Aberage tempertature graph")
plt.plot(temp, linewidth=5)
plt.xlabel("day")
plt.ylabel("temperature")
plt.legend(["temperature"])
plt.show()

f.close()               




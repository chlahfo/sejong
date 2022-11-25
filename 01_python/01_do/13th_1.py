#기온 공공 데이터 분석 시작
#https://data.kma.go.kr
#csv : Comma-Seperated Values
# 각각의 데이터 값을 콤마(,) 로 구분하는 파일 형식
# 공공데이터 포털이 제공하는 일반적인 파일 형식
# 데이터 분석가들이 자주 사용 (데이터 정제)

import csv              #1  csv 모듈을 불러옴

f = open("2002.csv")    #2  csv 파일을 open() 함수를 열어서 f에 저장함
data = csv.reader(f)    #3  csv 파일에서 데이터를 읽어와서 data에 저장함 reader ->내용물들을 다 읽어서 데이터 변수가 가지고 있음
header = next(data)     #4  header라는 변수에 헤더 데이터 행을 저장함 next -> 첫번째 행을 읽어옴
print(header)           #5
for row in data:        #6
    print(row)          #7
f.close()               #8

#각 행의 데이터는 리스트로 반환됨
#각 행의 데이터가 문자열로 이루어져있음


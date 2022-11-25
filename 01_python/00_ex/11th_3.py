#파일 읽기: readlines() -> 파일의 모든 줄을 읽어서 리스트로 반환함 
f = open("name.txt", encoding="UTF-8")
data=f.readlines()
print(data)

for line in data:
    print(line, end="")

f.close()
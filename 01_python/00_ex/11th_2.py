#readline() 함수 -> 한 줄 씩 읽어오며 문자열로 반환함
f = open("name.txt", encoding="UTF-8")
data=f.readline()
print(data)
f.close()

f = open("name.txt", encoding="UTF-8")
while True:
    data=f.readline()
    if not data: break
    print(data, end="")
f.close()
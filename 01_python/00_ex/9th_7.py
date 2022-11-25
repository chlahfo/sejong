#메뉴와 가격 정보 출력

#도전
import sys

menu = {"떡볶이": 3000, "라면": 2500, "돈까스": 4500}

print("{:-^20}".format("메뉴판"))
for i in menu.keys():
    print("{}: {}".format(i, menu[i]))
print("{:-^20}".format(""))
while True:
    print("가격을 검색할 메뉴명을 입력해주세요(q 입력 시 종료):", end=" ")
    txt = sys.stdin.readline().rstrip()
    
    if txt == "q":
        print("종료")
        break
    elif menu.get(txt):
        print("{}: {}".format(txt, menu[txt]))
    else:
        print("없는 메뉴")

# 답
menu = {}
menu["라면"]=3000
menu["떡볶이"]=3000
menu["김밥"]=3000
menu["햄버거"]=3000

for i in menu.keys():
    print("{}-{}".format(i, menu[i]))

while True:
    s=input("seach menu:")

    if s == "q":
        break
    print(menu.get(s, "not Found"))#첫번째 키 값, 두번쨰 인수 없을 때 반환되는 값
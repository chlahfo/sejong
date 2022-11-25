#답
addr = {} #빈 딕셔너리 생성

while True:
    s= int(input("1) 친구등록  2) 검색  3)종료"))
    if s == 1:
        name = input("name: ")
        phone = input("phone:" )
        addr[name] = phone
    elif s == 2:
        name =input("name : ")
        print(addr.get(name, "주소록에 없는 이름입니다."))
    elif s == 3:
        print("종료")
        break
    else:
        print("잘못 입력")
#종합 프로젝트(연락처어플 만들기)

#함수 정의 
def add():
    name = input("이름:")
    tel = input("연락처:")#연산에 참여시킬 숫자가 아니므로 문자열로 저장
    email=input("email:")
    return name, tel, email

def search():
    for all in datalist:#[(), (), ...]
        if find_name in all:
            print(all)
            print("찾았습니다.")
            print(find_name)
        else:
            print("해당 정보가 없습니다.")

print("메뉴를 선택하세요")
print("1:추가")
print("3:검색")
print("0:종료")

datalist=list() #빈 리스트를 만드는 곳에 사용 []

while True:
    menu=int(input("메뉴선택:"))
    if menu == 1:
        datalist.append(add())#튜플로 넣음
        print(datalist)
    elif menu == 3:
        find_name = input("이름으로 찾기:")
        search()
    elif menu == 0:
        break
    else:
        print("입력오류")
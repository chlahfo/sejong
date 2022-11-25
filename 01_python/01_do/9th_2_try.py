import sys
#스마트폰 친구 등록 이후 친구 이름 검색후 연락처 출력

#도전
f_list={}
c_num = 1000

while c_num != 0:
    
    print("""메뉴를 선택하세요

1) 친구등록
2) 검색
3) 전체 연락처 보기
0) 종료
    """)

    c_num = int(sys.stdin.readline().rstrip())
    if c_num == 0:
        print("프로그램 종료")
    elif c_num == 1:
        print("친구등록(처음 메뉴로 가기를 원하시면 입력 진행 시 0을 눌러주세요)")

        while True:
            print("\n이름과 전화번호를 입력해주세요(이름과 전화번호는 띄어쓰기로 구분해주세요.):", end=" ")
            user_input1 = sys.stdin.readline().rstrip()

            if user_input1 == "0":
                print("\n친구등록을 종료합니다.")
                break
            else:
                user_input1 = list(user_input1.split())
                f_list[user_input1[0]] = user_input1[1]
                
    elif c_num == 2:
        print("검색(처음 메뉴로 가기를 입력 진행 시 0을 눌러주세요)")

        while True:
            print("찾으실 연락처의 이름을 입력해주세요:", end=" ")
            user_input2 = sys.stdin.readline().rstrip()

            if user_input2 == "0":
                print("\n검색을 종료합니다.")
                break
            elif f_list.get(user_input2):
                print(f_list[user_input2])
            else:
                print("등록된 연락처가 없습니다.")
    
    elif c_num == 3:
        print("{:-^26}".format("연락처"))
        if f_list:
            for i in f_list.keys():
                print("{} : {}" .format(i, f_list[i]))
        else:
            print("\n등록된 연락처가 없습니다.")
        print("{:-^30}".format(""))
    else:
        print("\n잘못 입력(다시 입력 요청)")



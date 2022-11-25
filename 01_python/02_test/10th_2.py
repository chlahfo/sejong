#예약 프로그램 문제
def price(menu):
    if menu == 1:
        m="아메리카노"
        p="2500원"
    elif menu == 2:
        m="카페라떼"
        p="3000원"
    elif menu ==3:
        m = "바닐라라떼"
        p = "3000원"
    print(m, p)

n = int(input("메뉴를 선택해주세요 1: 아메리카노 2: 카페라떼 3: 바닐라라떼"))
result = price(n)


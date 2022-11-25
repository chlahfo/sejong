#빈 곳 채우기
def greet(lang):
    if lang == 1:
        print("Hello")
    elif lang == 2:
        print("Bounjour")
    elif lang == 3:
        print("안녕?")
    else:
        print("지원 안함")

h = int(input("언어를 선택하세요 1:EN / 2:FR / 3:KR\n"))
greet(h)
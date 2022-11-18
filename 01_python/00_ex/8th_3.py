#리스트를 활용한 반복 출력
for i in [1,2,3,4,5]:
    print(i, end=" ")
num = [1,2,3,4,5]
for i in num:
    print(i, end=" ")

print("\n")
#딕셔너리를 활용한 반복 출력
menu = {"쌀국수":4500, "볶음우동": 5000, "햄버거":4800}
for k in menu.keys():
    print(k, ":",menu[k])
f=open("club.txt", "w", encoding="UTF-8")
while True:
    name = input("name:")
    if not name:break
    f.write(name + "\n")#안하면 이어서 입력되어버림
f.close()
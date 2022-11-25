f=open("club.txt", "a", encoding="UTF-8")
while True:
    name = input("name: ")
    if not name: break
    f.write(name+"\n")
f.close()
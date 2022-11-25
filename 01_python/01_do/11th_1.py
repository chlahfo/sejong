#텍스트 파일을 모두 읽어 화면에 출력
f = open("data1.txt", "w", encoding="UTF-8")
f.write("Life is too short.\nSo, you need Python.\nPython is easy,\nand useful on many fields.")
f.close()

with open("data1.txt", "r", encoding="UTF-8") as f:
    lines=f.read()
    print(lines)
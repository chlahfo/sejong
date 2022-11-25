with open("name.txt", encoding="UTF-8") as f: #이 블럭을 벗어나면 자동으로 파일이 닫힘.
    data=f.readlines()
    for line in data:
        print(line, end="")
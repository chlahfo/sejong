#텍스트 파일 저장과 읽기
#도전
"""
import sys
nums = 0
with open("guest1.txt", "w", encoding="UTF-8") as f:
    while True:
        print("이름:", end=" ")
        names = sys.stdin.readline().rstrip()
        
        if not names:
            print("입력값 없음. 종료")
            break
        else:
            print("Welcome {}!".format(names))
            f.write(names+"\n")
            nums += 1
        
print("총 학생 수 {}명".format(nums))
"""

import sys
nums = 0
f = open("guest1.txt", "w", encoding="UTF-8")
while True:
        print("이름:", end=" ")
        names = sys.stdin.readline().rstrip()
        
        if not names:
            print("입력값 없음. 종료")
            break
        else:
            print("Welcome {}!".format(names))
            f.write(names+"\n")
            nums += 1

f.close()    
        
print("총 학생 수 {}명".format(nums))
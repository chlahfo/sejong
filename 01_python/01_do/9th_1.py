#로또 추첨
#도전 1~45 (6개 숫자)- 중복 제거..

import random
num_list=[]
all_nums=list(range(1, 46))
all_nums_len=len(all_nums)
for i in range(6):
    ran_num = random.randint(1, all_nums_len)
    num_list.append(all_nums[ran_num])

    #중복 제거
    all_nums.pop(ran_num)
    all_nums_len -= 1

num_list.sort()
print(num_list)

#답
lotto=[]
print("로또 프로그램 시작")
while True:
    num = random.randint(1, 45)
    #중복된 숫자 제거
    if lotto.count(num)==0:
        lotto.append(num)
    
    if len(lotto)==6:
        break
lotto.sort()
print("추첨된 로또 번호")
print(lotto)
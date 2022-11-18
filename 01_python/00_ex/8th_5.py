num = [10, -10, 20 , -30]
for i in num:
    if i < 0:
        break
    print(i)

for i in num:
    if i < 0:
        continue
    print(i)

#continue 와 pass 의 차이점?
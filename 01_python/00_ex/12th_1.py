#모듈 사용의 예
import random 
n = random.randint(1, 10)
print(n)

#별칭 쓰기
import random as r
n = r.randint(1, 10)
print(n)

#form 절 쓰기
from random import randint
n=randint(1, 10)
print(n)

#from 절 쓰기 2
from random import *
n=randint(1, 10)
print(n)
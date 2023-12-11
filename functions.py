# #제곱을 알려주는 함수

import random

a=random.randint(1,10)

def ha(x):
    o=x**2
    return o

print(ha(a))

# 2로 나누기
import random

a=random.randint(2,20)

def ha(x):
    o=x/2
    return o

print(ha(a))

#삼각형 넓이 구하기
import random

a=random.randint(2,20)
b=random.randint(1,10)

def ha(x,y):
    o=x*y/2
    return o

print(ha(a,b))

#사각형 넓이 구하기

import random

a=random.randint(2,20)
b=random.randint(1,10)

def ha(x,y):
    o=x*y
    return o

print(ha(a,b))

# 원 넓이 구하기

import random
import math

a=random.randint(1,5)

def ha(r):
    o=r**2*math.pi
    return o

print(ha(a))

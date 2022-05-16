import math
import sys
input=sys.stdin.readline

def p_made(x):
    for i in range(2,int(math.sqrt(x)+1)):
        if x%i==0:return False
    return True

def p_discri(y):

    p=[]
    for j in range(2,int(math.sqrt(y)+1)):
        if p_made(j):p.append(j)
    if not list(map(lambda x:y%x,p)).count(0):return True
    return False

def solution(x):
    for i in range(3,x-2,2):
        if p_discri(i) and p_discri(x-i):return [str(n),'=',str(i),'+',str(x-i)]

while True:
    n=int(input())
    if n==0:break
    print(' '.join(solution(n)))
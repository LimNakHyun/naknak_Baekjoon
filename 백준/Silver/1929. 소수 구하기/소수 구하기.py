import sys
import math
input=sys.stdin.readline

def pf(number):
    if number==1:return False
    square_root=int(math.sqrt(number))
    for i in range(2,square_root+1):
        if number%i==0:return False
    return True

m,n=map(int,input().rstrip().split())

for j in range(m,n+1):
    if pf(j):print(j)
import math
import sys
input=sys.stdin.readline

for i in range(int(input().strip())):
    n=int(input().strip())

    def pf(number): #숫자가 주어졌을 때 소수인지 판별해 주는 함수
        if number==1:return False
        square_root=int(math.sqrt(number))
        for i in range(2,square_root+1):
            if number%i==0:return False
        return True

    res=[]
    for j in range(2,int(n//2)+1):
        if pf(j) and pf(n-j):res.append([j,n-j])

    result=[]
    for k in range(len(res)):
        result.append(res[k][1]-res[k][0])

    val=min(result)

    print(res[result.index(val)][0],res[result.index(val)][1])
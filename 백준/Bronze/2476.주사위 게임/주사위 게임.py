import sys
input=sys.stdin.readline

n=int(input())
res=[]
for i in range(n):
    d=list(map(int,input().rstrip().split()))
    if d[0]==d[1] and d[1]==d[2]:
        res.append(10000+d[0]*1000)
    elif d[0]==d[1] and d[0]!=d[2]:
        res.append(1000+d[0]*100)
    elif d[0]==d[2] and d[0]!=d[1]:
        res.append(1000+d[0]*100)
    elif d[1]==d[2] and d[1]!=d[0]:
        res.append(1000+d[1]*100)
    else:
        res.append(100*max(d))
print(max(res))
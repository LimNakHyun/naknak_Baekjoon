import sys
input=sys.stdin.readline

d=list(map(int,input().rstrip().split()))
if d[0]==d[1] and d[1]==d[2]:
    print(10000+d[0]*1000)
elif d[0]==d[1] and d[0]!=d[2]:
    print(1000+d[0]*100)
elif d[0]==d[2] and d[0]!=d[1]:
    print(1000+d[0]*100)
elif d[1]==d[2] and d[1]!=d[0]:
    print(1000+d[1]*100)
else:
    print(100*max(d))